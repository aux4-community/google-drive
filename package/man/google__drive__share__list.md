#### Description

The `list` command shows all sharing permissions of a file, including the
permission ID, role, type, email address and display name of each entry. The
permission ID is what `aux4 google drive share remove` needs.

#### Usage

```bash
aux4 google drive share list <fileId> [--tokenFile <path>]
```

fileId       The file ID (positional argument)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive share list 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
```

```text
{
  "permissions": [
    {
      "id": "12345678901234567890",
      "role": "owner",
      "type": "user",
      "emailAddress": "owner@example.com",
      "displayName": "Owner"
    },
    {
      "id": "09876543210987654321",
      "role": "writer",
      "type": "user",
      "emailAddress": "alice@example.com",
      "displayName": "Alice"
    }
  ]
}
```
