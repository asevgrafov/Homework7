from aiohttp.web import Application, run_app
import aiohttp_autoreload
from aiopg.sa import create_engine


from app.routes import inject_routes
import config


async def pg_engine(app):
    """Создаёт один пул подключений на приложение."""
    dsn = config.ENGINE_STRING
    app["engine"] = await create_engine(dsn)
    yield
    app["engine"].close()
    await app["engine"].wait_closed()


def run():
    """Запуск приложения."""
    if config.ENABLE_AUTORELOAD:
        aiohttp_autoreload.start()

    app = Application()

    inject_routes(app)
    app.cleanup_ctx.append(pg_engine)

    run_app(
        app,
        host=config.API_SERVER_HOST,
        port=config.API_SERVER_PORT,
    )
