# ============================================================
# LIÇÃO 4.5 - FORMULÁRIOS E REQUISIÇÕES POST
# ============================================================
# Objetivo: Receber dados do usuário pelo navegador
# Conceito: GET = pedir página, POST = enviar dados
#
# Analogia: GET é pedir o cardápio no restaurante.
#           POST é fazer o pedido da comida.
#
# Arquivos usados:
# - templates/base.html       → layout base
# - templates/formulario.html  → formulário de cadastro
# - templates/resultado.html   → confirmação
# - templates/enquete.html     → enquete com votação
# - static/estilo.css          → estilos
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)


# "Banco de dados" temporário (lista na memória)
# Quando o servidor reiniciar, os dados somem!
# No Módulo 5 vamos usar um banco de dados de verdade.
cadastros = []
votos = {"Python": 0, "JavaScript": 0, "Java": 0, "C#": 0}


@app.context_processor
def dados_globais():
    return {"ano": datetime.now().year}


# -----------------------------
# PARTE 1: GET vs POST
# -----------------------------
# GET  → navegador PEDE uma página (clicar em link, digitar URL)
# POST → navegador ENVIA dados (enviar formulário)
#
# Quando você digita www.google.com → GET
# Quando você faz login → POST (envia usuário e senha)


@app.route("/")
def inicio():
    return """
    <html>
    <body style="font-family: Arial; max-width: 700px; margin: 50px auto;">
        <h1>📝 Lição 4.5 - Formulários e POST</h1>
        <p>Agora o usuário pode <strong>enviar dados</strong> para o servidor!</p>
        <nav style="font-size: 18px; line-height: 2.5;">
            <p><a href="/cadastro">📋 Formulário de Cadastro</a></p>
            <p><a href="/enquete">🗳️ Enquete (votação)</a></p>
            <p><a href="/calculadora">🔢 Calculadora Web</a></p>
        </nav>
    </body>
    </html>
    """


# -----------------------------
# PARTE 2: Formulário com POST
# -----------------------------

# Rota GET: mostra o formulário
@app.route("/cadastro")
def cadastro():
    """Mostra o formulário de cadastro"""
    return render_template("formulario.html", cadastros=cadastros)


# Rota POST: recebe os dados do formulário
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    """Recebe e processa os dados do formulário"""
    # request.form contém os dados enviados pelo formulário
    # Os nomes vêm do atributo "name" no HTML
    dados = {
        "nome": request.form["nome"],
        "idade": request.form["idade"],
        "email": request.form["email"],
        "curso": request.form["curso"],
        "mensagem": request.form.get("mensagem", ""),  # .get() para campos opcionais
    }

    # Salvar na nossa "lista banco de dados"
    cadastros.append(dados)

    # Mostrar no terminal do servidor (para debug)
    print(f"Novo cadastro: {dados['nome']} ({dados['email']})")

    # Redirecionar para página de confirmação
    # redirect() manda o navegador para outra página
    # url_for() gera a URL a partir do nome da função
    return render_template("resultado.html", dados=dados)


# O que aconteceu?
# 1. Usuário preenche o formulário e clica "Enviar"
# 2. Navegador envia os dados via POST para /cadastrar
# 3. Flask recebe os dados em request.form
# 4. Python processa e salva os dados
# 5. Flask mostra a página de confirmação


# -----------------------------
# PARTE 3: Mesma rota para GET e POST
# -----------------------------
# Às vezes, queremos que a mesma URL mostre o formulário (GET)
# e receba os dados (POST)

@app.route("/enquete", methods=["GET", "POST"])
def enquete():
    """Enquete: mostra formulário E processa votos"""
    if request.method == "POST":
        # Chegou um voto!
        linguagem = request.form["linguagem"]

        # Mapear valor do formulário para nome bonito
        nomes = {
            "python": "Python",
            "javascript": "JavaScript",
            "java": "Java",
            "csharp": "C#",
        }

        nome = nomes.get(linguagem, linguagem)
        if nome in votos:
            votos[nome] += 1

    # Tanto GET quanto POST mostram a mesma página (com resultados atualizados)
    total = sum(votos.values())
    return render_template("enquete.html", votos=votos, total_votos=total)


# Diferença importante:
# methods=["GET"]         → só aceita GET (padrão)
# methods=["POST"]        → só aceita POST
# methods=["GET", "POST"] → aceita ambos


# ============================================================
# EXERCÍCIO 4.5 - Calculadora Web
# ============================================================
# Uma calculadora que recebe dois números pelo formulário

@app.route("/calculadora", methods=["GET", "POST"])
def calculadora():
    """Calculadora web com formulário"""
    resultado = None
    erro = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacao = request.form["operacao"]

            if operacao == "somar":
                resultado = f"{num1} + {num2} = {num1 + num2}"
            elif operacao == "subtrair":
                resultado = f"{num1} - {num2} = {num1 - num2}"
            elif operacao == "multiplicar":
                resultado = f"{num1} × {num2} = {num1 * num2}"
            elif operacao == "dividir":
                if num2 == 0:
                    erro = "Não é possível dividir por zero!"
                else:
                    resultado = f"{num1} ÷ {num2} = {num1 / num2:.2f}"
        except ValueError:
            erro = "Por favor, digite números válidos."

    return f"""
    <html>
    <body style="font-family: Arial; max-width: 500px; margin: 50px auto; padding: 20px;">
        <h1>🔢 Calculadora Web</h1>

        <div style="background: white; padding: 25px; border-radius: 10px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <form method="POST">
                <div style="margin-bottom: 15px;">
                    <label style="display: block; font-weight: bold; margin-bottom: 5px;">
                        Primeiro número:
                    </label>
                    <input type="number" name="num1" step="any" required
                           style="width: 100%; padding: 10px; border: 1px solid #ddd;
                                  border-radius: 5px; box-sizing: border-box;">
                </div>

                <div style="margin-bottom: 15px;">
                    <label style="display: block; font-weight: bold; margin-bottom: 5px;">
                        Operação:
                    </label>
                    <select name="operacao" style="width: 100%; padding: 10px;
                            border: 1px solid #ddd; border-radius: 5px;">
                        <option value="somar">+ Somar</option>
                        <option value="subtrair">- Subtrair</option>
                        <option value="multiplicar">× Multiplicar</option>
                        <option value="dividir">÷ Dividir</option>
                    </select>
                </div>

                <div style="margin-bottom: 15px;">
                    <label style="display: block; font-weight: bold; margin-bottom: 5px;">
                        Segundo número:
                    </label>
                    <input type="number" name="num2" step="any" required
                           style="width: 100%; padding: 10px; border: 1px solid #ddd;
                                  border-radius: 5px; box-sizing: border-box;">
                </div>

                <button type="submit" style="background: #3498db; color: white; border: none;
                        padding: 12px 25px; border-radius: 5px; font-size: 16px; cursor: pointer;
                        width: 100%;">
                    Calcular
                </button>
            </form>

            {"" if not resultado else f'''
            <div style="background: #d4edda; padding: 15px; border-radius: 5px;
                        margin-top: 15px; text-align: center; font-size: 20px;">
                <strong>{resultado}</strong>
            </div>
            '''}

            {"" if not erro else f'''
            <div style="background: #f8d7da; padding: 15px; border-radius: 5px;
                        margin-top: 15px; text-align: center; color: #721c24;">
                <strong>{erro}</strong>
            </div>
            '''}
        </div>

        <p style="text-align: center; margin-top: 20px;"><a href="/">← Voltar</a></p>
    </body>
    </html>
    """


# ============================================================
# RESUMO: request.form vs request.args
# ============================================================
#
# request.form → dados de formulário POST
#   Dados ficam "escondidos" no corpo da requisição
#   Usado para: login, cadastro, envio de dados
#
# request.args → dados da URL (query string)
#   Dados ficam visíveis na URL: /busca?q=python
#   Usado para: busca, filtros, navegação
#
# Exemplo:
#   URL: /busca?q=python&pagina=2
#   request.args["q"]       → "python"
#   request.args["pagina"]  → "2"


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: Esquecer methods=["POST"] na rota
# @app.route("/cadastrar")  ← Só aceita GET!
# @app.route("/cadastrar", methods=["POST"])  ← Aceita POST

# ERRO 2: Atributo "name" faltando no HTML
# <input type="text">              ← Sem name, Flask não recebe!
# <input type="text" name="nome">  ← Correto

# ERRO 3: Usar request.form em rota GET
# request.form só tem dados quando o método é POST

# ERRO 4: Confundir action e method no form
# action = PARA ONDE enviar (URL)
# method = COMO enviar (GET ou POST)


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ GET pede páginas, POST envia dados
# ✓ method="POST" no formulário HTML
# ✓ request.form recebe dados do formulário no Flask
# ✓ methods=["GET", "POST"] aceita ambos na mesma rota
# ✓ redirect() e url_for() para redirecionar
# ✓ request.method verifica se é GET ou POST
# ✓ Validação de dados no servidor é importante
# ============================================================


if __name__ == "__main__":
    print("=" * 50)
    print("  Servidor rodando!")
    print("  Abra no navegador: http://localhost:5000")
    print("  Para parar: aperte Ctrl+C no terminal")
    print("=" * 50)
    app.run(debug=True)
