# google drive services

`community/google-auth` discovers the scopes it must request by calling the
private `services` command of every installed Google package. Publishing
`readonlyScope` next to `scope` is what makes `aux4 google auth login --readonly
true` request read-only access instead of full read-write.

## service metadata

### should declare the drive scope and its read-only counterpart

```execute
aux4 google drive services
```

```expect:json
{
  "name": "drive",
  "scope": "https://www.googleapis.com/auth/drive",
  "readonlyScope": "https://www.googleapis.com/auth/drive.readonly",
  "description": "Manage files, folders, and shared drives"
}
```
