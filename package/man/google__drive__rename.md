#### Description

The `rename` command changes the name of a file in Google Drive. The file stays in
the same folder.

#### Usage

```bash
aux4 google drive rename <fileId> --name <name> [--tokenFile <path>]
```

fileId       The file ID to rename (positional argument)
--name       New name for the file
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive rename 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms --name "Q1 Budget Final"
```

```text
{
  "id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "kind": "drive#file",
  "mimeType": "application/vnd.google-apps.spreadsheet",
  "name": "Q1 Budget Final"
}
```
