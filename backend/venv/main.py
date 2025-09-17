# backend/main.py
from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

# Importe os modelos
from models.usuario import Usuario
# Importe as rotas
from routes.usuario_routes import router as usuario_router

app = FastAPI()

@app.on_event("startup")
async def start_database():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.barbeariaDB, document_models=[Usuario])

# Inclui as rotas de usuário no app principal, com um prefixo
app.include_router(usuario_router, prefix="/api/usuarios", tags=["Usuarios"])

@app.get("/")
def ler_raiz():
    return {"mensagem": "Bem-vindo à API da Barbearia!"}