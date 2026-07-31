# google drive share

```beforeAll
nohup python3 mock-drive-api.py 18969 requests-18969.log >/dev/null 2>&1 &
sleep 2
```

```afterAll
aux4 curl request --url http://127.0.0.1:18969/__shutdown
rm -f requests-18969.log
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

## add

```beforeEach
rm -f requests-18969.log
```

### should post the role, type and email address

```execute
aux4 google drive share add FILE123 --email alice@example.com --role writer --tokenFile google-token.json --apiUrl http://127.0.0.1:18969/drive/v3 && jq -c '{method, path, body}' requests-18969.log
```

```expect:partial
{"method":"POST","path":"/drive/v3/files/FILE123/permissions","body":"{\"emailAddress\":\"alice@example.com\",\"role\":\"writer\",\"type\":\"user\"}"}
```

## list

```beforeAll
rm -f requests-18969.log
```

### should return the permissions of the file

```execute
aux4 google drive share list FILE123 --tokenFile google-token.json --apiUrl http://127.0.0.1:18969/drive/v3
```

```expect:partial
"permissions"
```

### should ask for the documented permission fields

```execute
jq -c '{method, path, query}' requests-18969.log
```

```expect
{"method":"GET","path":"/drive/v3/files/FILE123/permissions","query":"fields=permissions(id,role,type,emailAddress,displayName)"}
```

## remove

```beforeEach
rm -f requests-18969.log
```

### should delete the permission and report it

```execute
aux4 google drive share remove FILE123 --permissionId perm-1 --tokenFile google-token.json --apiUrl http://127.0.0.1:18969/drive/v3 && jq -c '{method, path}' requests-18969.log
```

```expect
Removed permission perm-1 from FILE123
{"method":"DELETE","path":"/drive/v3/files/FILE123/permissions/perm-1"}
```
