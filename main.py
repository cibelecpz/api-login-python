from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine("sqlite:///usuarios.db")
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class UsuarioDB(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)


Base.metadata.create_all(bind=engine)


class Usuario(BaseModel):
    nome: str
    email: str
    senha: str


@app.get("/")
def inicio():
    return {"mensagem": "API de Login com banco funcionando!"}


@app.post("/usuarios")
def cadastrar_usuario(usuario: Usuario):
    db = SessionLocal()

    novo_usuario = UsuarioDB(
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    db.close()

    return {
        "mensagem": "Usuário cadastrado com sucesso!",
        "usuario": novo_usuario
    }


@app.get("/usuarios")
def listar_usuarios():
    db = SessionLocal()
    usuarios = db.query(UsuarioDB).all()
    db.close()
    return usuarios


@app.post("/login")
def login(email: str, senha: str):
    db = SessionLocal()

    usuario = db.query(UsuarioDB).filter(
        UsuarioDB.email == email,
        UsuarioDB.senha == senha
    ).first()

    db.close()

    if usuario:
        return {"mensagem": "Login realizado com sucesso!"}

    return {"erro": "Email ou senha inválidos"}


produtos = [
    {"id": 1, "nome": "Camiseta Premium", "preco": 79.90},
    {"id": 2, "nome": "Boné Preto", "preco": 39.90}
]


@app.get("/produtos")
def listar_produtos():
    return produtos