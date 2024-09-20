from django.conf import settings
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from rest_framework import authentication, exceptions


class AuthToken(authentication.BaseAuthentication):
    keyword = "Bearer"

    def authenticate(self, request):
        auth = authentication.get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = "Invalid token header. No credentials provided."
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = "Invalid token header. Token string should not contain spaces."
            raise exceptions.AuthenticationFailed(msg)

        try:
            auth_token = auth[1].decode()
        except UnicodeError as err:
            msg = "Invalid token header. Token string should not contain invalid characters."
            raise exceptions.AuthenticationFailed(msg) from err

        return self.authenticate_credentials(auth_token)

    def authenticate_credentials(self, auth_token):
        if auth_token != settings.AUTH_TOKEN:
            msg = "Invalid token header. Token is invalid."
            raise exceptions.AuthenticationFailed(msg)

        return (True, auth_token)

    def authenticate_header(self, request):
        return self.keyword


class AuthTokenScheme(OpenApiAuthenticationExtension):
    target_class = "app.core.authentication.AuthToken"
    name = "Auth Token"
    description = "Auth Token"

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name="Authorization",
            token_prefix=self.target.keyword,
        )
