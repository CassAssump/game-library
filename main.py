from flask import Flask,render_template, request, redirect,session,flash
import os



class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.console = console
        self.categoria = categoria

jogo1= Jogo("Tetris", "Puzzle","Atari")
jogo2= Jogo("God of War", "Hack and slash", "ps2")
jogo3= Jogo("Mortal kombat","Luta","ps2")
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():


    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/novo")
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    
    return render_template("novo.html", titulo="Novo jogo")




@app.route("/criar", methods=['POST',])
def criar():

    nome = request.form["nome"]
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect("/")


@app.route("/login")
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)
    
   

@app.route ("/autenticar", methods=["POST",])
def autenticar():
    if 'admin' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado' ] + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(f'/{proxima_pagina}')
    else:
        flash('usuario não logado')
        return redirect ("/login")
    

@app.route ('/logout')
def logout():
    session ['usuario_logado'] = None
    flash ('Logout efetuado com sucesso! ')
    return redirect ('/')


app.run(debug=True)