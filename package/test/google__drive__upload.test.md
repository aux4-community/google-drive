# google drive upload

```timeout
15000
```

```file:test-upload.txt
hello from aux4
```

```afterAll
ID=$(aux4 google drive search "test-upload.txt" 2>/dev/null | jq -r '.files[0].id') && [ "$ID" != "null" ] && aux4 google drive trash $ID 2>/dev/null || true
```

## upload a file

### should upload to the test folder

```execute
aux4 google drive upload test-upload.txt --parent 1m0qynhnlInIeB7u0Hs4-I_y-1fBupX2y
```

```expect:partial
"name": "test-upload.txt"
```
