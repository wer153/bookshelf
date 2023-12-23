from db.connection import PLUGIN as DB_PLUGIN
from litestar import Litestar, get, post


@get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"message:": "healthy"}


@post("/books")
async def add_book(isbn: str) -> str:
    return isbn


def create_app() -> Litestar:
    app = Litestar(
        [healthcheck],
        plugins=[DB_PLUGIN],
    )
    return app
