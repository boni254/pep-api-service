import pytest
from rest_framework.exceptions import AuthenticationFailed

from app.core.authentication import AuthToken, AuthTokenScheme

pytestmark = pytest.mark.django_db


class TestAuthToken:
    def test_authenticate_success(self, api_request, settings):
        settings.AUTH_TOKEN = "match-token"
        auth_token = "match-token"

        api_request.META = {"HTTP_AUTHORIZATION": f"Bearer {auth_token}"}

        is_authenticated, authenticated_token = AuthToken().authenticate(request=api_request)

        assert is_authenticated
        assert authenticated_token == auth_token

    def test_authenticate_skip_if_no_auth(self, api_request):
        api_request.META = {}

        authenticated = AuthToken().authenticate(request=api_request)

        assert authenticated is None

    def test_authenticate_invalid_header_no_token(self, api_request):
        api_request.META = {"HTTP_AUTHORIZATION": "Bearer"}

        with pytest.raises(AuthenticationFailed):
            AuthToken().authenticate(request=api_request)

    def test_authenticate_invalid_header_multiple_tokens(self, api_request, settings):
        settings.AUTH_TOKEN = "no-match"
        api_request.META = {"HTTP_AUTHORIZATION": "Bearer token1 token2"}

        with pytest.raises(AuthenticationFailed):
            AuthToken().authenticate(request=api_request)

    def test_authenticate_invalid_header_unicode_error(self, api_request, settings):
        settings.AUTH_TOKEN = "não-ascii"
        api_request.META = {"HTTP_AUTHORIZATION": "Bearer não-ascii"}

        with pytest.raises(AuthenticationFailed):
            AuthToken().authenticate(request=api_request)

    def test_authenticate_invalid_header_invalid_secret(self, api_request, settings):
        settings.AUTH_TOKEN = "no-match"
        api_request.META = {"HTTP_AUTHORIZATION": "Bearer failed"}

        with pytest.raises(AuthenticationFailed):
            AuthToken().authenticate(request=api_request)

    def test_authenticate_header(self, api_request):
        assert AuthToken().authenticate_header(api_request) == AuthToken.keyword


class TestAuthTokenScheme:
    def test_get_security_definition(self, mocker):
        Auth = mocker.MagicMock(keyword="Bearer")

        security_definition = AuthTokenScheme(target=Auth).get_security_definition(auto_schema=None)

        assert security_definition == {
            "type": "http",
            "scheme": "bearer",
        }
