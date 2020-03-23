import pytest
from nameko.testing.services import worker_factory

from service import RPCGreetingService, HttpGreetingService


def test_rpc_greeting():
    greeting = worker_factory(RPCGreetingService)
    assert greeting.hello('World') == 'Hello World'

@pytest.fixture
def web_session(container_factory, web_config, web_session):
    container = container_factory(HttpGreetingService, web_config)
    container.start()
    return web_session


def test_get_hello(web_session):
    result = web_session.get('/greeting/World')
    assert result.text == '{"greeting": "Hello World"}'


if __name__ == "__main__":
    import sys

    pytest.main(sys.argv)
