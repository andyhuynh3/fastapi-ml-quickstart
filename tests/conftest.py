import pytest
from starlette.testclient import TestClient


from api.main import app
from api.ml.model import get_model
from .mocks import MockModel


def get_model_override():
    model = MockModel()
    return model


app.dependency_overrides[get_model] = get_model_override


@pytest.fixture()
def test_client():
    return TestClient(app)
