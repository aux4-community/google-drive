# google drive search

```beforeAll
nohup python3 mock-drive-api.py 18961 requests-18961.log >/dev/null 2>&1 &
sleep 2
```

```afterAll
aux4 curl request --url http://127.0.0.1:18961/__shutdown
rm -f requests-18961.log
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
rm -f requests-18961.log
```

### should build a name contains query

```execute
aux4 google drive search budget --tokenFile google-token.json --apiUrl http://127.0.0.1:18961/drive/v3 && jq -c '{method, path, query}' requests-18961.log
```

```expect:partial
{"method":"GET","path":"/drive/v3/files","query":"q=name contains 'budget' and trashed = false&fields=files(id,name,mimeType,modifiedTime,webViewLink)&pageSize=10"}
```

### should escape an apostrophe in the name so the Drive query stays valid

```execute
aux4 google drive search "Bob's report" --pageSize 3 --tokenFile google-token.json --apiUrl http://127.0.0.1:18961/drive/v3 && jq -r '.query' requests-18961.log
```

```expect:partial
q=name contains 'Bob\'s report' and trashed = false&fields=files(id,name,mimeType,modifiedTime,webViewLink)&pageSize=3
```
