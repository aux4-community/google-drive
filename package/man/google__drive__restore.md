#### Description

The `restore` command restores a file from trash in Google Drive. The file is moved back to its original location.

#### Usage

```bash
aux4 google drive restore <fileId>
```

fileId  The file ID to restore (positional argument)

#### Example

```bash
aux4 google drive restore 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```

```text
{
  "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "kind": "drive#file",
  "name": "Q1 Budget",
  "trashed": false
}
```
