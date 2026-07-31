#### Description

The `delete` command permanently deletes a file from Google Drive. This is
irreversible: the file is not moved to trash. A confirmation prompt is shown
first, which `--yes` skips.

To move a file to trash instead, which is reversible, use
`aux4 google drive trash`.

The Drive API answers a delete with an empty body, so the command prints its own
confirmation line once the request succeeds.

#### Usage

```bash
aux4 google drive delete <fileId> [--tokenFile <path>]
```

fileId       The file ID to permanently delete (positional argument)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive delete 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms --yes
```

```text
Permanently deleted 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```
