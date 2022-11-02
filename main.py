from projetosite import app  # Se tiver dentro de um __init__ é só importar de forma direta
#  from projeto_site.models import Usuario  # Para importar uma arquivo de uma pasta faça assim

if __name__ == '__main__':
    app.run(debug=True)
