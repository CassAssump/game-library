from flask import Flask,render_template, request, redirect,session,flash, url_for
import os

usuarios = []

class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.console = console
        self.categoria = categoria

jogo1= Jogo("Tetris", "Puzzle","Atari")
jogo2= Jogo("God of War", "Hack and slash", "ps2")
jogo3= Jogo("Mortal kombat","Luta","ps2")
lista = [jogo1, jogo2, jogo3]

class Usuario():
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario1 = Usuario('Cassiano Rocha', 'cass', 'admin')
usuario2 = Usuario('Matheus abreo', 'abreo', 'admin2')
usuario3 = Usuario('Rosane rocha', 'Rosa', 'admin3')

usuarios = { usuario1.nickname :usuario1, 
                usuario2.nickname :usuario2,
                usuario3.nickname :usuario3 }

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():


    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/novo")
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    
    return render_template("novo.html", titulo="Novo jogo")




@app.route("/criar", methods=['POST',])
def criar():

    nome = request.form["nome"]
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = url_for('index')
    return render_template('login.html',proxima=proxima)
    
   

@app.route ("/autenticar", methods=["POST",])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios [request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso ')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
            
    else:
        flash('Usuario não logado')
        return redirect(url_for('login'))

@app.route ('/logout')
def logout():
    session ['usuario_logado'] = None
    flash ('Logout efetuado com sucesso! ')
    return redirect (url_for('index'))


app.run(debug=True)