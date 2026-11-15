# LLD Template — Web + Backend

Use this structure for every LLD. Section numbers never change, so documents in different languages map one-to-one. Section titles are localized to the document language (Hebrew by default); IDs, technical identifiers, API field names, and data types stay in English.

A section that doesn't apply keeps its heading, with one line: `לא רלוונטי לפיצ'ר זה – <reason>` (or the equivalent in the document language). Don't delete it and don't renumber the sections after it. Don't add mandatory sections, tables, or columns beyond those below.

## Section map

| # | Hebrew title | English title | When |
|---|---|---|---|
| 1 | היסטוריית שינויים | Change History | Always |
| 2 | מסמכים ומקורות קשורים | Related Documents and Sources | Always |
| 3 | סקירה והיקף | Overview and Scope | Always |
| 4 | צד הגולש | Website Visitor | Always. No visitor side at all (a process-only feature): the heading stays with `לא רלוונטי לפיצ'ר זה – תהליך ללא ממשק משתמש`. Visitor side exists but its design hasn't arrived: `לא רלוונטי בשלב זה – ממתין לעיצוב`, and the section is added in a later version, keeping existing IDs |
| 5 | אינטגרציה וכללים עסקיים | Integration and Business Rules | When the feature calls any API (new or existing) or has a scenario crossing frontend, backend, or CMS beyond plain rendering of CMS content |
| 6 | צד העורך | Content Editor | When a CMS manages any part of the feature |

## ID scheme

Every component, field, rule, scenario, API operation, open item, and assumption has a unique ID. Other rows reference it by ID instead of repeating its content.

| Code | Meaning | Defined in |
|---|---|---|
| `CAP-xx` | Capability of the feature – the unit of understanding and of development readiness | 3.1 |
| `SR-xx` | Source-reading rule – how a source is read: what is valid, superseded, interpreted, or how a conflict was resolved | 2.2 |
| `UI-xx` | Displayed component | 4.4 |
| `CMS-xx` | Field a content editor fills in | 6.4 |
| `BR-xx` | Business rule | 5.1 |
| `SC-xx` | Cross-system scenario | 5.2 |
| `API-xx` | API operation the feature uses — new, changed, or existing (existing: link only) | 5.3 |
| `BQ-xx` / `TQ-xx` | Open question — business / technical | End of the section it belongs to |
| `AS-xx` | Assumption not yet confirmed | End of the section it belongs to |

Reference rules:

- **Code plus short name.** Write the code followed by a short name — `SC-01 חישוב תוצאות`, `BR-05 פילטר לפי תג` — so the reader understands it without looking it up. When the name already appears in the same sentence, the code alone in parentheses is enough.
- **Say shared things once.** When the same reference would repeat on every row of a table (for example, every rule's execution location is "to be decided by the development team"), state it once above the table instead.
- **Range references** such as `` `CMS-20` עד `CMS-35` `` count as references to every ID in the range.
- **Definitions** are the first cell of a table row (`| UI-01 |`), a list item that starts with the code (`` - `BQ-01` name: … ``), or a heading that starts with the code (`#### SC-01 – …`). `scripts/trace_check.py` relies on these three forms.

## Skeleton

```md
# מסמך אפיון LLD – [שם הפיצ'ר]

**סטטוס:** DRAFT
**פרויקט:** [שם הפרויקט]
**מסמך אושר ע"י:** [לפי הפרויקט]
**עודכן לאחרונה:** [DD/MM/YYYY]

## 1. היסטוריית שינויים

| תאריך | גרסה | תיאור השינוי | מחבר השינוי |
|---|---|---|---|
| [DD/MM/YYYY] | 0.1 | [תיאור] | [שם] |

## 2. מסמכים ומקורות קשורים

### 2.1 מקורות ומקרא

| מקור | קישור | סטטוס |
|---|---|---|
| [מסמך דרישה / HLD / Figma / חוזה API / ריפו / אפיון מופנה] | [קישור או –] | [נקרא / חסר / אין גישה – ומה נעשה במקום] |

**מקרא קודים.** [טבלת הקודים מסעיף "ID scheme", רק עם הקודים שמופיעים במסמך, וציון שבגרסת ה-HTML לחיצה על קוד מובילה להגדרה שלו.]

### 2.2 כללי קריאת המקורות

[משפט פתיחה: כללי קריאה שחלים על כל הפרויקט נרשמים במקום שהפרויקט קובע ומופנים לכאן לפי מזהה, בלי העתקה. כשאין כללי קריאה: "אין – המקורות נקראו כלשונם".]

| ID | במקור | כלל הקריאה | נימוק | הוחלט ע"י |
|---|---|---|---|---|
| SR-01 | [מקור וסעיף, או סיכום פגישה ותאריך] | [מה תקף / מה מוחלף ובמה / איך מתפרש מונח / איך הוכרעה סתירה / מה לא נלקח בחשבון] | [למה] | [אנליסט / החלטה רוחבית / `BQ-xx` שנסגר] |

## 3. סקירה והיקף

### 3.1 תיאור הפיצ'ר
[פסקת פתיחה: מה הפיצ'ר כולו עושה, למי, ואיך היכולות שלו מתחברות זו לזו.]

#### CAP-01 – [שם היכולת]

**מטרה עסקית:** [איזו בעיה היכולת פותרת ולמי. משפט או שניים.]

**מה היכולת עושה:** [פרוזה של 3–8 משפטים: מה מפעיל אותה, מה קורה בדרך ומה התוצאה. כתוב כך שקורא שלא היה בראיון יבין בלי לפתוח סעיף אחר.]

**מי מפעיל ומי מושפע:** [תפקידים, מערכות, תהליכים אוטומטיים.]

**קריטריונים לקבלה:** [חובה כשסעיף 4 לא רלוונטי או נדחה. קריטריונים שניתן לבדוק, עם הפניה ל-`BR-xx` / `SC-xx`.]
- [קריטריון]

**פירוט:** [הפניות לכללים, לתרחישים ולישויות של היכולת.]

### 3.2 שכבות מושפעות

| שכבה | מושפעת? | פירוט |
|---|---|---|
| Web UI | [כן / לא] | [סעיף 4] |
| Backend | [חדש / משתנה / שימוש בקיים / לא] | [סעיף 5] |
| CMS | [כן – <CMS וגרסה> / לא] | [סעיף 6] |

### 3.3 מחוץ להיקף
- [פריט]

### 3.4 מוכנות לפיתוח

[נכון לגרסה X. פרט שמסומן חסום לא ממומש ע"י השלמה עצמית – לא ע"י מפתח ולא ע"י כלי AI.]

| יכולת | סטטוס | ניתן לפתח עכשיו | חסום, ולמה | תלוי ב- |
|---|---|---|---|---|
| `CAP-01` [שם] | [ניתן לפיתוח / ניתן לפיתוח חלקית / חסום] | [מה] | [מה, ומה מותר בינתיים, או "לא לממש"] | [`BQ-xx`, `TQ-xx`, `AS-xx`, מסמך אחר, תלות חיצונית, עיצוב] |

## 4. צד הגולש

### 4.1 סיפור משתמש
[מטרת הגולש.]

### 4.2 תנאים מקדימים
- [תנאי]

### 4.3 הנחות יסוד ואילוצים
- [הנחה או אילוץ שאושרו]

### 4.4 טבלת רכיבים

| ID | רכיב | תיאור ופרטים | מקור התוכן | לוגיקה ומצבים | המחשה |
|---|---|---|---|---|---|
| UI-01 | [שם] | [מה מוצג, כולל אייקונים] | [`CMS-xx` שם / `API-xx` → `field.path` / מילון `key` / קבוע / נגזר – `BR-xx`, או הכלל בעמודת הלוגיקה כשסעיף 5 לא רלוונטי] | [מצבים ומקרי קצה; עבור API: מתי נקרא, הצלחה/ריק/שגיאה/כשל חלקי] | [צילום מסך או קישור Figma] |

### 4.5 רספונסיביות ונגישות
[רק דרישות ייחודיות לפיצ'ר וחריגות מההתנהגות הסטנדרטית של סביבת הפיתוח.]

| נושא | דרישה | רכיבים |
|---|---|---|
| [רספונסיביות / נגישות] | [דרישה] | [`UI-xx`] |

### 4.6 קריטריונים לקבלה
- [קריטריון שניתן לבדוק, עם הפניה ל-`UI-xx` / `SC-xx`]

### 4.7 נושאים פתוחים והנחות

**נושאים עסקיים פתוחים**
- `BQ-01` [שם קצר]: [שאלה]

**נושאים טכניים פתוחים**
- `TQ-01` [שם קצר] (בעלים: [אנליסט / צוות פיתוח / ...]): [שאלה]

**הנחות**
- `AS-01` [שם קצר]: [הנחה]

## 5. אינטגרציה וכללים עסקיים

### 5.1 כללים עסקיים

[הכללים מקובצים לפי יכולת. חובות שהמסמך מטיל על מסמכים אחרים, כשיש כאלה, בקבוצה נפרדת בסוף.]

**`CAP-01` – [שם היכולת]**

| ID | כלל | פירוט | מקור |
|---|---|---|---|
| BR-01 | [שם] | [התנהגות בלבד: הכלל המלא, כולל המערכת שמבצעת אותו או "ייקבע ע"י צוות הפיתוח" עם הפניה ל-TQ. כלל חסום מסומן "חסום – `BQ-xx`"] | [סעיף במקור / `SR-xx` / החלטה רוחבית. ריק כשהכלל נקבע בראיון] |

### 5.2 תרחישים חוצי מערכות

#### SC-01 – [שם התרחיש]

| היבט | פירוט |
|---|---|
| טריגר | [פעולות או אירועים שמפעילים, עם `UI-xx`] |
| מקורות נתונים | [`CMS-xx`, `API-xx`, מקורות חיצוניים] |
| כללים | [`BR-xx`, ומי מבצע כל אחד] |
| קלט | [מה עובר בין המערכות] |
| פלט | [מה חוזר ולאן] |
| מה הגולש רואה | [טעינה / הצלחה / ריק / שגיאה / כשל חלקי, עם `UI-xx`. כשאין צד גולש, השורה נקראת "מי מקבל את התוצאה": משתמש מושפע, יומן, מערכת אחרת] |
| שלבים | [חובה כשיש בתרחיש יותר מפעולה אחת: רשימה ממוספרת של השלבים, ומי מבצע כל שלב, כולל ענפי כשל] |

### 5.3 חוזי API

[כל פעולה שהפיצ'ר משתמש בה מקבלת `API-xx`. פעולה קיימת: שורה אחת עם קישור לחוזה והשדות שהפיצ'ר צורך, בלי לשכפל את החוזה. פעולה חדשה או משתנה: בלוק מלא, עם "(מוצע)" ליד כל ערך שמוצע לפי המוסכמות ועוד לא אושר ע"י צוות ה-Backend.]

#### API-01 – `[METHOD] /path` (קיים)

[קישור לחוזה]. שדות בשימוש: `[field]`, `[field]`.

#### API-02 – `[METHOD] /path` (מוצע)

- **מטרה:** [משפט אחד]
- **הרשאה:** [תפקיד / scope / ללא]
- **Request (מוצע):** [ללא גוף, כשאין]
  ```json
  { }
  ```
- **Response – הצלחה ([status]) (מוצע):**
  ```json
  { }
  ```
- **ולידציה:** [כללים לכל שדה בבקשה, כשיש קלט]
- **שגיאות:**

| Status | מצב | Body | מה הגולש רואה |
|---|---|---|---|
| [status לפי המוסכמה, או status (מוצע)] | [מצב] | [מבנה, `errorCode`: `VALUE` (מוצע)] | [`UI-xx` / התנהגות] |

- **תאימות לאחור:** [רק כשמשנים חוזה קיים]

### 5.4 שינויי נתונים

| ישות | שדה | סוג | אילוצים | חדש / קיים | הערות |
|---|---|---|---|---|---|
| [entity] | [field] | [type] | [required, unique, FK...] | [חדש / קיים] | [הערות] |

[השלכות מיגרציה על נתונים קיימים, או "אין". שינויי סכמה ב-CMS נכתבים בסעיף 6.4 בלבד.]

### 5.5 אינטגרציות ותלויות
[שירותים חיצוניים, תורים ו-APIs, ומה קורה כשאחד מהם לא זמין.]

### 5.6 נושאים פתוחים והנחות
[באותו מבנה כמו 4.7.]

## 6. צד העורך

### 6.1 סיפור משתמש
[מטרת עורך התוכן.]

### 6.2 תנאים מקדימים
- [תנאי]

### 6.3 הנחות יסוד ואילוצים
- [למשל: מספר המופעים המותר של התבנית]

### 6.4 מבנה התוכן ושדות
[משפט פתיחה לכל תבנית: מה עורך התוכן מזין כשהוא משלב את הרכיב או יוצר את הדף. אופן חלוקת הטבלאות נתון לשיקול האנליסט – ראו `lld_instructions.md`.]

#### 6.4.1 [שם התבנית או סוג התוכן]

| ID | שם שדה | תיאור | סוג שדה ([CMS וגרסה]) | חובה | בקרות ומגבלות | הערות לעורך |
|---|---|---|---|---|---|---|
| | **[רמה / קבוצה בהיררכיה]** | | | | | |
| CMS-01 | [שם] | [תפקיד השדה] | [שם העורך המדויק] | [כן / לא] | [ולידציה, מגבלות, ברירת מחדל כשרלוונטי] | [הנחיות לעורך] |

### 6.5 אופן הגעת התוכן לאתר

| שדה | נצרך ב- | עיבוד | התנהגות כשהתוכן חסר |
|---|---|---|---|
| [`CMS-xx`] | [`UI-xx` / `SC-xx` / `API-xx`] | [מיפוי, טרנספורמציה] | [fallback] |

[caching ועדכניות, או הפניה ל-TQ.]

### 6.6 הרשאות

| יחידה / תפקיד | קבוצה | יצירה | עריכה | אישור | פרסום |
|---|---|---|---|---|---|

### 6.7 Work Flow
[הפניה לתהליך קיים, או תיאור תהליך האישור והפרסום.]

### 6.8 קריטריונים לקבלה
- [קריטריון שניתן לבדוק]

### 6.9 נושאים פתוחים והנחות
[באותו מבנה כמו 4.7.]
```
