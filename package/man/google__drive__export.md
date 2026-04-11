#### Description

The `export` command exports a Google Workspace document (Docs, Sheets, Slides) to a specified format and saves it to a local file. This is required for Google-native documents which cannot be downloaded directly.

Supported export formats:

- **application/pdf** (default) — all document types
- **text/csv** — Sheets only
- **application/vnd.openxmlformats-officedocument.spreadsheetml.sheet** — Sheets to Excel
- **application/vnd.openxmlformats-officedocument.wordprocessingml.document** — Docs to Word
- **text/plain** — Docs to plain text
- **text/html** — Docs to HTML

#### Usage

```bash
aux4 google drive export <fileId> <output> [--mimeType <type>]
```

fileId      The file ID to export (positional argument)
output      Local file path to save to (positional argument)
--mimeType  Export format (default: application/pdf)

#### Example

```bash
aux4 google drive export 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms ./budget.csv --mimeType text/csv
```
