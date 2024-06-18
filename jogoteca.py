from flask import Flask, render_template, request, redirect, session, flash, url_for

class Usuario:
  def __init__(self, nome, nickname, senha) -> None:
    self.nome = nome
    self.nickname = nickname
    self.senha = senha

usuario1 = Usuario("Luiz Gabriel", "luizgabriel1504", "bibi1504")
usuario2 = Usuario("Pedro Miguel", "pedromiguel0602", "pedro0602")
usuario3 = Usuario("Andréa Luciana", "andrealuciana0109", "andrea0109")

usuarios = { usuario1.nickname : usuario1, 
            usuario2.nickname : usuario2,
            usuario3.nickname : usuario3 }

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
def index():
  return render_template('lista.html', titulo = 'Jogos', jogos = lista)

@app.route('/novo_jogo')
def novo_jogo(): 
  if 'usuario_logado' not in session or session['usuario_logado'] == None:
    return redirect(url_for('login', proxima=url_for('novo_jogo')))
  return render_template('novo_jogo.html', titulo = 'Novo Jogo', )

@app.route('/criar', methods=['POST', ])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo = Jogo(nome, categoria, console)
  lista.append(jogo)
  return redirect(url_for('index'))

@app.route('/login')
def login():
  proxima = request.args.get('proxima')
  return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
  if request.form['usuario'] in usuarios:
    usuario = usuarios[request.form['usuario']]
    if request.form['senha'] == usuario.senha:
      session['usuario_logado'] = usuario.nickname
      flash(f'{usuario.nome} logado com sucesso!')
      proxima_pagina = request.form['proxima']
      return redirect(proxima_pagina)
  else:
    flash('Nome de usuário ou senha inválidas.')
    return redirect(url_for('login'))
  
@app.route('/logout')
def logout():
 session['usuario_logado'] = None
 flash('Logout efetuado com sucesso!')
 return redirect(url_for('index'))

app.run(debug=True)
