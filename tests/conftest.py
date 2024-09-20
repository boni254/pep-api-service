# from unittest import mock

import pytest
from rest_framework.test import APIClient, APIRequestFactory


@pytest.fixture
def api_request():
    return APIRequestFactory()


@pytest.fixture
def api_client():
    return APIClient()
