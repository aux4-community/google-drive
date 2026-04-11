#### Description

The `remove` command removes a sharing permission from a file. You need the `permissionId`, which you can find by running `aux4 google drive share list`.

#### Usage

```bash
aux4 google drive share remove <fileId> <permissionId>
```

fileId        The file ID (positional argument)
permissionId  The permission ID to remove (positional argument)

#### Example

```bash
aux4 google drive share remove 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms 09876543210987654321
```
