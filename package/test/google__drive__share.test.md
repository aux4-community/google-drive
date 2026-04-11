# google drive share

```timeout
15000
```

```beforeAll
aux4 google drive upload /dev/null --parent 1m0qynhnlInIeB7u0Hs4-I_y-1fBupX2y --name "aux4-drive-share-test" 2>/dev/null | jq -r '.id' > /tmp/aux4-drive-share-test-id.txt
```

```afterAll
aux4 google drive trash $(cat /tmp/aux4-drive-share-test-id.txt) 2>/dev/null || true
rm -f /tmp/aux4-drive-share-test-id.txt
```

## list

### should list permissions for the test file

```execute
aux4 google drive share list $(cat /tmp/aux4-drive-share-test-id.txt)
```

```expect:partial
"permissions"
```
