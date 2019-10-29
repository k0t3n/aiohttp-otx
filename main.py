from aiohttp import web

from app.settings import MIDDLEWARES
from app.views import routes

app = web.Application(middlewares=MIDDLEWARES)
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
