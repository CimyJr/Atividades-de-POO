from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aluno.db'

db = SQLAlchemy(app)


class Aluno(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, index=True, unique=False)
    password = db.Column(db.String(255))


    def __init__(self, email, password):
        self.email = email
        self.password = password


    def __repr__(self):
        return '<Email %r>' % self.email


db.create_all()


@app.route('/')
def home():
    result = "<h1>Tabelas</h1><br><ul>"
    for table in db.metadata.tables.items():
        result += "<li>%s</li>" % str(table)
    result += "</ul>"
    return result


@app.route('/add')
def add_aluno():
    test = Aluno(email='cimyqueiroz@flask.com', password='123456')
    db.session.add(test)
    db.session.commit()
    result = "Aluno Adicionado"
    return result


@app.route('/del/<int:id>')
def del_aluno(id):
    aluno = Aluno.query.get(id)
    db.session.delete(aluno)
    db.session.commit()
    return "Aluno Removido"


@app.route('/list')
def list():
    aluno = Aluno.query.order_by(Aluno.id).all()
    lista = "<h1>Lista de Alunos</h1><br><ul>"
    for aluno in aluno:
        lista += '<p>'
        lista += 'Id = '  + str(aluno.id)
        lista += ' Email = ' + aluno.email
        lista += ' Senha = ' + aluno.password
        lista += '</p>'
    return lista


@app.route('/find/<int:id>')
def find(id):
    aluno = Aluno.query.get(id)
    result = "<h1>Aluno Encontrado</h1><br><ul>"
    result += "<p> Id=" + str(aluno.id) + "</p>"
    result += "<p> Nome=" + aluno.email + "</p>"
    result += "<p> Senha=" + aluno.password + "</p>"
    return result


@app.route('/change/<int:id>')
def change(id):
    aluno = Aluno.query.get(id)
    aluno.email = 'cimy@flask.com'
    db.session.commit()
    return 'Aluno mudado'


if __name__ == '__main__':
    app.run()
