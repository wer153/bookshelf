from __future__ import annotations

from litestar.contrib.sqlalchemy.base import UUIDBase
from litestar.contrib.sqlalchemy.plugins import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyInitPlugin,
)

from app.settings import PostgresConfig

_DATABASE_URI = (
    "postgresql+asyncpg://"
    f"{PostgresConfig.username}:{PostgresConfig.password}@"
    f"{PostgresConfig.host}:{PostgresConfig.port}/{PostgresConfig.db_name}"
)

_SESSION_CONFIG = AsyncSessionConfig(expire_on_commit=False)
_SQLALCHEMY_CONFIG = SQLAlchemyAsyncConfig(
    connection_string=_DATABASE_URI,
    session_config=_SESSION_CONFIG,
)


async def init_db() -> None:
    async with _SQLALCHEMY_CONFIG.get_engine().begin() as conn:
        await conn.run_sync(UUIDBase.metadata.create_all)


PLUGIN = SQLAlchemyInitPlugin(
    config=_SESSION_CONFIG,
)
