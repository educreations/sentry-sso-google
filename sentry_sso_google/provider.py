from __future__ import absolute_import

from django.conf import settings
import requests
from sentry.auth import AuthView
from sentry.auth.providers.oauth2 import (
    OAuth2Callback,
    OAuth2Login,
    OAuth2Provider,
)


class FetchProfileView(AuthView):
    PROFILE_URL = 'https://www.googleapis.com/plus/v1/people/me/openIdConnect'

    def dispatch(self, request, helper):
        token = helper.fetch_state('data')['access_token']
        r = requests.get(self.PROFILE_URL, params={'access_token': token})
        r.raise_for_status()
        profile = r.json()
        domain = profile.get('hd')
        domains = getattr(settings, 'GOOGLE_WHITE_LISTED_DOMAINS', [])
        if domains:
            if not domain:
                return helper.error('User has no Google apps domain')
            if domain not in domains:
                return helper.error('Google apps domain not in whitelist')
        helper.bind_state('profile', profile)
        return helper.next_step()


class GoogleOAuth2Provider(OAuth2Provider):
    name = 'Google'
    client_id = settings.GOOGLE_OAUTH2_CLIENT_ID
    client_secret = settings.GOOGLE_OAUTH2_CLIENT_SECRET

    def get_auth_pipeline(self):
        return [
            OAuth2Login(
                authorize_url='https://accounts.google.com/o/oauth2/auth',
                client_id=self.client_id,
                scope='openid profile email',
            ),
            OAuth2Callback(
                access_token_url='https://accounts.google.com/o/oauth2/token',
                client_id=self.client_id,
                client_secret=self.client_secret,
            ),
            FetchProfileView(),
        ]

    def build_config(self, state):
        return {}

    def build_identity(self, state):
        profile = state['profile']
        return {
            'email': profile['email'],
            'id': profile['sub'],
            'name': profile.get('name') or '',
        }

    def refresh_identity(self, auth_identity):
        pass
