# google drive get

```beforeAll
nohup python3 mock-drive-api.py 18963 requests-18963.log >/dev/null 2>&1 &
sleep 2
```

```afterAll
aux4 curl request --url http://127.0.0.1:18963/__shutdown
rm -f requests-18963.log
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

## with a valid file ID

### should return the file metadata

```execute
aux4 google drive get FILE123 --tokenFile google-token.json --apiUrl http://127.0.0.1:18963/drive/v3
```

```expect:partial
"id": "FILE123"
```

### should ask for the documented field set

```execute
jq -c '{method, path, query}' requests-18963.log
```

```expect
{"method":"GET","path":"/drive/v3/files/FILE123","query":"fields=id,name,mimeType,modifiedTime,size,webViewLink,parents,shared,owners"}
```

## without a stored token

### should report that the provider has no token

```execute
aux4 google drive get FILE123 --tokenFile ./no-such-directory/google.json --apiUrl http://127.0.0.1:18963/drive/v3
```

```error:partial
no token found for provider "google"
```
