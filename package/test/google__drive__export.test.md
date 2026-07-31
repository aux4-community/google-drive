# google drive export

```beforeAll
nohup python3 mock-drive-api.py 18968 requests-18968.log >/dev/null 2>&1 &
sleep 2
```

```afterAll
aux4 curl request --url http://127.0.0.1:18968/__shutdown
rm -f requests-18968.log
rm -f /tmp/aux4-google-drive-export.csv
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

## as CSV

```afterEach
rm -f exported.csv
```

### should write the exported bytes to the output file

```execute
aux4 google drive export FILE123 --output exported.csv --mimeType text/csv --tokenFile google-token.json --apiUrl http://127.0.0.1:18968/drive/v3 && wc -c < exported.csv && cat exported.csv
```

```expect
Saved exported.csv
      25
drive,mock,payload
1,2,3
```

### should call the export endpoint with the requested mime type

```execute
aux4 google drive export FILE123 --output exported.csv --mimeType text/csv --tokenFile google-token.json --apiUrl http://127.0.0.1:18968/drive/v3 && jq -r --slurp '.[-1] | .method + " " + .path + " " + .query' requests-18968.log
```

```expect:partial
GET /drive/v3/files/FILE123/export mimeType=text/csv
```

## as PDF into an absolute path outside the current directory

### should percent-encode the mime type and write the file

```execute
aux4 google drive export FILE123 --output /tmp/aux4-google-drive-export.csv --mimeType application/pdf --tokenFile google-token.json --apiUrl http://127.0.0.1:18968/drive/v3 && jq -r --slurp '.[-1].rawQuery' requests-18968.log && wc -c < /tmp/aux4-google-drive-export.csv
```

```expect
Saved /tmp/aux4-google-drive-export.csv
mimeType=application%2Fpdf
      25
```
