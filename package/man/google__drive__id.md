#### Description

The `id` command returns the file ID for a given name or path. It returns only the raw ID as plain text (no JSON), making it easy to pipe into other commands.

- **By name**: `aux4 google drive id "Q1 Budget"` — searches for an exact name match across all non-trashed files. Returns the first match.
- **By path**: `aux4 google drive id "reports/Q1 Budget"` — walks each folder segment from root and returns the ID of the final file.

If the file is not found, the command exits with an error.

#### Usage

```bash
aux4 google drive id <name>
```

name  File name or path using `/` as separator (positional argument)

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
aux4 google drive id "reports/Q1 Budget"
```

```text
1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```

Combined with google sheets:

```bash
aux4 google sheets values get --spreadsheetId $(aux4 google drive id "test/test") --range 'Sheet1!A1:C10'
```
