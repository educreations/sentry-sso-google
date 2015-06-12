# sentry-sso-google

Google SSO support for Sentry 7.5 and above.

## Usage

The following settings are required to be in your Sentry configuration. You can create a new project in the [Developers Console][dev-console]. From there, go to APIs & Auth, Credentials and get the credentials for a web application.

- `GOOGLE_OAUTH2_CLIENT_ID`
- `GOOGLE_OAUTH2_CLIENT_SECRET`

You can limit who can sign into Sentry using this provider by setting the `GOOGLE_WHITE_LISTED_DOMAINS` to a list of allowed domains. For example, to limit to `educreations.com` users, one could do:

```python
GOOGLE_WHITE_LISTED_DOMAINS = ['educreations.com']
```

## Copyright

Copyright © 2015, Educreations, Inc under the MIT software license. See LICENSE for more information.


[dev-console]: https://console.developers.google.com
