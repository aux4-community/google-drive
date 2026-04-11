#### Description

The `mkdir` command creates a new folder in Google Drive. By default the folder is created in the root of your Drive. Use `--parent` to create it inside an existing folder.

#### Usage

```bash
aux4 google drive mkdir <name> [--parent <folderId>]
```

name      Folder name (positional argument)
--parent  Parent folder ID (default: root)

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
