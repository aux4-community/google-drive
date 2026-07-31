# google drive file operations

Covers `copy`, `rename`, `move`, `trash`, `restore` and `delete` against the
local Drive API stand-in.

```beforeAll
nohup python3 mock-drive-api.py 18964 requests-18964.log >/dev/null 2>&1 &
sleep 2
```

```afterAll
aux4 curl request --url http://127.0.0.1:18964/__shutdown
rm -f requests-18964.log
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

## copy

```beforeEach
rm -f requests-18964.log
```

### should post the new name to the copy endpoint

```execute
aux4 google drive copy FILE123 --name "Q1 Budget Copy" --tokenFile google-token.json --apiUrl http://127.0.0.1:18964/drive/v3 && jq -c '{method, path, contentType, body}' requests-18964.log
```

```expect:partial
{"method":"POST","path":"/drive/v3/files/FILE123/copy","contentType":"application/json","body":"{\"name\":\"Q1 Budget Copy\"}"}
```

## rename

```beforeEach
rm -f requests-18964.log
```

### should patch the new name onto the file

```execute
aux4 google drive rename FILE123 --name "Q1 Budget Final" --tokenFile google-token.json --apiUrl http://127.0.0.1:18964/drive/v3 && jq -c '{method, path, body}' requests-18964.log
```

```expect:partial
{"method":"PATCH","path":"/drive/v3/files/FILE123","body":"{\"name\":\"Q1 Budget Final\"}"}
```

## move

```beforeEach
rm -f requests-18964.log
```

### should send addParents only when no source folder is given

```execute
aux4 google drive move FILE123 --folderId DEST9 --tokenFile google-token.json --apiUrl http://127.0.0.1:18964/drive/v3 && jq -c '{method, path, query, body}' requests-18964.log
```

```expect:partial
{"method":"PATCH","path":"/drive/v3/files/FILE123","query":"addParents=DEST9","body":""}
```

### should send addParents and removeParents when a source folder is given

```execute
aux4 google drive move FILE123 --folderId DEST9 --fromFolderId SRC7 --tokenFile google-token.json --apiUrl http://127.0.0.1:18964/drive/v3 && jq -r '.query' requests-18964.log
```

```expect:partial
addParents=DEST9&removeParents=SRC7
```

## trash and restore

```beforeAll
rm -f requests-18964.log
```

### should patch trashed true

```execute
aux4 google drive trash FILE123 --tokenFile google-token.json --apiUrl http://127.0.0.1:18964/drive/v3
```

```expect:partial
"trashed": true
```

### should patch trashed false

```execute
aux4 google drive restore FILE123 --tokenFile google-token.json --apiUrl http://127.0.0.1:18964/drive/v3
```

```expect:partial
"trashed": false
```

### should ask for the trashed field on both calls

```execute
jq -c '{method, path, query, body}' requests-18964.log
```

```expect
{"method":"PATCH","path":"/drive/v3/files/FILE123","query":"fields=id,name,mimeType,trashed","body":"{\"trashed\": true}"}
{"method":"PATCH","path":"/drive/v3/files/FILE123","query":"fields=id,name,mimeType,trashed","body":"{\"trashed\": false}"}
```

## delete

```beforeEach
rm -f requests-18964.log
```

### should confirm, send a DELETE and report what was removed

```execute
aux4 google drive delete FILE123 --yes --tokenFile google-token.json --apiUrl http://127.0.0.1:18964/drive/v3 && jq -c '{method, path}' requests-18964.log
```

```expect
Permanently deleted FILE123
{"method":"DELETE","path":"/drive/v3/files/FILE123"}
```
