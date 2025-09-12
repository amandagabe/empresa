from flask import Flask, send_from_directory, render_template_string, request, Response
import os

app = Flask(__name__)
PASTA = r'C:\DADOS\ATENDIMENTO'

USUARIO = 'amanda'
SENHA = 'senha123'

def autenticar():
    return Response(
        'Autenticação necessária.', 401,
        {'WWW-Authenticate': 'Basic realm="Login obrigatório"'}
    )

def verificar_login():
    auth = request.authorization
    return auth and auth.username == USUARIO and auth.password == SENHA

@app.route('/')
def listar_arquivos():
    if not verificar_login():
        return autenticar()

    arquivos = os.listdir(PASTA)
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Arquivos Disponíveis</title>
        <style>
            body {
                background-color: #0A464E;
                color: white;
                font-family: Arial, sans-serif;
                padding: 20px;
            }
            h2 {
                color: #00995D;
            }
            a {
                color: #00995D;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h2>Arquivos disponíveis:</h2>
        <ul>
        {% for arquivo in arquivos %}
            <li><a href="/arquivos/{{ arquivo }}">{{ arquivo }}</a></li>
        {% endfor %}
        </ul>
    </body>
    </html>
    """
    return render_template_string(html, arquivos=arquivos)

@app.route('/arquivos/<path:nome_arquivo>')
def baixar_arquivo(nome_arquivo):
    if not verificar_login():
        return autenticar()
    return send_from_directory(PASTA, nome_arquivo)

if __name__ == '__main__':
    app.run(debug=True)
