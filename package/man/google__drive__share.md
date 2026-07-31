#### Description

The `share` command group manages the sharing permissions of files and folders in
Google Drive.

Available subcommands:

- **add** — Share a file with a user, group, domain or anyone
- **list** — List the sharing permissions of a file
- **remove** — Remove a sharing permission

All three need a read-write login: `aux4 google auth login --services drive`
without `--readonly true`.

#### Usage

```bash
aux4 google drive share <subcommand>
```

#### Example

```bash
aux4 google drive share add FILE_ID --email alice@example.com --role writer
aux4 google drive share list FILE_ID
```
