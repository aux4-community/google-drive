#### Description

The `trash` command moves a file to trash in Google Drive. The file can be brought
back with `aux4 google drive restore`. Trashed files are deleted permanently by
Google after 30 days.

#### Usage

```bash
aux4 google drive trash <fileId> [--tokenFile <path>]
```

fileId       The file ID to trash (positional argument)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive trash 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```

```text
{
  "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "name": "Q1 Budget",
  "mimeType": "application/vnd.google-apps.spreadsheet",
  "trashed": true
}
```
