#### Description

The `upload` command uploads a local file to Google Drive and returns the metadata
of the new file. The content type is detected from the file, and `--mimeType`
overrides the detection.

**An upload is two API calls, and it is not atomic.** Drive's single-call upload
needs a `multipart/related` request body, which `aux4/curl` cannot produce yet, so
`upload` does this instead:

1. `POST /upload/drive/v3/files?uploadType=media` sends the raw bytes with the
   detected content type and an exact `Content-Length`. Drive creates a file named
   `Untitled` in *My Drive* and returns its ID.
2. `PATCH /drive/v3/files/<id>` attaches the name and, when `--parent` was given,
   the parent folder.

The consequences are worth knowing:

- For a moment the file exists as `Untitled` in the Drive root.
- If the second call fails, that `Untitled` file stays behind.
  `aux4 google drive list --query "name = 'Untitled'"` finds it.

If the local file does not exist, the command fails before any request is sent.

#### Usage

```bash
aux4 google drive upload <file> [--parent <folderId>] [--name <name>] [--mimeType <type>] [--tokenFile <path>]
```

file         Path to the local file to upload (positional argument)
--parent     Parent folder ID (optional, defaults to the Drive root)
--name       Target filename (optional, defaults to the source filename)
--mimeType   Content type to send (optional, detected from the file when omitted)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive upload ./report.pdf --parent 0AJkGH123 --name "Q1 Report.pdf"
```

```text
{
  "id": "1DxjOWt1YSB6oGNeL8cBkArhmVVrquemct85PhFG3wqn",
  "kind": "drive#file",
  "mimeType": "application/pdf",
  "name": "Q1 Report.pdf",
  "parents": ["0AJkGH123"],
  "webViewLink": "https://drive.google.com/file/d/1DxjOWt1YSB6oGNeL8cBkArhmVVrquemct85PhFG3wqn/view"
}
```

Force the content type when the detection is wrong, which is common for CSV:

```bash
aux4 google drive upload ./data.csv --mimeType text/csv
```
