# google drive mkdir

```timeout
15000
```

```afterAll
ID=$(aux4 google drive search "aux4-drive-mkdir-test" 2>/dev/null | jq -r '.files[0].id') && [ "$ID" != "null" ] && aux4 google drive trash $ID 2>/dev/null || true
```

## create a folder

### should create a folder in the test directory

```execute
aux4 google drive mkdir "aux4-drive-mkdir-test" --parent 1m0qynhnlInIeB7u0Hs4-I_y-1fBupX2y
```

```expect:partial
"mimeType": "application/vnd.google-apps.folder"
```
