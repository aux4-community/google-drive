#### Description

The `rename` command changes the name of a file in Google Drive. The file stays in the same location.

#### Usage

```bash
aux4 google drive rename <fileId> <name>
```

fileId  The file ID to rename (positional argument)
name    New name for the file (positional argument)

#### Example

```bash
aux4 google drive rename 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms "Q1 Budget Final"
```

```text
{
  "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "kind": "drive#file",
  "mimeType": "application/vnd.google-apps.spreadsheet",
  "name": "Q1 Budget Final"
}
```
