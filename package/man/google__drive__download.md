#### Description

The `download` command downloads the content of a file from Google Drive to a local path. This works for binary files (PDFs, images, etc.). For Google Workspace documents (Docs, Sheets, Slides), use `aux4 google drive export` instead, which converts them to a downloadable format.

#### Usage

```bash
aux4 google drive download <fileId> <output>
```

fileId  The file ID to download (positional argument)
output  Local file path to save to (positional argument)

#### Example

```bash
aux4 google drive download 1DxjOWt1YSB6oGNeL8cBkArhmVVrquemct85PhFG3wqn ./report.pdf
```
