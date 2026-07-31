#### Description

The `add` command shares a file with a user, group, domain, or anyone with the
link. The default role is `reader` (view only). Available roles:

- **reader** — can view
- **commenter** — can view and comment
- **writer** — can edit
- **organizer** — can manage (shared drives only)

The `--type` flag specifies the target type:

- **user** (default) — a specific Google account
- **group** — a Google Group
- **domain** — everyone in a domain
- **anyone** — anyone with the link

`--email` is the address of the user or group. It is ignored by Drive for
`--type anyone`.

#### Usage

```bash
aux4 google drive share add <fileId> --email <email> [--role <role>] [--type <type>] [--tokenFile <path>]
```

fileId       The file ID to share (positional argument)
--email      Email address to share with
--role       Permission role (default: `reader`)
--type       Permission type (default: `user`)
--tokenFile  Where the OAuth token is stored (default: `~/.aux4.config/.oauth/google.json`)

#### Example

```bash
aux4 google drive share add 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms --email alice@example.com --role writer
```

```text
{
  "id": "12345678901234567890",
  "kind": "drive#permission",
  "role": "writer",
  "type": "user",
  "emailAddress": "alice@example.com"
}
```
