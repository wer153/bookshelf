from advanced_alchemy.extensions.litestar.plugins.init.config import (
    SQLAlchemyAsyncConfig,
)
from advanced_alchemy.extensions.litestar.plugins.init.plugin import (
    SQLAlchemyInitPlugin,
)
from settings import PostgresConfig

_DATABASE_URI = (
    "postgresql+asyncpg://"
    f"{PostgresConfig.username}:{PostgresConfig.password}@"
    f"{PostgresConfig.host}:{PostgresConfig.port}/{PostgresConfig.db_name}"
)


def _get_init_plugin() -> SQLAlchemyInitPlugin:
    return SQLAlchemyInitPlugin(
        config=SQLAlchemyAsyncConfig(connection_string=_DATABASE_URI),
    )


PLUGIN = _get_init_plugin()
