"""Render an LLD Markdown file to a standalone HTML page (RTL by default).

The Markdown file is the single source of truth: this script regenerates the HTML in full on every
run, and the HTML is never edited by hand.

Usage: python3 md_to_html.py lld_<feature>.md [-o out.html] [--lang he|en]

Supports the Markdown subset the LLD template uses: headings, paragraphs, bold, inline code,
links, images, pipe tables (with hierarchy group rows), bullet lists, blockquotes, fenced code
blocks, and <br> inside table cells. Traceability IDs (UI-01, CMS-03, ...) become links to their
definitions.
"""
import argparse, html, os, re

ID = re.compile(r'(?:UI|CMS|API|BR|SC|BQ|TQ|AS)-\d{2}')

CSS = """
:root { --ink:#1d2433; --muted:#5b6475; --line:#d9dee7; --head:#f2f5f9; --accent:#0b6e99; }
* { box-sizing:border-box; }
body { margin:0; background:#fff; color:var(--ink); font:15px/1.6 "Segoe UI","Arial Hebrew",Arial,sans-serif; }
main { max-width:1200px; margin:0 auto; padding:32px 16px 64px; }
h1 { font-size:26px; border-bottom:3px solid var(--accent); padding-bottom:8px; }
h2 { font-size:21px; margin-top:40px; border-bottom:1px solid var(--line); padding-bottom:4px; color:var(--accent); }
h3 { font-size:17px; margin-top:28px; } h4, h5, h6 { font-size:15px; margin-top:20px; }
code { font-family:Consolas,Menlo,monospace; font-size:.88em; background:#eef2f6; padding:1px 5px; border-radius:4px;
       direction:ltr; unicode-bidi:isolate; white-space:nowrap; }
pre { direction:ltr; text-align:left; background:#f6f8fa; border:1px solid var(--line); border-radius:6px; padding:10px 12px; overflow-x:auto; }
pre code { background:none; padding:0; white-space:pre; }
.table-wrap { overflow-x:auto; margin:12px 0 20px; }
table { border-collapse:collapse; width:100%; font-size:14px; }
th, td { border:1px solid var(--line); padding:6px 9px; vertical-align:top; text-align:start; }
th { background:var(--head); font-weight:600; }
tr.group td { background:#fafbfd; font-weight:600; }
td img { max-width:220px; height:auto; display:block; }
blockquote { margin:12px 0; padding:8px 14px; border-inline-start:4px solid var(--accent); background:#f5f9fc; color:var(--muted); }
a.ref { text-decoration:none; } a.ref code { color:var(--accent); } a.ref:hover code { text-decoration:underline; }
[id] { scroll-margin-top:16px; } :target, :target td { background:#fff6d6 !important; }
.generated { color:var(--muted); font-size:12px; margin-bottom:24px; }
@media print {
  main { max-width:none; padding:0; } body { font-size:11pt; }
  h2 { break-after:avoid; } tr, img, pre { break-inside:avoid; } thead { display:table-header-group; }
  .table-wrap { overflow:visible; } a { color:inherit; text-decoration:none; } .generated { display:none; }
}
@page { size:A4 landscape; margin:14mm; }
"""

BLOCK_START = re.compile(r'^(#{1,6}\s|\||\s*- |>|\s*```)')


def inline(text):
    out = []
    for part in re.split(r'(`[^`]+`)', text):  # code spans are rendered verbatim
        if len(part) > 1 and part.startswith('`') and part.endswith('`'):
            c = part[1:-1]
            out.append(f'<a class="ref" href="#{c}"><code>{c}</code></a>' if ID.fullmatch(c)
                       else f'<code>{html.escape(c)}</code>')
            continue
        p = html.escape(part).replace('&lt;br&gt;', '<br>')
        p = re.sub(r'!\[([^\]]*)\]\(([^)\s]+)\)', r'<img src="\2" alt="\1" loading="lazy">', p)
        p = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', p)
        p = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p)
        out.append(p)
    return ''.join(out)


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def render(md):
    lines, out, i = md.splitlines(), [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.strip().startswith('```'):
            i += 1
            code = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code.append(lines[i]); i += 1
            i += 1
            indent = min((len(l) - len(l.lstrip()) for l in code if l.strip()), default=0)
            out.append('<pre><code>' + html.escape('\n'.join(l[indent:] for l in code)) + '</code></pre>')
        elif m := re.match(r'^(#{1,6})\s+(.*)', line):
            n, d = len(m[1]), ID.match(m[2])
            out.append(f'<h{n}' + (f' id="{d[0]}"' if d else '') + f'>{inline(m[2])}</h{n}>'); i += 1
        elif line.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            head = cells(line); i += 2
            t = ['<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>']
            while i < len(lines) and lines[i].startswith('|'):
                r = cells(lines[i]); i += 1
                r += [''] * (len(head) - len(r))
                if not r[0] and any(c.startswith('**') for c in r):  # "| | **רמה 2** | | |" hierarchy row
                    t.append(f'<tr class="group"><td colspan="{len(head)}">{inline(" ".join(c for c in r if c))}</td></tr>')
                else:
                    t.append((f'<tr id="{r[0]}">' if ID.fullmatch(r[0]) else '<tr>') + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            out.append(''.join(t) + '</tbody></table></div>')
        elif re.match(r'^\s*- ', line):
            items = []
            while i < len(lines) and re.match(r'^\s*- ', lines[i]):
                item = lines[i].strip()[2:]; i += 1
                d = re.match(rf'`({ID.pattern})`', item)
                body = [inline(item)]
                while i < len(lines) and lines[i].startswith('  ') and not re.match(r'^\s*(- |```)', lines[i]):
                    body.append(inline(lines[i].strip())); i += 1  # wrapped continuation line
                items.append((f'<li id="{d[1]}">' if d else '<li>') + '<br>'.join(body) + '</li>')
            out.append('<ul>' + ''.join(items) + '</ul>')
        elif line.startswith('>'):
            quote = []
            while i < len(lines) and lines[i].startswith('>'):
                quote.append(lines[i].lstrip('> ').rstrip()); i += 1
            out.append(f'<blockquote>{inline(" ".join(quote))}</blockquote>')
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not BLOCK_START.match(lines[i]):
                para.append(inline(lines[i].strip())); i += 1
            out.append('<p>' + '<br>'.join(para) + '</p>')
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('src', help='LLD Markdown file')
    ap.add_argument('-o', '--out', help='output HTML path (default: next to the Markdown file)')
    ap.add_argument('--lang', default='he', help='document language; he/ar/fa render RTL (default: he)')
    a = ap.parse_args()
    md = open(a.src, encoding='utf-8').read()
    dst = a.out or os.path.splitext(a.src)[0] + '.html'
    title = (re.search(r'^#\s+(.*)', md, re.M) or [None, 'LLD'])[1]
    direction = 'rtl' if a.lang in ('he', 'ar', 'fa') else 'ltr'
    note = f'Generated from {os.path.basename(a.src)} — do not edit this file; edit the Markdown and regenerate.'
    page = (f'<!doctype html>\n<html lang="{a.lang}" dir="{direction}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)}</title>'
            f'<style>{CSS}</style></head><body><main>\n<!-- {note} -->\n<div class="generated" dir="ltr">{note}</div>\n'
            f'{render(md)}\n</main></body></html>\n')
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(page)
    print(dst)


if __name__ == '__main__':
    main()
