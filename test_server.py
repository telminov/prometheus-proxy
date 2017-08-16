import pytest
import server


@pytest.fixture
def cli(loop, test_client):
    app = server.create_app()
    return loop.run_until_complete(test_client(app))


async def test_index(cli):
    resp = await cli.get('/')
    assert resp.status == 200

    text = await resp.text()
    assert 'HTTP proxy' in text


async def test_metrics(cli):
    resp = await cli.get('/metrics')
    assert resp.status == 500
