#### Description

The `remove` command removes a sharing permission from a file. Find the permission
ID with `aux4 google drive share list`.

The Drive API answers with an empty body, so the command prints its own
confirmation line once the request succeeds.

#### Usage

```bash
aux4 google drive share remove <fileId> --permissionId <id> [--tokenFile <path>]
```

fileId          The file ID (positional argument)
--permissionId  The permission ID to remove
--tokenFile     Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive share remove 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms --permissionId 09876543210987654321
```

```text
Removed permission 09876543210987654321 from 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```
