from aiohttp import web

from app.views import CheckOrders, PostOrders


def inject_routes(app: web.Application) -> None:
    """Инициализация роутов."""
    app.add_routes(
        [
            web.view("/order", CheckOrders),
            web.view("/orders", PostOrders)
        ]
    )
