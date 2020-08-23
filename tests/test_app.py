def teste_app(app):
    assert app.name == "delivery.app"

def test_config_is_loader(config):
    assert config["DEBUG"] == False

def test_request_returns_404(client):
    assert client.get("/ur_que_nao_existe").status_code == 404