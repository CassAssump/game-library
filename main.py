from flask import Flask,render_template, request, redirect

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

@app.route('/')
def index():


    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/novo")
def novo():
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
    return render_template('login.html')



app.run(debug=True)