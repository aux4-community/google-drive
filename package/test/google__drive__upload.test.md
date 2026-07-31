# google drive upload

An upload is two API calls, because `aux4/curl` cannot yet emit the
`multipart/related` body that Drive's single-call upload requires:

1. `POST /upload/drive/v3/files?uploadType=media` sends the raw file bytes with
   the detected content type and a real `Content-Length` (never chunked, which
   Drive rejects).
2. `PATCH /drive/v3/files/<id>` attaches the name, and `addParents` when a
   parent folder was given.

```beforeAll
nohup python3 mock-drive-api.py 18966 requests-18966.log >/dev/null 2>&1 &
sleep 2
```

```afterAll
aux4 curl request --url http://127.0.0.1:18966/__shutdown
rm -f requests-18966.log
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

```file:sample-upload.csv
col1,col2
hello,aux4
```

## with no parent folder

```beforeAll
rm -f requests-18966.log
```

### should name the new file after the source file

```execute
aux4 google drive upload sample-upload.csv --tokenFile google-token.json --apiUrl http://127.0.0.1:18966/drive/v3 --uploadApiUrl http://127.0.0.1:18966/upload/drive/v3
```

```expect:partial
"name": "sample-upload.csv"
```

### should send the file as the raw request body with a real Content-Length

The source file is 20 bytes, and `Content-Length` must say exactly that.
`Transfer-Encoding` must stay empty: Drive rejects a chunked upload.

```execute
wc -c < sample-upload.csv && jq -c 'select(.method == "POST") | {path, query, contentType, contentLength, transferEncoding, body}' requests-18966.log
```

```expect
      20
{"path":"/upload/drive/v3/files","query":"uploadType=media&fields=id,name","contentType":"text/plain","contentLength":"20","transferEncoding":"","body":"col1,col2\nhello,aux4"}
```

### should follow up with a PATCH that sets the name

```execute
jq -c 'select(.method == "PATCH") | {path, query, body}' requests-18966.log
```

```expect
{"path":"/drive/v3/files/mock-file-id","query":"fields=id,name,mimeType,parents,webViewLink","body":"{\"name\":\"sample-upload.csv\"}"}
```

## with a parent folder and a custom name

```beforeEach
rm -f requests-18966.log
```

### should attach the parent and the name in the follow-up PATCH

```execute
aux4 google drive upload sample-upload.csv --parent FOLDER9 --name "Renamed.csv" --tokenFile google-token.json --apiUrl http://127.0.0.1:18966/drive/v3 --uploadApiUrl http://127.0.0.1:18966/upload/drive/v3 && jq -c 'select(.method == "PATCH") | {path, query, body}' requests-18966.log
```

```expect:partial
{"path":"/drive/v3/files/mock-file-id","query":"addParents=FOLDER9&fields=id,name,mimeType,parents,webViewLink","body":"{\"name\":\"Renamed.csv\"}"}
```

## with an explicit content type

```beforeEach
rm -f requests-18966.log
```

### should send the given mime type instead of the detected one

```execute
aux4 google drive upload sample-upload.csv --mimeType text/csv --tokenFile google-token.json --apiUrl http://127.0.0.1:18966/drive/v3 --uploadApiUrl http://127.0.0.1:18966/upload/drive/v3 && jq -r 'select(.method == "POST") | .contentType' requests-18966.log
```

```expect:partial
text/csv
```

## with a source file that does not exist

### should fail before contacting Drive

```execute
aux4 google drive upload no-such-file.csv --tokenFile google-token.json --apiUrl http://127.0.0.1:18966/drive/v3 --uploadApiUrl http://127.0.0.1:18966/upload/drive/v3
```

```error:partial
no-such-file.csv: No such file or directory
```
