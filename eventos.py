from flask import Flask, render_template, request, redirect, url_for

from models import Evento
from dao import EventoDao
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "0.0.0.0"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "my_logger"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

evento_dao = EventoDao(db)


@app.route('/')
def index():
	lista_eventos = evento_dao.listar()
	return render_template('lista.html', eventos=lista_eventos, titulo="Meus Eventos")


@app.route('/criar', methods=['POST', ])
def criar():
	nome = request.form['nome']
	data_inicio = request.form['data_inicio']
	data_fim = request.form['data_fim']
	novo_evento = Evento(nome, data_inicio, data_fim)

	evento_dao.salvar(novo_evento)
	return redirect('/')


@app.route('/novo')
def novo():
	return render_template('form.html', titulo="Novo Evento")


@app.route('/deletar/<int:id>')
def deletar(id):
	evento_dao.deletar(id)
	return redirect(url_for('index'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
