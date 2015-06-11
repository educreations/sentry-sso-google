from __future__ import absolute_import

from sentry.auth import manager

from .provider import GoogleOAuth2Provider

manager.register(GoogleOAuth2Provider.name, GoogleOAuth2Provider)
