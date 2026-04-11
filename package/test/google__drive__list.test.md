# google drive list

```timeout
15000
```

## with default options

### should list recent files

```execute
aux4 google drive list
```

```expect:partial
"files"
```

## with a custom query

### should filter by mime type

```execute
aux4 google drive list --query "mimeType = 'application/vnd.google-apps.spreadsheet' and trashed = false" --pageSize 5
```

```expect:partial
"mimeType"
```
