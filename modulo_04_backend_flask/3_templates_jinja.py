# ============================================================
# LIÇÃO 4.3 - TEMPLATES COM JINJA2
# ============================================================
# Objetivo: Separar o HTML do Python usando templates
# Motivação: Escrever HTML dentro de strings Python é confuso!
#            Templates deixam cada coisa no seu lugar.
#
# Templates ficam na pasta templates/
# O Flask encontra eles automaticamente!
# ============================================================

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


# -----------------------------
# PARTE 1: O problema sem templates
# -----------------------------
# Na lição anterior, fizemos isso:

@app.route("/")
def inicio():
    return """
    <html>
    <body style="font-family: Arial; max-width: 700px; margin: 50px auto;">
        <h1>📄 Lição 4.3 - Templates com Jinja2</h1>
        <p>Chega de escrever HTML dentro do Python!</p>
        <p>Agora usamos <strong>templates</strong> - arquivos HTML separados.</p>
        <nav style="font-size: 18px; line-height: 2.5;">
            <p><a href="/saudar/Maria">👋 Saudação para Maria</a></p>
            <p><a href="/saudar/João">👋 Saudação para João</a></p>
            <p><a href="/frutas">🍎 Lista de Frutas</a></p>
            <p><a href="/turma">🎓 Turma de Python</a></p>
        </nav>
        <div style="background: #fff3cd; padding: 15px; border-radius: 10px; margin-top: 20px;">
            <strong>Dica:</strong> Olhe a pasta <code>templates/</code> para ver os arquivos HTML!
        </div>
    </body>
    </html>
    """

# Isso funciona, mas imagine escrever um site inteiro assim...
# HTML misturado com Python = confusão!
#
# SOLUÇÃO: Templates! O HTML fica em arquivos separados na pasta templates/


# -----------------------------
# PARTE 2: render_template() - O básico
# -----------------------------
# render_template() carrega um arquivo HTML e envia para o navegador
# Variáveis Python são passadas como argumentos

@app.route("/saudar/<nome>")
def saudar(nome):
    """Usa o template saudacao.html"""
    agora = datetime.now()
    hora = agora.hour

    # Determinar período do dia
    if hora < 12:
        periodo = "Bom dia"
        emoji = "🌅"
        cor = "#ffeaa7"  # amarelo claro
    elif hora < 18:
        periodo = "Boa tarde"
        emoji = "☀️"
        cor = "#fab1a0"  # rosa claro
    else:
        periodo = "Boa noite"
        emoji = "🌙"
        cor = "#a29bfe"  # roxo claro

    # render_template() carrega templates/saudacao.html
    # e substitui as variáveis {{ }} pelos valores
    return render_template(
        "saudacao.html",
        nome=nome,
        hora=hora,
        mensagem_periodo=periodo,
        emoji=emoji,
        cor_fundo=cor
    )

# O que acontece:
# 1. Flask procura templates/saudacao.html
# 2. Substitui {{ nome }} pelo valor de nome
# 3. Substitui {{ hora }} pelo valor de hora
# 4. Envia o HTML completo para o navegador


# -----------------------------
# PARTE 3: {% if %} e {% for %} nos templates
# -----------------------------
# Jinja2 tem sua própria sintaxe para lógica:
#   {{ variavel }}       → mostra o valor
#   {% if condição %}    → decisão
#   {% for item in lista %} → repetição
#   {# comentário #}    → comentário (não aparece no HTML)

@app.route("/frutas")
def frutas():
    """Lista de frutas usando {% for %} no template"""
    lista_frutas = [
        {"nome": "Maçã", "preco": 5.90, "emoji": "🍎"},
        {"nome": "Banana", "preco": 3.50, "emoji": "🍌"},
        {"nome": "Uva", "preco": 8.90, "emoji": "🍇"},
        {"nome": "Manga", "preco": 4.00, "emoji": "🥭"},
        {"nome": "Morango", "preco": 12.00, "emoji": "🍓"},
    ]

    return render_template("lista_frutas.html", frutas=lista_frutas)


# ============================================================
# EXERCÍCIO 4.3 - Turma de Alunos com Template
# ============================================================
# Passe uma lista de alunos para o template alunos_template.html
# O template já tem a lógica de {% if %} para aprovado/reprovado

@app.route("/turma")
def turma():
    """Mostra a turma usando template com {% if %} e {% for %}"""
    alunos = [
        {"nome": "Maria Silva", "idade": 17, "nota": 8.5},
        {"nome": "João Pedro", "idade": 16, "nota": 6.0},
        {"nome": "Ana Santos", "idade": 17, "nota": 9.2},
        {"nome": "Carlos Lima", "idade": 18, "nota": 4.5},
        {"nome": "Beatriz Souza", "idade": 16, "nota": 7.0},
    ]

    # Calcular média da turma
    soma = sum(a["nota"] for a in alunos)
    media = soma / len(alunos)

    return render_template(
        "alunos_template.html",
        alunos=alunos,
        media_turma=f"{media:.1f}"
    )


# ============================================================
# RESUMO DA SINTAXE JINJA2
# ============================================================
#
# No arquivo .html (template):
#
# MOSTRAR VARIÁVEL:
#   {{ nome }}
#   {{ aluno.nota }}
#   {{ lista|length }}          ← filtro: tamanho da lista
#   {{ "%.2f"|format(preco) }}  ← filtro: formatar número
#
# CONDIÇÃO (if):
#   {% if nota >= 7 %}
#       <p>Aprovado!</p>
#   {% elif nota >= 5 %}
#       <p>Recuperação</p>
#   {% else %}
#       <p>Reprovado</p>
#   {% endif %}                 ← IMPORTANTE: fechar com endif!
#
# REPETIÇÃO (for):
#   {% for aluno in alunos %}
#       <p>{{ aluno.nome }}</p>
#   {% endfor %}                ← IMPORTANTE: fechar com endfor!
#
# COMENTÁRIO:
#   {# Isso não aparece no HTML #}


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: Template não encontrado
# Certifique-se de que o arquivo está em templates/
# E que o nome está correto (com extensão .html)

# ERRO 2: Esquecer o {% endif %} ou {% endfor %}
# Todo {% if %} precisa de {% endif %}
# Todo {% for %} precisa de {% endfor %}

# ERRO 3: Usar = ao invés de == no template
# {% if nota = 10 %}  ← ERRADO
# {% if nota == 10 %} ← CERTO

# ERRO 4: Esquecer de passar a variável no render_template
# Se o template usa {{ nome }} mas você não passou nome=...,
# vai aparecer vazio


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ Templates separam HTML do Python
# ✓ render_template() carrega e processa templates
# ✓ {{ variavel }} mostra valores no HTML
# ✓ {% if %} faz decisões no template
# ✓ {% for %} repete elementos no template
# ✓ Filtros como |length e |format transformam valores
# ============================================================


if __name__ == "__main__":
    print("=" * 50)
    print("  Servidor rodando!")
    print("  Abra no navegador: http://localhost:5000")
    print("  Para parar: aperte Ctrl+C no terminal")
    print("=" * 50)
    app.run(debug=True)
