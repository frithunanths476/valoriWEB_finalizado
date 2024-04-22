from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import relationship
from flask_bcrypt import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/valori'
db = SQLAlchemy(app)


class Despesa(db.Model):
    id_despesa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_emissao = db.Column(db.Date)
    valor = db.Column(db.Integer)
    descricao = db.Column(db.String(256))
    nome_despesa = db.Column(db.String(256))
    id_usuario = db.Column(db.Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship("Usuario", back_populates="despesas")


class Receita(db.Model):
    id_receita = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_emissao = db.Column(db.Date)
    valor = db.Column(db.Integer)
    descricao = db.Column(db.String(256))
    nome_receita = db.Column(db.String(256))
    id_usuario = db.Column(db.Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship("Usuario", back_populates="receitas")


class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(254))
    senha = db.Column(db.String(50))
    despesas = relationship("Despesa", back_populates="usuario")
    receitas = relationship("Receita", back_populates="usuario")


@app.route('/main')
def index():
    if 'user_id' in session:
        valori = Usuario.query.all()

        id_usuario = session['user_id']

        receitas = db.session.query(Receita).filter_by(id_usuario=id_usuario).all()

        despesas = db.session.query(Despesa).filter_by(id_usuario=id_usuario).all()

        total_receita = (db.session.query(func.coalesce(func.sum(Receita.valor), 0)).filter_by(id_usuario=id_usuario).
                         scalar())

        total_despesa = (db.session.query(func.coalesce(func.sum(Despesa.valor), 0)).filter_by(id_usuario=id_usuario).
                         scalar())

        total = total_receita - total_despesa

        return render_template('index.html', outro=valori,
                               receitaUnit=receitas,
                               despesaUnit=despesas,
                               receita=total_receita,
                               despesa=total_despesa,
                               total=total)
    else:
        return render_template('login.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    valori = Usuario.query.filter_by(nome=nome, email=email, senha=senha).first()
    if valori:
        flash("Usuário já existente!", 'error')
        return redirect(url_for('cadastro'))
    else:
        senha_hash = generate_password_hash(senha).decode('utf-8')
        novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('login_form'))


@app.route('/')
def login_form():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    senha_form = request.form.get('senha')

    user = Usuario.query.filter_by(email=email).first()
    if user and check_password_hash(user.senha, senha_form):
        session['user_id'] = user.id_usuario
        if 'next' in session:
            next_route = session.pop('next')
            return redirect(url_for(next_route))
        return redirect(url_for('index'))
    else:
        flash('Email ou senha incorretos', 'error')
        return redirect(url_for('login_form'))


@app.route('/logout', methods=['POST'])
def logout():
    # Remova as chaves da sessão relacionadas ao usuário autenticado
    session.pop('user_id', None)
    # Redirecione para a página inicial ou outra página após o logout
    return redirect(url_for('login_form'))


@app.route('/despesa')
def despesa():
    if 'user_id' in session:
        return render_template('despesa.html')
    else:
        return render_template('login.html')


@app.route('/adicionar_despesa', methods=['POST'])
def despesa_post():
    nome_despesa = request.form.get('nome_despesa')
    descricao = request.form.get('descricao_despesa')
    data_emissao = request.form.get('data_despesa')
    valor = request.form.get('valor_despesa')
    id_usuario = session['user_id']

    despesa = Despesa.query.filter_by(nome_despesa=nome_despesa,
                                      descricao=descricao,
                                      data_emissao=data_emissao,
                                      valor=valor,
                                      id_usuario=id_usuario).first()
    if despesa:
        flash('Despesa já existe', 'error')
        return redirect(url_for('despesa'))
    else:
        nova_despesa = Despesa(nome_despesa=nome_despesa,
                               descricao=descricao,
                               data_emissao=data_emissao,
                               valor=valor,
                               id_usuario=id_usuario)
        db.session.add(nova_despesa)
        db.session.commit()
        flash('Despesa inserida com sucesso', 'success')
        return redirect(url_for('index'))


@app.route('/receita')
def receita():
    if 'user_id' in session:
        return render_template('receita.html')
    else:
        return render_template('login.html')


@app.route('/adicionar_receita', methods=['POST'])
def receita_post():
    nome_receita = request.form.get('nome_receita')
    descricao = request.form.get('descricao_receita')
    data_emissao = request.form.get('data_receita')
    valor = request.form.get('valor_receita')
    id_usuario = session['user_id']

    receita = Receita.query.filter_by(nome_receita=nome_receita,
                                      descricao=descricao,
                                      data_emissao=data_emissao,
                                      valor=valor,
                                      id_usuario=id_usuario).first()

    if receita:
        flash('Receita já existe', 'error')
        return redirect(url_for('receita'))
    else:
        nova_receita = Receita(nome_receita=nome_receita,
                               descricao=descricao,
                               data_emissao=data_emissao,
                               valor=valor,
                               id_usuario=id_usuario)
        db.session.add(nova_receita)
        db.session.commit()
        flash('Receita inserida com sucesso', 'success')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
