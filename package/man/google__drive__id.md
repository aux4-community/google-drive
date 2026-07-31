#### Description

The `id` command returns the file ID for a given name or path. It prints only the
raw ID as plain text, which makes it easy to substitute into another command.

- **By name**: `aux4 google drive id "Q1 Budget"` — one exact-name search across
  the whole Drive (`name = 'Q1 Budget' and trashed = false`). The first match wins.
- **By path**: `aux4 google drive id "reports/Q1 Budget"` — the path is walked one
  segment at a time starting at the Drive root. Every segment except the last
  must be a folder, and each segment must be a direct child of the previous one.

An apostrophe in any segment is escaped for the Drive query language.

If a segment cannot be resolved, the command writes `not found: <segment>` to
stderr and exits 1, so the failing segment of a long path is named directly.

#### Usage

```bash
aux4 google drive id <name> [--tokenFile <path>]
```

name         File name, or path using `/` as the separator (positional argument)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

By name:

```bash
aux4 google drive id "Q1 Budget"
```

```text
1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```

By path:

```bash
aux4 google drive id "reports/2026/Q1 Budget"
```

```text
1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```

When a segment does not exist:

```bash
aux4 google drive id "reports/nope"
```

```text
not found: nope
```

Combined with google sheets:

```bash
aux4 google sheets values get --spreadsheetId $(aux4 google drive id "reports/Q1 Budget") --range 'Sheet1!A1:C10'
```
