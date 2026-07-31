#### Description

The `get` command retrieves detailed metadata for a file by its ID. The response
includes the file name, MIME type, modification time, size, web link, parent
folders, sharing status and owner information.

#### Usage

```bash
aux4 google drive get <fileId> [--tokenFile <path>]
```

fileId       The file ID (positional argument)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive get 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```

```text
{
  "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "name": "Q1 Budget",
  "mimeType": "application/vnd.google-apps.spreadsheet",
  "modifiedTime": "2025-03-15T10:30:00.000Z",
  "webViewLink": "https://docs.google.com/spreadsheets/d/.../edit",
  "parents": ["0AJkGH..."],
  "shared": true,
  "owners": [{"displayName": "Alice", "emailAddress": "alice@example.com"}]
}
```
