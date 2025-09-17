# backend/models/usuario.py
from beanie import Document
from pydantic import BaseModel, EmailStr

class Usuario(Document):
    """
    Modelo que representa um Usuário no banco de dados.
    A classe 'Document' do Beanie faz a mágica de conectar
    esta classe à uma coleção no MongoDB.
    """
    nome: str
    email: EmailStr  # O Pydantic valida automaticamente se o formato é de um e-mail
    senha_hash: str

    class Settings:
        # Define o nome da "tabela" (coleção) no MongoDB
        name = "usuarios"

class UsuarioCreate(BaseModel):
    """
    Modelo usado para receber os dados de criação de um novo usuário.
    Não queremos receber a senha já em hash, então criamos um modelo
    separado só para a entrada de dados.
    """
    nome: str
    email: EmailStr
    senha: str