# backend/routes/usuario_routes.py
from fastapi import APIRouter, HTTPException, status
from models.usuario import Usuario, UsuarioCreate

# Para criptografar a senha
from passlib.context import CryptContext

# Cria um "roteador". É como um mini-app FastAPI que podemos incluir no principal.
router = APIRouter()

# Configuração para hashing de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/cadastro", status_code=status.HTTP_201_CREATED, response_model=Usuario)
async def criar_usuario(data: UsuarioCreate):
    """
    Endpoint para cadastrar um novo usuário.
    """
    # 1. Verifica se já existe um usuário com o mesmo e-mail
    usuario_existente = await Usuario.find_one(Usuario.email == data.email)
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Este e-mail já está cadastrado."
        )

    # 2. Criptografa a senha fornecida
    senha_hash = pwd_context.hash(data.senha)

    # 3. Cria uma instância do modelo Usuario com os dados prontos para o banco
    novo_usuario = Usuario(
        nome=data.nome,
        email=data.email,
        senha_hash=senha_hash
    )

    # 4. Insere o novo usuário no banco de dados
    await novo_usuario.insert()

    return novo_usuario