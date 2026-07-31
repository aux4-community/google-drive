# google drive command injection

Regression test for command injection through user-supplied arguments. A file
ID that carries shell metacharacters must be shell-escaped when the command
builds the request URL, so it can never break out and run an arbitrary command.

The request targets a dead port, so no real network call succeeds — the test
only cares that the injected `touch` never runs.

```beforeAll
rm -f /tmp/AUX4_INJ_drive
```

```afterAll
rm -f /tmp/AUX4_INJ_drive
```

```file:google-token.json
{
  "clientId": "mock-client",
  "clientSecret": "mock-secret",
  "authUrl": "https://accounts.google.com/o/oauth2/v2/auth",
  "tokenUrl": "https://oauth2.googleapis.com/token",
  "scopes": "https://www.googleapis.com/auth/drive openid email",
  "accessToken": "mock-access-token",
  "refreshToken": "mock-refresh-token",
  "expiresAt": "2099-12-31T23:59:59Z"
}
```

## with a quote-bearing file ID

### should not execute an injected command

```execute
aux4 google drive get "x'; touch /tmp/AUX4_INJ_drive; echo '" --apiUrl http://127.0.0.1:1 --tokenFile google-token.json </dev/null; test -f /tmp/AUX4_INJ_drive && echo VULNERABLE || echo SAFE
```

```expect:partial
SAFE
```
