# google drive get

```timeout
15000
```

```beforeAll
aux4 google drive upload /dev/null --parent 1m0qynhnlInIeB7u0Hs4-I_y-1fBupX2y --name "aux4-drive-get-test" 2>/dev/null | jq -r '.id' > /tmp/aux4-drive-get-test-id.txt
```

```afterAll
aux4 google drive trash $(cat /tmp/aux4-drive-get-test-id.txt) 2>/dev/null || true
rm -f /tmp/aux4-drive-get-test-id.txt
```

## with a valid file ID

### should return file metadata

```execute
aux4 google drive get $(cat /tmp/aux4-drive-get-test-id.txt)
```

```expect:partial
"name": "aux4-drive-get-test"
```
