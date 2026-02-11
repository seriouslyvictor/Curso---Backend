# ============================================================
# LIÇÃO 4.1 - SEU PRIMEIRO SERVIDOR: HELLO FLASK
# ============================================================
# Objetivo: Criar um servidor web que mostra páginas no navegador
# O momento mágico: seu código Python vira um site!
#
# ANTES DE COMEÇAR:
# Instale o Flask no terminal:
#   pip install flask
# ============================================================

# -----------------------------
# PARTE 1: O servidor mais simples do mundo
# -----------------------------
# São só 5 linhas de código para criar um site!

from flask import Flask

# Cria o aplicativo Flask
# __name__ diz ao Flask onde ele está rodando
app = Flask(__name__)


# @app.route("/") significa: quando alguém acessar a página principal...
@app.route("/")
def inicio():
    """Página inicial do site"""
    return "Olá, mundo! Meu primeiro servidor Flask!"


# O que aconteceu aqui?
# 1. Importamos Flask
# 2. Criamos um app
# 3. Definimos uma ROTA ("/") = endereço da página
# 4. A função retorna o texto que aparece no navegador


# -----------------------------
# PARTE 2: Mais páginas (rotas)
# -----------------------------
# Cada @app.route() cria uma página nova no seu site

@app.route("/sobre")
def sobre():
    """Página Sobre"""
    return "Esta é a página Sobre. Estou aprendendo Flask!"


@app.route("/contato")
def contato():
    """Página de Contato"""
    return "Me encontre no GitHub! Esta é minha página de contato."


# Agora seu site tem 3 páginas:
# http://localhost:5000/        → página inicial
# http://localhost:5000/sobre   → página sobre
# http://localhost:5000/contato → página de contato


# -----------------------------
# PARTE 3: Retornando HTML
# -----------------------------
# Você pode retornar HTML ao invés de texto simples!

@app.route("/boas-vindas")
def boas_vindas():
    """Página com HTML básico"""
    return """
    <html>
    <head><title>Boas-vindas</title></head>
    <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1 style="color: #2c3e50;">Bem-vindo ao meu site!</h1>
        <p style="font-size: 18px;">Este site foi feito com Python e Flask.</p>
        <p>Incrível, não é? 🚀</p>
        <hr>
        <p><a href="/">Voltar para o início</a></p>
    </body>
    </html>
    """


# -----------------------------
# PARTE 4: O que é localhost?
# -----------------------------
# localhost = seu próprio computador
# É como dizer "me visite aqui mesmo"
#
# Porta 5000 = a "porta" por onde o site responde
# Pense assim: seu computador é um prédio com várias portas
# Flask usa a porta 5000 por padrão
#
# Então: http://localhost:5000 = "acesse meu computador na porta 5000"


# ============================================================
# EXERCÍCIO 4.1 - Criando Suas Próprias Páginas
# ============================================================
# Adicione pelo menos 2 rotas novas ao seu servidor.
# Ideias:
# - /hobbies → liste seus hobbies
# - /escola → informações sobre sua escola
# - /favoritos → suas músicas, filmes ou jogos favoritos
#
# Use HTML para deixar as páginas mais bonitas!
# Dica: use tags <h1>, <p>, <ul>, <li>, <a href="">

@app.route("/hobbies")
def hobbies():
    """Página de hobbies - exemplo do exercício"""
    return """
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 50px auto;">
        <h1>🎮 Meus Hobbies</h1>
        <ul style="font-size: 18px;">
            <li>Programar em Python</li>
            <li>Jogar videogame</li>
            <li>Ouvir música</li>
            <li>Assistir séries</li>
        </ul>
        <p><a href="/">← Voltar para o início</a></p>
    </body>
    </html>
    """


@app.route("/escola")
def escola():
    """Página da escola - exemplo do exercício"""
    return """
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 50px auto;">
        <h1>🏫 Minha Escola</h1>
        <p><strong>Nome:</strong> Escola Estadual Exemplo</p>
        <p><strong>Série:</strong> 2º ano do Ensino Médio</p>
        <p><strong>Matéria favorita:</strong> Informática!</p>
        <p><a href="/">← Voltar para o início</a></p>
    </body>
    </html>
    """


# ============================================================
# DESAFIO EXTRA - Página de Navegação
# ============================================================
# Crie uma página que tenha links para TODAS as outras páginas
# Como um menu de navegação!

@app.route("/menu")
def menu():
    """Menu com links para todas as páginas"""
    return """
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 50px auto;">
        <h1>📋 Menu do Site</h1>
        <nav style="font-size: 18px; line-height: 2;">
            <p><a href="/">🏠 Início</a></p>
            <p><a href="/sobre">ℹ️ Sobre</a></p>
            <p><a href="/contato">📧 Contato</a></p>
            <p><a href="/boas-vindas">👋 Boas-vindas</a></p>
            <p><a href="/hobbies">🎮 Hobbies</a></p>
            <p><a href="/escola">🏫 Escola</a></p>
        </nav>
    </body>
    </html>
    """


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: Esquecer de instalar o Flask
# pip install flask    ← rode isso no terminal!

# ERRO 2: Duas rotas com o mesmo nome de função
# @app.route("/a")
# def pagina(): ...
# @app.route("/b")
# def pagina(): ...  ← ERRO! Nomes de função devem ser únicos

# ERRO 3: Esquecer a barra no início da rota
# @app.route("sobre")   ← ERRADO
# @app.route("/sobre")  ← CERTO

# ERRO 4: Rodar o arquivo e nada acontecer
# Precisa do app.run() lá embaixo!


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ Flask transforma Python em um servidor web
# ✓ @app.route() define os endereços (URLs) do site
# ✓ Cada rota tem uma função que retorna o conteúdo
# ✓ Você pode retornar texto simples ou HTML
# ✓ localhost:5000 é o endereço do seu servidor local
# ✓ debug=True reinicia o servidor quando você salva o código
# ============================================================


# IMPORTANTE: Este bloco faz o servidor rodar!
# debug=True = reinicia sozinho quando você muda o código
if __name__ == "__main__":
    print("=" * 50)
    print("  Servidor rodando!")
    print("  Abra no navegador: http://localhost:5000")
    print("  Para parar: aperte Ctrl+C no terminal")
    print("=" * 50)
    app.run(debug=True)
