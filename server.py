#! /usr/bin/env python
import argparse
from aiohttp import web, ClientSession, TCPConnector
import async_timeout

parser = argparse.ArgumentParser(description='Prometheus HTTP proxy.')
parser.add_argument('--host', dest='host', default='0.0.0.0',
                    help='HTTP server host. Default 0.0.0.0')
parser.add_argument('-p', '--port', dest='port', default=9126, type=int,
                    help='HTTP server port. Default 9126')
args = parser.parse_args()

HTTP_STATUS_ERROR = 500


def create_app() -> web.Application:
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_get('/metrics', metrics)
    return app


async def _request(target: str, headers: dict, scheme: str = 'http', path: str = '/metrics',
                   verify_ssl: bool = True) -> tuple:
    try:
        url = scheme + '://' + target + path
        verify_ssl = verify_ssl

        connector = TCPConnector(verify_ssl=verify_ssl)
        async with ClientSession(connector=connector) as session:
            with async_timeout.timeout(10):
                async with session.get(url, headers=headers) as response:
                    return (await response.text(), response.status, response.headers)
    except Exception as ex:
        return (str(ex), HTTP_STATUS_ERROR, {})

async def index(request):
    return web.Response(text='<h1>HTTP proxy</h1><p><a href="/metrics">Metrics</a><p>', content_type='text/html')

async def metrics(request):
    params = dict()
    params['headers'] = request.headers
    params['target'] = request.query['target']

    if request.query.get('scheme'):
        params['scheme'] = request.query.get('scheme')
    if request.query.get('path'):
        params['path'] = request.query.get('path')
    if request.query.get('verify_ssl'):
        params['verify_ssl'] = request.query.get('verify_ssl')

    result, status, response_headers = await _request(**params)

    return web.Response(text=result, status=status, headers=response_headers)


if __name__ == '__main__':
    app = create_app()
    web.run_app(app, host=args.host, port=args.port)
