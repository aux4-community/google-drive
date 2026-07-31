# google drive download

```beforeAll
nohup python3 mock-drive-api.py 18967 requests-18967.log >/dev/null 2>&1 &
sleep 2
```

```afterAll
aux4 curl request --url http://127.0.0.1:18967/__shutdown
rm -f requests-18967.log
rm -f /tmp/aux4-google-drive-outside-cwd.csv
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

## into the current directory

```afterEach
rm -f downloaded.csv
```

### should write the response body to the output path

```execute
aux4 google drive download FILE123 --output downloaded.csv --tokenFile google-token.json --apiUrl http://127.0.0.1:18967/drive/v3 && cat downloaded.csv
```

```expect
Saved downloaded.csv
drive,mock,payload
1,2,3
```

### should request the content with alt=media

```execute
aux4 google drive download FILE123 --output downloaded.csv --tokenFile google-token.json --apiUrl http://127.0.0.1:18967/drive/v3 && jq -r --slurp '.[-1] | .method + " " + .path + " " + .query' requests-18967.log
```

```expect:partial
GET /drive/v3/files/FILE123 alt=media
```

## into an absolute path outside the current directory

The previous implementation could not do this at all: the CLI it wrapped refused
any output path outside the working directory.

### should write the file where it was asked to

```execute
aux4 google drive download FILE123 --output /tmp/aux4-google-drive-outside-cwd.csv --tokenFile google-token.json --apiUrl http://127.0.0.1:18967/drive/v3 && wc -c < /tmp/aux4-google-drive-outside-cwd.csv && cat /tmp/aux4-google-drive-outside-cwd.csv
```

```expect
Saved /tmp/aux4-google-drive-outside-cwd.csv
      25
drive,mock,payload
1,2,3
```

## when the file does not exist

### should report the error and leave no file behind

```execute
aux4 google drive download missing --output should-not-exist.csv --tokenFile google-token.json --apiUrl http://127.0.0.1:18967/drive/v3
```

```error:partial
Error: HTTP 404
```

### should not have created the output file

```execute
ls should-not-exist.csv
```

```error:partial
should-not-exist.csv
```
