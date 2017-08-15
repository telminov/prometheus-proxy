import pytest
import server


def test_get_config():
    config_data = server.get_config()
    assert config_data['targets'][0]['name'] == 'localhost:9115'
    assert config_data['targets'][0]['url'] == 'http://localhost:9115'


@pytest.fixture
def cli(loop, test_client):
    app = server.create_app()
    return loop.run_until_complete(test_client(app))


async def test_index(cli):
    resp = await cli.get('/')
    assert resp.status == 200

    text = await resp.text()
    assert 'HTTP exporter' in text


async def test_metrics(cli):
    resp = await cli.get('/metrics')
    assert resp.status == 200
