#### Description

The `download` command downloads the content of a file from Google Drive
(`GET /drive/v3/files/<fileId>?alt=media`) and writes it to a local path. This
works for uploaded files such as PDFs, images and archives. Google-native
documents (Docs, Sheets, Slides) have no downloadable content, so use
`aux4 google drive export` for those.

The output path may be relative or absolute, and it may point anywhere on the
filesystem, including outside the working directory.

If the request fails, the error is reported and **no file is written**, so a
failed download can never leave a truncated or error-page file behind. On success
the command prints the path it wrote.

#### Usage

```bash
aux4 google drive download <fileId> --output <path> [--tokenFile <path>]
```

fileId       The file ID to download (positional argument)
--output     Local file path to write to
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive download 1DxjOWt1YSB6oGNeL8cBkArhmVVrquemct85PhFG3wqn --output ~/Downloads/report.pdf
```

```text
Saved /Users/alice/Downloads/report.pdf
```

When the file does not exist or access is denied:

```bash
aux4 google drive download nope --output ./report.pdf
```

```text
Error: HTTP 404
{"error": {"code": 404, "message": "File not found: nope."}}
```
