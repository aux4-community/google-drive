# google drive export

```timeout
15000
```

```beforeAll
aux4 google sheets create "aux4-drive-export-test" --folderId 1m0qynhnlInIeB7u0Hs4-I_y-1fBupX2y 2>/dev/null | jq -r '.id' > /tmp/aux4-drive-export-test-id.txt
```

```afterAll
aux4 google drive trash $(cat /tmp/aux4-drive-export-test-id.txt) 2>/dev/null || true
rm -f /tmp/aux4-drive-export-test-id.txt
rm -f test-export.csv
```

## export spreadsheet as CSV

### should export the test spreadsheet

```execute
aux4 google drive export --fileId $(cat /tmp/aux4-drive-export-test-id.txt) --output test-export.csv --mimeType text/csv
```

```expect:partial
"status": "success"
```
