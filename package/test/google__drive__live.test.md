# google drive against the real Drive API

These tests talk to Google. They are in the optional `integration` group, so
`aux4 test run` skips them unless you ask for them:

```bash
aux4 test run --group integration
```

They need a real login (`aux4 google auth login --services drive`) and a
writable folder in your Drive. Set `AUX4_DRIVE_TEST_FOLDER` to that folder's ID
before running; everything is created inside it and trashed afterwards.

```timeout
30000
```

```file:aux4-drive-live.csv
col1,col2
hello,aux4
```

## round trip

```afterAll
ID=$(aux4 google drive search aux4-drive-live.csv | jq -r '.files[0].id // empty') && aux4 google drive trash "$ID"
rm -f aux4-drive-live-download.csv
```

### should upload the file into the test folder under its source name

```execute
aux4 google drive upload aux4-drive-live.csv --parent $AUX4_DRIVE_TEST_FOLDER
```

```expect:partial
"name": "aux4-drive-live.csv"
```

### should resolve the uploaded name back to an ID

```execute
aux4 google drive id aux4-drive-live.csv
```

```expect:regex
^[a-zA-Z0-9_-]+$
```

### should read the metadata back, including the parent folder

```execute
aux4 google drive get $(aux4 google drive id aux4-drive-live.csv)
```

```expect:partial
"name": "aux4-drive-live.csv"
```

### should download the content to an absolute path outside the working directory

```execute
aux4 google drive download $(aux4 google drive id aux4-drive-live.csv) --output /tmp/aux4-drive-live-download.csv && cat /tmp/aux4-drive-live-download.csv
```

```expect:partial
hello,aux4
```

### should list the sharing permissions

```execute
aux4 google drive share list $(aux4 google drive id aux4-drive-live.csv)
```

```expect:partial
"permissions"
```

## folders

```afterAll
ID=$(aux4 google drive search aux4-drive-live-folder | jq -r '.files[0].id // empty') && aux4 google drive trash "$ID"
```

### should create a folder inside the test folder

```execute
aux4 google drive mkdir aux4-drive-live-folder --parent $AUX4_DRIVE_TEST_FOLDER
```

```expect:partial
"mimeType": "application/vnd.google-apps.folder"
```

## listing and searching

### should list files

```execute
aux4 google drive list --pageSize 5
```

```expect:partial
"files"
```

### should search by name

```execute
aux4 google drive search aux4-drive-live
```

```expect:partial
"files"
```
