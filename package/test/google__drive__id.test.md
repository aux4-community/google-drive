# google drive id

```timeout
15000
```

```beforeAll
aux4 google sheets create "aux4-drive-id-test" --folderId 1m0qynhnlInIeB7u0Hs4-I_y-1fBupX2y 2>/dev/null | jq -r '.id' > /tmp/aux4-drive-id-test-id.txt
```

```afterAll
aux4 google drive trash $(cat /tmp/aux4-drive-id-test-id.txt) 2>/dev/null || true
rm -f /tmp/aux4-drive-id-test-id.txt
```

## by name

### should return the file ID

```execute
aux4 google drive id "aux4-drive-id-test"
```

```expect:regex
^[a-zA-Z0-9_-]+$
```

## by path

### should resolve a full path to the file ID

```execute
EXPECTED=$(cat /tmp/aux4-drive-id-test-id.txt) && ACTUAL=$(aux4 google drive id "test/aux4-drive-id-test") && [ "$ACTUAL" = "$EXPECTED" ] && echo "match" || echo "mismatch: expected $EXPECTED got $ACTUAL"
```

```expect
match
```

## with invalid path

### should fail with not found

```execute
aux4 google drive id "nonexistent/file" 2>&1 || true
```

```expect:partial
not found
```
