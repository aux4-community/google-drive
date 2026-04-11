# google drive file operations

```timeout
30000
```

```beforeAll
aux4 google drive upload /dev/null --parent 1m0qynhnlInIeB7u0Hs4-I_y-1fBupX2y --name "aux4-drive-file-ops-test" 2>/dev/null | jq -r '.id' > /tmp/aux4-drive-file-ops-test-id.txt
```

```afterAll
ID=$(aux4 google drive search "test-renamed-ops" 2>/dev/null | jq -r '.files[0].id') && [ "$ID" != "null" ] && aux4 google drive trash $ID 2>/dev/null || true
aux4 google drive trash $(cat /tmp/aux4-drive-file-ops-test-id.txt) 2>/dev/null || true
rm -f /tmp/aux4-drive-file-ops-test-id.txt
```

## copy

### should copy the test file

```execute
aux4 google drive copy $(cat /tmp/aux4-drive-file-ops-test-id.txt) --name "test-copy-ops"
```

```expect:partial
"name": "test-copy-ops"
```

## rename

### should rename the copied file

```execute
COPY_ID=$(aux4 google drive search "test-copy-ops" 2>/dev/null | jq -r '.files[0].id') && aux4 google drive rename --fileId $COPY_ID --name "test-renamed-ops"
```

```expect:partial
"name": "test-renamed-ops"
```

## trash

### should trash the renamed file

```execute
FILE_ID=$(aux4 google drive search "test-renamed-ops" 2>/dev/null | jq -r '.files[0].id') && aux4 google drive trash --fileId $FILE_ID
```

```expect:partial
"trashed": true
```

## restore

### should restore the trashed file

```execute
FILE_ID=$(aux4 google drive list --query "name = 'test-renamed-ops' and trashed = true" 2>/dev/null | jq -r '.files[0].id') && aux4 google drive restore --fileId $FILE_ID
```

```expect:partial
"trashed": false
```
