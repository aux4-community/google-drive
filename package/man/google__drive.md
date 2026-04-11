#### Description

The `google drive` command group provides access to Google Drive operations through the Google Workspace CLI (`gws`). It covers file management, uploads, downloads, exports, and sharing.

Available subcommands:

- **list** — List files in Google Drive
- **search** — Search files by name
- **id** — Get the file ID by name or path
- **get** — Get file metadata by ID
- **copy** — Create a copy of a file
- **rename** — Rename a file
- **move** — Move a file to a different folder
- **delete** — Permanently delete a file
- **trash** — Move a file to trash
- **restore** — Restore a file from trash
- **upload** — Upload a local file
- **download** — Download a file
- **export** — Export a Google Workspace document
- **mkdir** — Create a folder
- **share** — Manage sharing permissions

#### Usage

```bash
aux4 google drive <subcommand>
```

#### Example

```bash
aux4 google drive search "budget"
aux4 google drive upload ./report.pdf
```
