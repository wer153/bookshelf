from pydantic import BaseModel


class _PostgresConfig(BaseModel):
    username: str = "postgres"
    password: str = "password"
    host: str = "postgres"
    port: int = 5432
    db_name: str = "bookshelf"


POSTGRES_CONFIG = _PostgresConfig()
