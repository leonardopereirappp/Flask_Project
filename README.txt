# Bora criar um site?

# Mas primeiro bora pensar em um site:

"""
Temos o front-send e o back-end
Front-end => A parte bonita do site: HTML/CSS
Back-end => A parte escondida do site que gerencia os usuários, banco de dados, etc...
"""

# Lembrando que o recomendável é colocar o site em um V.Env. Mas vou colocar tudo aqui para mostrar todos os projetos

# Para instalar o Flask, basta dar um pip install flask

# O que é um decorator?
# O decorator é uma função que atribui a uma outra função uma nova funcionalidade. Ex.: @app.route que dá a função abaixo (def helloworld), a função de retornar algo para um site

@app.route('/home')
def helloworld():
    return print("Hello world")

# Nesse projeto usaremos o Bootstrap.