"""Traceability check for an LLD Markdown file.

Fails (exit 1) when:
- an ID is referenced but never defined;
- an ID is defined more than once;
- a field, rule, scenario, API operation, open question, or assumption is defined but nothing
  references it outside its own definition line. UI components are exempt (they are the top of the
  trace), and so are closed items (definition line contains "נסגר" or "Closed").
Gaps in open-item and assumption numbering (BQ, TQ, AS) are reported as a warning: close them
before the first share, then keep IDs stable. UI and CMS IDs may be numbered in blocks (CMS-01.., CMS-20..).

Usage: python3 trace_check.py lld_<feature>.md
Definitions are a table row's first cell (| UI-01 |), a list item starting with the code
(- `BQ-01` ...), or a heading starting with the code (#### SC-01 – ...).
"""
import re, sys
from collections import Counter, defaultdict

ID = r'(?:UI|CMS|API|BR|SC|BQ|TQ|AS)-\d{2}'
DEF_PATTERNS = (rf'^\| ({ID}) \|.*$', rf'^\s*- `({ID})`.*$', rf'^#+ ({ID})\b.*$')


def expand_ranges(text):
    """IDs covered by ranges such as `CMS-20` עד `CMS-35` (endpoints excluded; they are counted directly)."""
    out = []
    for a, b in re.findall(rf'`({ID})`\s*(?:עד|to|–|-)\s*`({ID})`', text):
        prefix = a.rsplit('-', 1)[0]
        out += [f'{prefix}-{n:02d}' for n in range(int(a[-2:]) + 1, int(b[-2:]))]
    return out


def check(text):
    defs, duplicates = {}, []
    for pattern in DEF_PATTERNS:
        for m in re.finditer(pattern, text, re.M):
            if m[1] in defs:
                duplicates.append(m[1])
            defs[m[1]] = m[0]
    refs = Counter(re.findall(ID, text) + expand_ranges(text))
    for i, line in defs.items():  # a mention on an ID's own definition line is not a reference
        refs[i] -= len(re.findall(re.escape(i), line))
    undefined = sorted(i for i in refs if i not in defs)
    unused = sorted(i for i, line in defs.items()
                    if refs[i] < 1 and not i.startswith('UI') and 'נסגר' not in line and 'Closed' not in line)
    numbers = defaultdict(set)
    for i in defs:
        prefix, n = i.rsplit('-', 1)
        numbers[prefix].add(int(n))
    gaps = sorted(f'{p}-{n:02d}' for p, ns in numbers.items() if p in ('BQ', 'TQ', 'AS') for n in range(1, max(ns)) if n not in ns)
    return undefined, sorted(set(duplicates)), unused, gaps


def main():
    undefined, duplicates, unused, gaps = check(open(sys.argv[1], encoding='utf-8').read())
    print('Referenced but not defined:', ', '.join(undefined) or 'none')
    print('Defined more than once:', ', '.join(duplicates) or 'none')
    print('Defined but never referenced:', ', '.join(unused) or 'none')
    if gaps:
        print('Warning – numbering gaps (close them before the first share):', ', '.join(gaps))
    sys.exit(1 if undefined or duplicates or unused else 0)


if __name__ == '__main__':
    main()
