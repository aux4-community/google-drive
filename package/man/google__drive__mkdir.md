#### Description

The `mkdir` command creates a new folder in Google Drive. A folder is a file with
the MIME type `application/vnd.google-apps.folder`. By default the folder is
created in the root of your Drive; use `--parent` to create it inside an existing
folder.

Drive allows two folders with the same name in the same parent, so `mkdir` does
not check whether the folder already exists.

#### Usage

```bash
aux4 google drive mkdir <name> [--parent <folderId>] [--tokenFile <path>]
```

name         Folder name (positional argument)
--parent     Parent folder ID (default: `root`)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive mkdir "Project Files" --parent 0AJkGH123
```

```text
{
  "id": "1FxjOWt1YSB6oGNeL8cBkArhmVVrquemct85PhFG3wqn",
  "kind": "drive#file",
  "mimeType": "application/vnd.google-apps.folder",
  "name": "Project Files"
}
```
