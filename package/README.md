# community/google-drive

Commands to interact with Google Drive using the Google Workspace CLI

This package provides aux4 command wrappers around the [Google Workspace CLI](https://github.com/googleworkspace/cli) (`gws`) for managing Google Drive files. It covers listing, searching, uploading, downloading, exporting, copying, renaming, moving, trashing, and sharing files and folders.

## Installation

```bash
aux4 aux4 pkger install community/google-drive
```

## System Dependencies

This package requires the Google Workspace CLI (`gws`). It will be installed automatically via one of the following:

- [brew](https://brew.sh): `brew install googleworkspace-cli`
- [npm](https://www.npmjs.com): `npm install -g @googleworkspace/cli`

## Prerequisites

Before using this package, authenticate with Google:

```bash
gws auth setup
```

Or if you already have a project configured:

```bash
gws auth login
```

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

### Search by name

Search for files by name (case-insensitive, partial match):

```bash
aux4 google drive search "budget"
```

### Get file ID

Get the file ID by name or path (returns only the raw ID):

```bash
aux4 google drive id "Q1 Budget"
aux4 google drive id "reports/Q1 Budget"
```

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

### Download a file

Download a file by ID:

```bash
aux4 google drive download FILE_ID ./output.pdf
```

### Export a Google Workspace document

Export a Google Doc, Sheet, or Slide to a different format:

```bash
aux4 google drive export FILE_ID ./report.pdf
aux4 google drive export FILE_ID ./data.csv --mimeType text/csv
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
aux4 google drive rename FILE_ID "New Name"
```

### Move a file

Move a file to a different folder:

```bash
aux4 google drive move FILE_ID --folderId DESTINATION_FOLDER_ID --fromFolderId CURRENT_FOLDER_ID
```

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
aux4 google drive share add FILE_ID alice@example.com
```

Share with write access:

```bash
aux4 google drive share add FILE_ID alice@example.com --role writer
```

### List permissions

```bash
aux4 google drive share list FILE_ID
```

### Remove a permission

```bash
aux4 google drive share remove FILE_ID PERMISSION_ID
```

## Environment Variables

The Google Workspace CLI reads the following environment variables for authentication:

- `GOOGLE_WORKSPACE_CLI_TOKEN` — OAuth access token (highest priority)
- `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` — Path to credentials JSON file
- `GOOGLE_WORKSPACE_CLI_CONFIG_DIR` — Override default config directory

## License

MIT — See [LICENSE](./license) for details.
