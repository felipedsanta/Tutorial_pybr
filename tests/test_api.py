from fastapi.testclient import TestClient

import pytest
from http import HTTPStatus
from api_pedidos.api import app

@pytest.fixture
def cliente():
    return TestClient(app)

def test_quando_verificar_integridade_devo_ter_como_retorno_codigo_de_status_200():
    resposta = cliente.get("/healthcheck")
    assert resposta.status_code == HTTPStatus.OK

def test_quando_verificar_integridade_formato_de_retorno_deve_ser_json():
    resposta = cliente.get("/healthcheck")
    assert resposta.headers["Content-Type"] == "application/json"    

def test_quando_verificar_integridade_devo_ter_como_retorno_codigo_de_status_200():
    resposta = cliente.get("/healthcheck")
    assert resposta.json() == {
        "status": "ok"
    }