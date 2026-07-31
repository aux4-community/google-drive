#### Description

The `export` command converts a Google Workspace document (Docs, Sheets, Slides)
to the requested format and writes it to a local file
(`GET /drive/v3/files/<fileId>/export?mimeType=<type>`). Google-native documents
cannot be downloaded directly, which is why they need this command instead of
`aux4 google drive download`.

Supported export formats:

- **application/pdf** (default) — all document types
- **text/csv** — Sheets only, first sheet
- **application/vnd.openxmlformats-officedocument.spreadsheetml.sheet** — Sheets to Excel
- **application/vnd.openxmlformats-officedocument.wordprocessingml.document** — Docs to Word
- **text/plain** — Docs to plain text
- **text/html** — Docs to HTML

The output path may be relative or absolute, and it may point outside the working
directory. If the export fails, no file is written. On success the command prints
the path it wrote.

#### Usage

```bash
aux4 google drive export <fileId> --output <path> [--mimeType <type>] [--tokenFile <path>]
```

fileId       The file ID to export (positional argument)
--output     Local file path to write to
--mimeType   Export format (default: `application/pdf`)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive export 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms --output ./budget.csv --mimeType text/csv
```

```text
Saved ./budget.csv
```
