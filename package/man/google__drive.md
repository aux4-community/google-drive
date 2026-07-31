#### Description

The `google drive` command group manages files and folders through the Google
Drive v3 REST API. Requests are sent over `aux4/curl`'s OAuth2 transport using
the token that `aux4 google auth login` stored, so this package needs no
credential setup of its own.

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

Every subcommand accepts `--tokenFile` (environment variable
`AUX4_GOOGLE_TOKEN_FILE`, default `~/.aux4.config/.oauth/google.json`), so a
second Google account can be used without logging out of the first.

#### Usage

```bash
aux4 google drive <subcommand>
```

#### Example

```bash
aux4 google auth login --services drive
aux4 google drive search "budget"
aux4 google drive upload ./report.pdf
```
