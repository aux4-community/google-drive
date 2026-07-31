#### Description

The `copy` command creates a copy of a file in Google Drive. The copy is placed in
the same folder as the original. Provide a name for the copy with `--name`.

#### Usage

```bash
aux4 google drive copy <fileId> --name <name> [--tokenFile <path>]
```

fileId       The file ID to copy (positional argument)
--name       Name for the copy
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive copy 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms --name "Q1 Budget Copy"
```

```text
{
  "id": "1CzjOWt1YSB6oGNeL8cBkArhmVVrquemct85PhFG3wqn",
  "kind": "drive#file",
  "mimeType": "application/vnd.google-apps.spreadsheet",
  "name": "Q1 Budget Copy"
}
```
