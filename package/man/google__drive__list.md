#### Description

The `list` command lists files in Google Drive. By default it returns the 20 most
recently modified non-trashed files, including each file's ID, name, MIME type,
modification time, size and web link, plus a `nextPageToken`. The query, page
size and sort order are all configurable.

The query and the sort order are percent-encoded before the request is sent, so
spaces, `=` and `/` need no escaping of your own.

The `--query` flag accepts the full Google Drive search query syntax. Common
query patterns:

- `name contains 'budget'` — files with "budget" in the name
- `mimeType = 'application/vnd.google-apps.spreadsheet'` — only spreadsheets
- `'FOLDER_ID' in parents` — files in a specific folder
- `modifiedTime > '2025-01-01'` — files modified after a date
- `trashed = true` — trashed files

Multiple conditions can be combined with `and` / `or`.

Pagination is not automatic: use the returned `nextPageToken` if you need the
next page.

#### Usage

```bash
aux4 google drive list [--query <query>] [--pageSize <n>] [--orderBy <field>] [--tokenFile <path>]
```

--query      Google Drive search query (default: `trashed = false`)
--pageSize   Number of files to return (default: 20)
--orderBy    Sort order (default: `modifiedTime desc`)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive list --query "mimeType = 'application/vnd.google-apps.spreadsheet'" --pageSize 5
```

```text
{
  "files": [
    {
      "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
      "name": "Q1 Budget",
      "mimeType": "application/vnd.google-apps.spreadsheet",
      "modifiedTime": "2025-03-15T10:30:00.000Z",
      "webViewLink": "https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms/edit"
    }
  ]
}
```
