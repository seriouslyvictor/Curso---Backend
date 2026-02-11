# ============================================================
# LIÇÃO 4.4 - HERANÇA DE TEMPLATES E LAYOUTS
# ============================================================
# Objetivo: Criar um layout base que todas as páginas compartilham
# Analogia: Uma moldura de quadro — a moldura é sempre a mesma,
#           só a foto dentro muda!
#
# Arquivos usados:
# - templates/base.html    → o layout (moldura)
# - templates/inicio.html  → página que herda de base.html
# - templates/sobre.html   → outra página que herda
# - templates/galeria.html → outra página que herda
# - templates/contato.html → outra página que herda
# - static/estilo.css      → CSS compartilhado
# ============================================================

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


# -----------------------------
# PARTE 1: O problema sem herança
# -----------------------------
# Sem herança, cada página repete o menu, rodapé, CSS...
# Se quiser mudar o menu, tem que mudar em TODAS as páginas!
#
# COM herança:
# - base.html tem o menu, rodapé, e CSS
# - Cada página define apenas o que é DIFERENTE
# - Mudou o menu em base.html? Mudou em todas as páginas!


# -----------------------------
# PARTE 2: Como funciona a herança
# -----------------------------
#
# base.html define "blocos" com {% block nome %}{% endblock %}
# São espaços vazios que cada página preenche.
#
# Exemplo em base.html:
#   <title>{% block titulo %}Meu Site{% endblock %}</title>
#   <main>{% block conteudo %}{% endblock %}</main>
#
# Exemplo em inicio.html:
#   {% extends "base.html" %}
#   {% block titulo %}Início{% endblock %}
#   {% block conteudo %}<h1>Bem-vindo!</h1>{% endblock %}
#
# Resultado: o HTML de base.html com os blocos preenchidos!


# Variável global: ano atual (disponível em todos os templates)
@app.context_processor
def dados_globais():
    """Variáveis disponíveis em TODOS os templates"""
    return {"ano": datetime.now().year}


# -----------------------------
# PARTE 3: As rotas usando herança
# -----------------------------

@app.route("/")
def inicio():
    """Página inicial - herda de base.html"""
    return render_template("inicio.html")


@app.route("/sobre")
def sobre():
    """Página sobre - herda de base.html"""
    return render_template("sobre.html")


@app.route("/galeria")
def galeria():
    """Galeria de projetos - herda de base.html"""
    projetos = [
        {
            "nome": "Quiz Interativo",
            "descricao": "Jogo de perguntas e respostas com pontuação",
            "modulo": "Módulo 1",
            "emoji": "🎮",
        },
        {
            "nome": "Agenda de Contatos",
            "descricao": "App para gerenciar contatos com JSON",
            "modulo": "Módulo 2",
            "emoji": "📒",
        },
        {
            "nome": "Portfólio Web",
            "descricao": "Site pessoal responsivo com HTML e CSS",
            "modulo": "Módulo 3",
            "emoji": "🌐",
        },
        {
            "nome": "Web App Flask",
            "descricao": "Aplicação web com backend Python",
            "modulo": "Módulo 4",
            "emoji": "🐍",
        },
    ]
    return render_template("galeria.html", projetos=projetos)


@app.route("/contato")
def contato():
    """Página de contato - herda de base.html"""
    return render_template("contato.html")


# ============================================================
# EXERCÍCIO 4.4 - Adicionar uma nova página
# ============================================================
# 1. Crie um arquivo templates/habilidades.html
# 2. Use {% extends "base.html" %} no topo
# 3. Defina {% block titulo %} e {% block conteudo %}
# 4. Liste suas habilidades de programação
# 5. Adicione a rota aqui embaixo:

# @app.route("/habilidades")
# def habilidades():
#     lista = ["Python", "HTML", "CSS", "Flask"]
#     return render_template("habilidades.html", habilidades=lista)


# ============================================================
# CONCEITOS IMPORTANTES
# ============================================================
#
# 1. {% extends "base.html" %} → "esta página herda de base.html"
#    DEVE ser a primeira coisa no arquivo!
#
# 2. {% block nome %}...{% endblock %} → define/preenche um bloco
#    No base.html: cria o espaço
#    No filho: preenche o espaço
#
# 3. url_for('static', filename='estilo.css') → caminho para arquivos
#    estáticos (CSS, imagens, JS) na pasta static/
#
# 4. url_for('inicio') → gera a URL para a função 'inicio'
#    Melhor que escrever "/sobre" direto!
#
# 5. @app.context_processor → variáveis globais para todos os templates


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: {% extends %} não ser a primeira coisa no template
# Se tiver qualquer texto antes de {% extends %}, dá erro!

# ERRO 2: Esquecer o {% endblock %}
# Todo {% block %} precisa fechar com {% endblock %}

# ERRO 3: Pasta static/ no lugar errado
# A pasta static/ deve estar ao lado do seu arquivo .py principal

# ERRO 4: Nome do bloco errado
# Se base.html tem {% block conteudo %}, o filho deve usar o mesmo nome


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ Herança evita repetição de HTML
# ✓ base.html é o "molde" com blocos vazios
# ✓ {% extends %} herda de outro template
# ✓ {% block %} define áreas que mudam em cada página
# ✓ static/ guarda CSS, imagens e JavaScript
# ✓ url_for() gera URLs de forma segura
# ✓ context_processor compartilha dados com todos os templates
# ============================================================


if __name__ == "__main__":
    print("=" * 50)
    print("  Servidor rodando!")
    print("  Abra no navegador: http://localhost:5000")
    print("  Para parar: aperte Ctrl+C no terminal")
    print("=" * 50)
    app.run(debug=True)
