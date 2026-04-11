#!/bin/bash
# Resolves a Google Drive name or path to a file ID.
# Single name: searches globally by exact name.
# Path with /: walks each segment from root, querying by name + parent.

path="$1"

# Single name (no /): global search
if [[ "$path" != */* ]]; then
  result=$(gws drive files list --params "{\"q\": \"name = '$path' and trashed = false\", \"fields\": \"files(id)\", \"pageSize\": 1}" 2>/dev/null)
  id=$(echo "$result" | jq -r '.files[0].id')
  if [ "$id" = "null" ] || [ -z "$id" ]; then
    echo "not found: $path" >&2
    exit 1
  fi
  echo "$id"
  exit 0
fi

# Path: walk segments from root
parent="root"
IFS='/' read -ra segments <<< "$path"
last_index=$(( ${#segments[@]} - 1 ))

for i in "${!segments[@]}"; do
  segment="${segments[$i]}"
  [ -z "$segment" ] && continue

  if [ "$i" -lt "$last_index" ]; then
    result=$(gws drive files list --params "{\"q\": \"name = '$segment' and '$parent' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false\", \"fields\": \"files(id)\", \"pageSize\": 1}" 2>/dev/null)
  else
    result=$(gws drive files list --params "{\"q\": \"name = '$segment' and '$parent' in parents and trashed = false\", \"fields\": \"files(id)\", \"pageSize\": 1}" 2>/dev/null)
  fi

  parent=$(echo "$result" | jq -r '.files[0].id')
  if [ "$parent" = "null" ] || [ -z "$parent" ]; then
    echo "not found: $segment" >&2
    exit 1
  fi
done

echo "$parent"
