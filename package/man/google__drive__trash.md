#### Description

The `trash` command moves a file to trash in Google Drive. The file can be restored later using `aux4 google drive restore`. Trashed files are automatically deleted after 30 days.

#### Usage

```bash
aux4 google drive trash <fileId>
```

fileId  The file ID to trash (positional argument)

#### Example

```bash
aux4 google drive trash 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```

```text
{
  "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "kind": "drive#file",
  "name": "Q1 Budget",
  "trashed": true
}
```
