import time

from litestar import Litestar, get, post
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.connection import PLUGIN as DB_PLUGIN
from app.db.connection import init_db


@get("/healthcheck")
async def healthcheck(db_session: AsyncSession) -> dict[str, str]:
    ping_query = text("SELECT 1")
    start_time = time.time()
    await db_session.execute(ping_query)
    end_time = time.time()
    connection_time_ms = (end_time - start_time) * 1000
    return {
        "message:": "healthy",
        "connection_time": f"{connection_time_ms:.0f}",
    }


@post("/books")
async def add_book(isbn: str) -> str:
    return isbn


def create_app() -> Litestar:
    app = Litestar(
        on_startup=[init_db],
        route_handlers=[healthcheck],
        plugins=[DB_PLUGIN],
    )
    return app
