from pydantic import BaseModel


class PostgresConfig(BaseModel):
    username: str = "postgres"
    password: str = "password"
    host: str = "localhost"
    port: int = 8000
    db_name: str = "bookshelf"
