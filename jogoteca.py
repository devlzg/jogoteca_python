from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'Mithrandir'

class Jogo:
  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console

jogo1 = Jogo('Mario 3d Land', 'Plataforma', '3ds')
jogo2 = Jogo('God of War', 'Hack n Slash', 'Ps2')
jogo3 = Jogo('Pokémon Emerald', 'RPG', 'GBA')
jogo4 = Jogo('Dark Souls', 'Action RPG', 'Ps3')
jogo5 = Jogo('Devil May Cry', 'Hack n Slash', 'Ps2')

lista = [jogo1, jogo2, jogo3, jogo4, jogo5]
  
@app.route('/')
def listar_jogos():
  return render_template('lista.html', titulo = 'Jogos', jogos = lista)

@app.route('/novo_jogo')
def novo_jogo(): 
  return render_template('novo_jogo.html', titulo = 'Novo Jogo', )

@app.route('/criar', methods=['POST', ])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo = Jogo(nome, categoria, console)
  lista.append(jogo)
  return redirect('/')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
  if 'senha123' == request.form['senha']:
    session['usuario_logado'] = request.form['usuario']
    nome_do_usuario = session['usuario_logado']
    flash(f'{nome_do_usuario} logado com sucesso!')
    return redirect('/')
  else:
    flash('Nome de usuário ou senha inválidas.')
    return redirect('/login')

app.run(debug=True)
