import pytest
from litestar import Litestar
from litestar.testing import TestClient

from app.main import create_app


@pytest.fixture(scope="session")
def app() -> Litestar:
    return create_app()


@pytest.fixture
def test_client(app: Litestar) -> TestClient[Litestar]:
    return TestClient(app=app)
