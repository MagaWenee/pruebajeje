
import falcon
import falcon.asgi

from app.version import V1

class Ping:
    async def on_get(self, req, resp):
        """ Handles GET requests """
        resp.status = falcon.HTTP_200
        resp.media = dict(ping="pong")

api = falcon.asgi.App()
api.add_route(f"{V1}/ping", Ping())