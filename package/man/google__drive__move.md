#### Description

The `move` command moves a file from one folder to another in Google Drive. The
destination folder ID is required.

A Drive file has a single parent, so adding the destination replaces the previous
folder and `--fromFolderId` is usually unnecessary. Pass it when the file has
more than one parent, which can happen for files in a shared drive, and only the
named parent is removed.

#### Usage

```bash
aux4 google drive move <fileId> --folderId <id> [--fromFolderId <id>] [--tokenFile <path>]
```

fileId          The file ID to move (positional argument)
--folderId      Destination folder ID
--fromFolderId  Folder ID to remove the file from (optional)
--tokenFile     Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive move 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms --folderId 0AJkGH123
```

```text
{
  "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "kind": "drive#file",
  "mimeType": "application/vnd.google-apps.spreadsheet",
  "name": "Q1 Budget"
}
```
