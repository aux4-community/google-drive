# community/google-drive

Commands to interact with Google Drive using the Drive v3 REST API.

This package talks to `https://www.googleapis.com/drive/v3` directly over
`aux4/curl`'s OAuth2 transport. It covers listing, searching, uploading,
downloading, exporting, copying, renaming, moving, trashing and sharing files
and folders.

## Installation

```bash
aux4 aux4 pkger install community/google-drive
```

## Prerequisites

Authentication is handled by `community/google-auth`, which is installed as a
dependency. Log in once and every command in this package works:

```bash
aux4 google auth login --services drive
```

Read-only access is enough for `list`, `search`, `id`, `get`, `download` and
`export`:

```bash
aux4 google auth login --services drive --readonly true
```

The token is stored at `~/.aux4.config/.oauth/google.json`. Point every command
somewhere else with `--tokenFile`, or by exporting `AUX4_GOOGLE_TOKEN_FILE`.

**Note:** the token file holds a refresh token in plain text (mode `0600`).
Treat it like an SSH private key.

## Quick Start

Search for a file by name:

```bash
aux4 google drive search "Q1 Budget"
```

List recent files:

```bash
aux4 google drive list
```

Upload a file:

```bash
aux4 google drive upload ./report.pdf
```

## Files — list, search, and inspect

### List files

List recent files (sorted by last modified, 20 results):

```bash
aux4 google drive list
```

List with a custom query:

```bash
aux4 google drive list --query "mimeType = 'application/vnd.google-apps.spreadsheet'"
```

List files sorted by name:

```bash
aux4 google drive list --orderBy name --pageSize 50
```

The query and the sort order are percent-encoded before they are sent, so spaces
and quotes need no escaping of your own.

### Search by name

Search for files by name (case-insensitive, partial match):

```bash
aux4 google drive search "budget"
```

An apostrophe in the name is escaped for you, so `aux4 google drive search
"Bob's report"` works.

### Get file ID

Get the file ID by name or path (returns only the raw ID):

```bash
aux4 google drive id "Q1 Budget"
aux4 google drive id "reports/Q1 Budget"
```

A bare name is searched for across the whole Drive. A path is walked one segment
at a time from the Drive root, and every segment except the last must be a
folder.

Combined with google sheets:

```bash
aux4 google sheets values get --spreadsheetId $(aux4 google drive id "reports/Q1 Budget") --range 'Sheet1!A1:C10'
```

### Get file metadata

Get detailed metadata for a specific file:

```bash
aux4 google drive get FILE_ID
```

## Upload and download

### Upload a file

Upload a local file to Google Drive:

```bash
aux4 google drive upload ./report.pdf
```

Upload to a specific folder with a custom name:

```bash
aux4 google drive upload ./data.csv --parent FOLDER_ID --name "Sales Data.csv"
```

The content type is detected from the file. Override it when the detection is
wrong:

```bash
aux4 google drive upload ./data.csv --mimeType text/csv
```

**Note:** an upload is two API calls, not one. The bytes are sent first and the
name and parent folder are attached immediately afterwards, so for a moment the
file exists as `Untitled` in *My Drive*. If the second call fails, that
`Untitled` file is left behind, and `aux4 google drive list --query "name = 'Untitled'"`
will find it.

### Download a file

Download a file by ID:

```bash
aux4 google drive download FILE_ID --output ./output.pdf
```

The output path can be anywhere, including an absolute path outside the working
directory:

```bash
aux4 google drive download FILE_ID --output ~/Downloads/report.pdf
```

If the request fails no file is written, so a failed download can never leave a
truncated file behind.

### Export a Google Workspace document

Export a Google Doc, Sheet, or Slide to a different format:

```bash
aux4 google drive export FILE_ID --output ./report.pdf
aux4 google drive export FILE_ID --output ./data.csv --mimeType text/csv
```

Supported export formats:

- `application/pdf` (default)
- `text/csv` (Sheets)
- `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (Sheets to Excel)
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document` (Docs to Word)
- `text/plain` (Docs to plain text)
- `text/html` (Docs to HTML)

## File operations — copy, rename, move, trash

### Copy a file

```bash
aux4 google drive copy FILE_ID --name "Budget Copy"
```

### Rename a file

```bash
aux4 google drive rename FILE_ID --name "New Name"
```

### Move a file

Move a file to a different folder:

```bash
aux4 google drive move FILE_ID --folderId DESTINATION_FOLDER_ID
```

A Drive file has a single parent, so the previous folder is replaced. Pass
`--fromFolderId` to remove a specific parent explicitly, which matters for a
file in a shared drive.

### Trash and restore

Move a file to trash:

```bash
aux4 google drive trash FILE_ID
```

Restore a file from trash:

```bash
aux4 google drive restore FILE_ID
```

### Permanently delete

Permanently delete a file (prompts for confirmation):

```bash
aux4 google drive delete FILE_ID
```

## Folders

Create a new folder:

```bash
aux4 google drive mkdir "Project Files"
```

Create a subfolder:

```bash
aux4 google drive mkdir "Reports" --parent PARENT_FOLDER_ID
```

## Sharing — manage permissions

### Share a file

Share with a user (default role: reader):

```bash
aux4 google drive share add FILE_ID --email alice@example.com
```

Share with write access:

```bash
aux4 google drive share add FILE_ID --email alice@example.com --role writer
```

### List permissions

```bash
aux4 google drive share list FILE_ID
```

### Remove a permission

```bash
aux4 google drive share remove FILE_ID --permissionId PERMISSION_ID
```

## Scopes

The package declares two scopes and `aux4 google auth login` requests the one
that matches how you logged in:

| Login | Scope |
|-------|-------|
| `aux4 google auth login --services drive` | `https://www.googleapis.com/auth/drive` |
| `aux4 google auth login --services drive --readonly true` | `https://www.googleapis.com/auth/drive.readonly` |

The writing commands (`upload`, `copy`, `rename`, `move`, `trash`, `restore`,
`delete`, `mkdir`, `share add`, `share remove`) fail with a permission error
under a read-only login.

## Environment Variables

- `AUX4_GOOGLE_TOKEN_FILE` — where the OAuth token is read from and written to
  (default `~/.aux4.config/.oauth/google.json`)

## License

MIT — See [LICENSE](./LICENSE) for details.
