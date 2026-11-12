import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")                                
    )
)

from src.app import app

def test_pagina_inicial():
    client = app.test_client()
    response = client.get("/")  

    assert response.status_code == 200
    assert response.json["empresa"] == "CodeFactory Solutions"
    assert response.json["status"] == "sucesso"
    