from litestar import Litestar, get, post


@get("/healthcheck")
async def healthcheck() -> str:
    return "healthy"


@post("/books")
async def add_book(isbn: str) -> str:
    return isbn


app = Litestar([healthcheck])
