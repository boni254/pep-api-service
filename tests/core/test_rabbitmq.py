import datetime

import pytest
from django.contrib.contenttypes.models import ContentType

from app.core.rabbitmq import publish_to_rabbitmq

pytestmark = pytest.mark.django_db


class TestSpectacularElementsViewSpectacularElementsView:
    def test_rabbitmq_publish(self):
        message = {"test": "data"}

        try:
            publish_to_rabbitmq(message)
            assert True
        except Exception as e:
            raise AssertionError(f"RabbitMQ publish failed: {str(e)}") from e

    def test_rabbitmq_publish_invalid_data(self):
        message = object()

        with pytest.raises(TypeError):
            publish_to_rabbitmq(message)

    def test_rabbitmq_publish_datetime(self):
        message = {"test": datetime.datetime.now()}

        try:
            publish_to_rabbitmq(message)
            assert True
        except Exception as e:
            raise AssertionError(f"RabbitMQ publish failed: {str(e)}") from e

    def test_django_database_access(self):
        assert ContentType.objects.first() is not None
