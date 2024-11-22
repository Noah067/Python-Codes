from pydantic import BaseModel
class Usuario(BaseModel):
    nome: str
    idade: int
    email: str
usuario = Usuario(nome="Abel",idade=16,email='abel2example.com')
print(usuario.nome)
print(usuario.idade)
print(usuario.email)

