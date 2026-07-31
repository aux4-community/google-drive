# google-drive test suite

The `core` group is CI safe: it runs against `mock-drive-api.py`, a local
stand-in for the Drive v3 REST API, so it needs no OAuth token and no network.

The `integration` group talks to the real Drive API and is skipped unless you
ask for it with `aux4 test run --group integration`.

Groups are only honoured when `aux4 test run` is executed from this directory.

## core

- google__drive__services.test.md
- google__drive__list.test.md
- google__drive__search.test.md
- google__drive__id.test.md
- google__drive__get.test.md
- google__drive__file-ops.test.md
- google__drive__mkdir.test.md
- google__drive__upload.test.md
- google__drive__download.test.md
- google__drive__export.test.md
- google__drive__share.test.md
- google__drive__injection.test.md

## integration (optional)

- google__drive__live.test.md
