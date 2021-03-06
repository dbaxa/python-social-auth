"""
This module is originally written: django-social-auth-appsfuel==1.0.0
You could refer to https://github.com/AppsFuel/django-social-auth-appsfuel for
issues.

Needed keys are:
    SOCIAL_AUTH_APPSFUEL_KEY = ''
    SOCIAL_AUTH_APPSFUEL_SECRET = ''
"""
from social.backends.oauth import BaseOAuth2


class AppsfuelOAuth2(BaseOAuth2):
    name = 'appsfuel'
    ID_KEY = 'user_id'
    AUTHORIZATION_URL = 'http://app.appsfuel.com/content/permission'
    ACCESS_TOKEN_URL = 'https://api.appsfuel.com/v1/live/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'
    USER_DETAILS_URL = 'https://api.appsfuel.com/v1/live/user'

    def get_user_details(self, response):
        """Return user details from Appsfuel account"""
        fullname = response.get('display_name', '')
        email = response.get('email', '')
        username = email.split('@')[0] if email else ''
        return {
            'username': username,
            'first_name': fullname,
            'email': email
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json(self.USER_DETAILS_URL, params={
            'access_token': access_token
        })


class AppsfuelOAuth2Sandbox(AppsfuelOAuth2):
    name = 'appsfuel-sandbox'
    AUTHORIZATION_URL = 'https://api.appsfuel.com/v1/sandbox/choose'
    ACCESS_TOKEN_URL = 'https://api.appsfuel.com/v1/sandbox/oauth/token'
    USER_DETAILS_URL = 'https://api.appsfuel.com/v1/sandbox/user'
