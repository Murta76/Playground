from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    dados = {"nome": "teste", "profissao": "marido", "canal": "teste"}
    return render_template('index.html', dados=dados)
@app.route('/contato')
def contato():
    return render_template('contato.html')
