# main.py
from fastapi import FastAPI

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define um "endpoint" na raiz do site ("/")
# Quando alguém acessar a URL principal, a função abaixo será executada
@app.get("/")
def ler_raiz():
    return {"mensagem": "Bem-vindo à API da Barbearia!"}