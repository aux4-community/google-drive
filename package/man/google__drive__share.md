#### Description

The `share` command group manages sharing permissions for files and folders in Google Drive.

Available subcommands:

- **add** — Share a file with a user or group
- **list** — List sharing permissions for a file
- **remove** — Remove a sharing permission

#### Usage

```bash
aux4 google drive share <subcommand>
```

#### Example

```bash
aux4 google drive share add FILE_ID alice@example.com --role writer
aux4 google drive share list FILE_ID
```
