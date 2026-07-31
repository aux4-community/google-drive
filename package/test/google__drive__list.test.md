# google drive list

These tests run against `mock-drive-api.py`, a local stand-in for the Drive v3
REST API, so they need no OAuth token and no network access. Every request the
mock receives is appended to a log file, which lets the tests assert the exact
URL that was built.

```beforeAll
nohup python3 mock-drive-api.py 18960 requests-18960.log >/dev/null 2>&1 &
sleep 2
```

```afterAll
aux4 curl request --url http://127.0.0.1:18960/__shutdown
rm -f requests-18960.log
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

## with default options

### should return the file list

```execute
aux4 google drive list --tokenFile google-token.json --apiUrl http://127.0.0.1:18960/drive/v3
```

```expect:partial
"nextPageToken": "next-page"
```

### should request the default query, page size and sort order

```execute
jq -c '{method, path, query}' requests-18960.log
```

```expect
{"method":"GET","path":"/drive/v3/files","query":"q=trashed = false&fields=files(id,name,mimeType,modifiedTime,size,webViewLink),nextPageToken&pageSize=20&orderBy=modifiedTime desc"}
```

## with a custom query, page size and sort order

```beforeEach
rm -f requests-18960.log
```

### should percent-encode the query and the sort order

Spaces, `=` and `/` are percent-encoded. A single quote is left as-is because it
is legal in a query string, which is what Drive expects around a value.

```execute
aux4 google drive list --query "mimeType = 'application/vnd.google-apps.spreadsheet'" --pageSize 5 --orderBy name --tokenFile google-token.json --apiUrl http://127.0.0.1:18960/drive/v3 && jq -r '.rawQuery' requests-18960.log
```

```expect:partial
q=mimeType%20%3D%20'application%2Fvnd.google-apps.spreadsheet'&fields=files(id,name,mimeType,modifiedTime,size,webViewLink),nextPageToken&pageSize=5&orderBy=name
```
