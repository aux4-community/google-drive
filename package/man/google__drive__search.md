#### Description

The `search` command finds files by name using a case-insensitive partial match
(`name contains '<name>'`). Trashed files are filtered out. This is a convenience
wrapper: for advanced queries use `aux4 google drive list --query`.

An apostrophe in the name is escaped for the Drive query language, and the whole
query is percent-encoded, so a name like `Bob's report` is searched for
correctly.

#### Usage

```bash
aux4 google drive search <name> [--pageSize <n>] [--tokenFile <path>]
```

name         File name to search for (positional argument)
--pageSize   Number of results to return (default: 10)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

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
