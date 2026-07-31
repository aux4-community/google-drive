#### Description

The `restore` command restores a file from trash in Google Drive. The file returns
to the folder it was in before it was trashed.

To find the ID of a trashed file, list the trash:

```bash
aux4 google drive list --query "trashed = true"
```

#### Usage

```bash
aux4 google drive restore <fileId> [--tokenFile <path>]
```

fileId       The file ID to restore (positional argument)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive restore 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```

```text
{
  "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "name": "Q1 Budget",
  "mimeType": "application/vnd.google-apps.spreadsheet",
  "trashed": false
}
```
