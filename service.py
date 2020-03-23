from nameko.rpc import rpc
from nameko.web.handlers import http
import json


class RPCGreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return f"Hello {name}"


class HttpGreetingService:
    name = 'greeting_http_service'

    @http('GET', '/greeting/<string:user_name>')
    def get_hello(self, request, user_name):
        return json.dumps(dict(greeting=f"Hello {user_name}"))
