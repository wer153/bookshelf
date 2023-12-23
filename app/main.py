from litestar import Litestar, get, post

from app.db.connection import PLUGIN as DB_PLUGIN
from app.db.connection import init_db


@get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"message:": "healthy"}


@post("/books")
async def add_book(isbn: str) -> str:
    return isbn


def create_app() -> Litestar:
    app = Litestar(
        on_startup=init_db,
        route_handlers=[healthcheck],
        plugins=[DB_PLUGIN],
    )
    return app
