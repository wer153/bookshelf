from litestar import Litestar
from litestar.status_codes import HTTP_200_OK
from litestar.testing import TestClient


def test_healthcheck(test_client: TestClient[Litestar]) -> None:
    with test_client as client:
        response = client.get("/healthcheck")
        assert response.status_code == HTTP_200_OK
        assert response.json() == {"message:": "healthy"}
