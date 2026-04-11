#### Description

The `move` command moves a file from one folder to another in Google Drive. You must provide the destination folder ID via `--folderId`. If `--fromFolderId` is provided, the file is removed from that folder; otherwise the API removes it from its current parent automatically.

#### Usage

```bash
aux4 google drive move <fileId> --folderId <id> [--fromFolderId <id>]
```

fileId          The file ID to move (positional argument)
--folderId      Destination folder ID
--fromFolderId  Source folder ID (optional)

#### Example

```bash
aux4 google drive move 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms --folderId 0AJkGH123 --fromFolderId 0AJkGH456
```

```text
{
  "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "kind": "drive#file",
  "name": "Q1 Budget"
}
```
