from litestar import Litestar, get


@get("/healthcheck")
async def healthcheck() -> str:
    return "healthy"


app = Litestar([healthcheck])
