#### Description

The `search` command finds files by name using a case-insensitive partial match. It automatically filters out trashed files. This is a convenience command — for advanced queries, use `aux4 google drive list --query`.

#### Usage

```bash
aux4 google drive search <name> [--pageSize <n>]
```

name       File name to search for (positional argument)
--pageSize  Number of results to return (default: 10)

#### Example

```bash
aux4 google drive search "budget"
```

```text
{
  "files": [
    {
      "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
      "name": "Q1 Budget",
      "mimeType": "application/vnd.google-apps.spreadsheet",
      "modifiedTime": "2025-03-15T10:30:00.000Z",
      "webViewLink": "https://docs.google.com/spreadsheets/d/.../edit"
    }
  ]
}
```
