# google drive id

The mock answers a file search with an id derived from the name the query asked
for (`report` becomes `id-report`), so a multi-segment path walk can be checked
segment by segment. The reserved name `missing` answers with no match.

```beforeAll
nohup python3 mock-drive-api.py 18962 requests-18962.log >/dev/null 2>&1 &
sleep 2
```

```afterAll
aux4 curl request --url http://127.0.0.1:18962/__shutdown
rm -f requests-18962.log
```

```file:google-token.json
{
  "clientId": "mock-client",
  "clientSecret": "mock-secret",
  "authUrl": "https://accounts.google.com/o/oauth2/v2/auth",
  "tokenUrl": "https://oauth2.googleapis.com/token",
  "scopes": "https://www.googleapis.com/auth/drive openid email",
  "accessToken": "mock-access-token",
  "refreshToken": "mock-refresh-token",
  "expiresAt": "2099-12-31T23:59:59Z"
}
```

## by name

```beforeEach
rm -f requests-18962.log
```

### should return the file ID

```execute
aux4 google drive id report --tokenFile google-token.json --apiUrl http://127.0.0.1:18962/drive/v3
```

```expect
id-report
```

### should search the whole Drive, with no parent restriction

```execute
aux4 google drive id report --tokenFile google-token.json --apiUrl http://127.0.0.1:18962/drive/v3 && jq -r '.query' requests-18962.log
```

```expect:partial
q=name = 'report' and trashed = false&fields=files(id)&pageSize=1
```

## by path

```beforeEach
rm -f requests-18962.log
```

### should resolve the last segment of the path

```execute
aux4 google drive id reports/2026/summary --tokenFile google-token.json --apiUrl http://127.0.0.1:18962/drive/v3
```

```expect
id-summary
```

### should walk one segment at a time, requiring a folder for every segment but the last

```execute
aux4 google drive id reports/2026/summary --tokenFile google-token.json --apiUrl http://127.0.0.1:18962/drive/v3 && jq -r '.query' requests-18962.log
```

```expect
id-summary
q=name = 'reports' and 'root' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false&fields=files(id)&pageSize=1
q=name = '2026' and 'id-reports' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false&fields=files(id)&pageSize=1
q=name = 'summary' and 'id-2026' in parents and trashed = false&fields=files(id)&pageSize=1
```

## with a name that does not exist

### should fail with not found

```execute
aux4 google drive id missing --tokenFile google-token.json --apiUrl http://127.0.0.1:18962/drive/v3
```

```error:partial
not found: missing
```

## with a path that does not exist

### should name the segment that could not be resolved

```execute
aux4 google drive id reports/missing --tokenFile google-token.json --apiUrl http://127.0.0.1:18962/drive/v3
```

```error:partial
not found: missing
```
