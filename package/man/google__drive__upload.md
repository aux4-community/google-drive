#### Description

The `upload` command uploads a local file to Google Drive. The MIME type is detected automatically from the file extension. You can optionally specify a parent folder and a custom filename.

#### Usage

```bash
aux4 google drive upload <file> [--parent <folderId>] [--name <name>]
```

file      Path to the local file to upload (positional argument)
--parent  Parent folder ID (optional, defaults to root)
--name    Target filename (optional, defaults to source filename)

#### Example

```bash
aux4 google drive upload ./report.pdf --parent 0AJkGH123 --name "Q1 Report.pdf"
```

```text
{
  "id": "1DxjOWt1YSB6oGNeL8cBkArhmVVrquemct85PhFG3wqn",
  "kind": "drive#file",
  "mimeType": "application/pdf",
  "name": "Q1 Report.pdf"
}
```
