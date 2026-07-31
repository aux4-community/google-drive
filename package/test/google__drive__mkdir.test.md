# google drive mkdir

```beforeAll
nohup python3 mock-drive-api.py 18965 requests-18965.log >/dev/null 2>&1 &
sleep 2
```

```afterAll
aux4 curl request --url http://127.0.0.1:18965/__shutdown
rm -f requests-18965.log
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

## in the Drive root

```beforeAll
rm -f requests-18965.log
```

### should create a folder with root as the parent

```execute
aux4 google drive mkdir "Project Files" --tokenFile google-token.json --apiUrl http://127.0.0.1:18965/drive/v3
```

```expect:partial
"mimeType": "application/vnd.google-apps.folder"
```

### should post the folder mime type and the parent array

```execute
jq -c '{method, path, contentType, body}' requests-18965.log
```

```expect
{"method":"POST","path":"/drive/v3/files","contentType":"application/json","body":"{\"name\":\"Project Files\",\"mimeType\":\"application/vnd.google-apps.folder\",\"parents\":[\"root\"]}"}
```

## inside another folder

```beforeEach
rm -f requests-18965.log
```

### should use the given parent folder ID

```execute
aux4 google drive mkdir Reports --parent PARENT1 --tokenFile google-token.json --apiUrl http://127.0.0.1:18965/drive/v3 && jq -r '.body' requests-18965.log
```

```expect:partial
{"name":"Reports","mimeType":"application/vnd.google-apps.folder","parents":["PARENT1"]}
```
