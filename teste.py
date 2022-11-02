from projetosite.models import Usuario, Post, Comentarios
from projetosite import database

database.create_all()

usuario = Comentarios.query[0]
print(usuario.corpo)
print(usuario.titulo)

