#### Description

The `delete` command permanently deletes a file from Google Drive. This action is irreversible — the file is not moved to trash. A confirmation prompt is shown before proceeding.

To move a file to trash instead (reversible), use `aux4 google drive trash`.

#### Usage

```bash
aux4 google drive delete <fileId>
```

fileId  The file ID to permanently delete (positional argument)

#### Example

```bash
aux4 google drive delete 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```

```text
Are you sure you want to permanently delete this file? (y/n)
```
