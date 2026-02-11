# ============================================================
# LIÇÃO 4.2 - ROTAS E PÁGINAS DINÂMICAS
# ============================================================
# Objetivo: Criar páginas que mudam baseado no que o usuário acessa
# Conceito: Rotas dinâmicas capturam partes da URL como variáveis
# ============================================================

from flask import Flask

app = Flask(__name__)


# -----------------------------
# PARTE 1: Relembrando rotas fixas
# -----------------------------
# Na lição anterior, cada rota era fixa:

@app.route("/")
def inicio():
    return """
    <html>
    <body style="font-family: Arial; max-width: 700px; margin: 50px auto;">
        <h1>🌐 Lição 4.2 - Rotas Dinâmicas</h1>
        <nav style="font-size: 18px; line-height: 2.5;">
            <p><a href="/usuario/Maria">👤 Perfil da Maria</a></p>
            <p><a href="/usuario/João">👤 Perfil do João</a></p>
            <p><a href="/usuario/Ana">👤 Perfil da Ana</a></p>
            <p><a href="/produto/1">📦 Produto 1</a></p>
            <p><a href="/produto/2">📦 Produto 2</a></p>
            <p><a href="/produto/3">📦 Produto 3</a></p>
            <p><a href="/tabuada/7">🔢 Tabuada do 7</a></p>
            <p><a href="/cores">🎨 Lista de Cores</a></p>
            <p><a href="/alunos">🎓 Lista de Alunos</a></p>
        </nav>
    </body>
    </html>
    """


# -----------------------------
# PARTE 2: Rotas dinâmicas com variáveis
# -----------------------------
# <nome> na rota captura parte da URL e passa como parâmetro
# É como uma variável que vem da URL!

@app.route("/usuario/<nome>")
def perfil_usuario(nome):
    """Mostra o perfil de qualquer usuário"""
    return f"""
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 50px auto;">
        <h1>👤 Perfil de {nome}</h1>
        <div style="background: #f0f0f0; padding: 20px; border-radius: 10px;">
            <p><strong>Nome:</strong> {nome}</p>
            <p><strong>Status:</strong> Estudante de Python</p>
            <p><strong>Nível:</strong> Aprendendo Flask!</p>
        </div>
        <p style="margin-top: 20px;">
            Tente trocar o nome na URL!<br>
            Exemplo: <code>/usuario/SeuNome</code>
        </p>
        <p><a href="/">← Voltar</a></p>
    </body>
    </html>
    """

# Teste: acesse /usuario/Maria, /usuario/João, /usuario/SeuNome
# A mesma rota funciona para qualquer nome!


# -----------------------------
# PARTE 3: Variáveis com tipo específico
# -----------------------------
# <int:numero> aceita apenas números inteiros
# Isso evita erros!

@app.route("/produto/<int:produto_id>")
def produto(produto_id):
    """Mostra detalhes de um produto pelo ID"""
    # Simulando um "banco de dados" com dicionário
    produtos = {
        1: {"nome": "Camiseta Python", "preco": 49.90, "cor": "#306998"},
        2: {"nome": "Caneca Flask", "preco": 29.90, "cor": "#44b78b"},
        3: {"nome": "Adesivo GitHub", "preco": 9.90, "cor": "#333"},
    }

    if produto_id in produtos:
        p = produtos[produto_id]
        return f"""
        <html>
        <body style="font-family: Arial; max-width: 600px; margin: 50px auto;">
            <h1>📦 {p['nome']}</h1>
            <div style="background: {p['cor']}; color: white; padding: 30px;
                        border-radius: 10px; text-align: center;">
                <p style="font-size: 24px;">{p['nome']}</p>
                <p style="font-size: 32px; font-weight: bold;">R$ {p['preco']:.2f}</p>
            </div>
            <p><a href="/">← Voltar</a></p>
        </body>
        </html>
        """
    else:
        return f"""
        <html>
        <body style="font-family: Arial; max-width: 600px; margin: 50px auto;">
            <h1>❌ Produto não encontrado</h1>
            <p>O produto {produto_id} não existe.</p>
            <p>Temos produtos: 1, 2 e 3.</p>
            <p><a href="/">← Voltar</a></p>
        </body>
        </html>
        """, 404


# Tipos disponíveis para variáveis na URL:
# <string:nome>  → texto (padrão, não precisa escrever "string:")
# <int:numero>   → número inteiro
# <float:valor>  → número decimal
# <path:caminho> → texto que pode conter barras /


# -----------------------------
# PARTE 4: Múltiplas variáveis na rota
# -----------------------------

@app.route("/saudar/<nome>/<int:idade>")
def saudar(nome, idade):
    """Saudação personalizada com nome e idade"""
    # Mensagem muda baseada na idade
    if idade < 13:
        categoria = "criança"
        emoji = "🧒"
    elif idade < 18:
        categoria = "adolescente"
        emoji = "🧑"
    else:
        categoria = "adulto"
        emoji = "🧑‍💼"

    return f"""
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 50px auto;">
        <h1>{emoji} Olá, {nome}!</h1>
        <p>Você tem {idade} anos e é {categoria}.</p>
        <p>Tente: <code>/saudar/SeuNome/SuaIdade</code></p>
        <p><a href="/">← Voltar</a></p>
    </body>
    </html>
    """


# -----------------------------
# PARTE 5: Gerando conteúdo dinâmico com Python
# -----------------------------
# O poder do Flask: usar TODA a lógica do Python para gerar HTML!

@app.route("/tabuada/<int:numero>")
def tabuada(numero):
    """Gera a tabuada de qualquer número"""
    linhas = ""
    for i in range(1, 11):
        resultado = numero * i
        linhas += f"<tr><td>{numero} × {i}</td><td>=</td><td><strong>{resultado}</strong></td></tr>\n"

    return f"""
    <html>
    <body style="font-family: Arial; max-width: 400px; margin: 50px auto;">
        <h1>🔢 Tabuada do {numero}</h1>
        <table style="width: 100%; font-size: 20px; border-collapse: collapse;">
            {linhas}
        </table>
        <p style="margin-top: 20px;">
            Tente outros números: <code>/tabuada/5</code>, <code>/tabuada/12</code>
        </p>
        <p><a href="/">← Voltar</a></p>
    </body>
    </html>
    """


# -----------------------------
# PARTE 6: Listas e loops no HTML
# -----------------------------

@app.route("/cores")
def cores():
    """Mostra uma lista de cores gerada com Python"""
    lista_cores = [
        ("Vermelho", "#e74c3c"),
        ("Azul", "#3498db"),
        ("Verde", "#2ecc71"),
        ("Amarelo", "#f1c40f"),
        ("Roxo", "#9b59b6"),
        ("Laranja", "#e67e22"),
    ]

    itens = ""
    for nome, codigo in lista_cores:
        itens += f"""
        <div style="display: flex; align-items: center; margin: 10px 0;">
            <div style="width: 50px; height: 50px; background: {codigo};
                        border-radius: 50%; margin-right: 15px;"></div>
            <span style="font-size: 18px;">{nome} ({codigo})</span>
        </div>
        """

    return f"""
    <html>
    <body style="font-family: Arial; max-width: 500px; margin: 50px auto;">
        <h1>🎨 Catálogo de Cores</h1>
        {itens}
        <p><a href="/">← Voltar</a></p>
    </body>
    </html>
    """


# ============================================================
# EXERCÍCIO 4.2 - Lista de Alunos Dinâmica
# ============================================================
# Crie uma rota /alunos que mostra uma tabela de alunos
# E uma rota /aluno/<nome> que mostra detalhes de um aluno

# Dados dos alunos (nosso "banco de dados" por enquanto)
alunos = {
    "maria": {"nome": "Maria Silva", "idade": 17, "curso": "Python Backend", "nota": 8.5},
    "joao": {"nome": "João Pedro", "idade": 16, "curso": "Python Backend", "nota": 7.0},
    "ana": {"nome": "Ana Santos", "idade": 17, "curso": "Python Backend", "nota": 9.2},
    "carlos": {"nome": "Carlos Lima", "idade": 18, "curso": "Python Backend", "nota": 6.8},
}


@app.route("/alunos")
def lista_alunos():
    """Lista todos os alunos"""
    linhas = ""
    for chave, aluno in alunos.items():
        linhas += f"""
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #ddd;">
                <a href="/aluno/{chave}">{aluno['nome']}</a>
            </td>
            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{aluno['idade']}</td>
            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{aluno['nota']}</td>
        </tr>
        """

    return f"""
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 50px auto;">
        <h1>🎓 Lista de Alunos</h1>
        <table style="width: 100%; border-collapse: collapse;">
            <tr style="background: #3498db; color: white;">
                <th style="padding: 10px; text-align: left;">Nome</th>
                <th style="padding: 10px; text-align: left;">Idade</th>
                <th style="padding: 10px; text-align: left;">Nota</th>
            </tr>
            {linhas}
        </table>
        <p>Clique no nome para ver detalhes!</p>
        <p><a href="/">← Voltar</a></p>
    </body>
    </html>
    """


@app.route("/aluno/<chave>")
def detalhe_aluno(chave):
    """Mostra detalhes de um aluno"""
    if chave in alunos:
        a = alunos[chave]
        # Determinar situação
        if a["nota"] >= 7:
            situacao = "✅ APROVADO"
            cor = "#2ecc71"
        elif a["nota"] >= 5:
            situacao = "⚠️ RECUPERAÇÃO"
            cor = "#f39c12"
        else:
            situacao = "❌ REPROVADO"
            cor = "#e74c3c"

        return f"""
        <html>
        <body style="font-family: Arial; max-width: 500px; margin: 50px auto;">
            <h1>👤 {a['nome']}</h1>
            <div style="background: #f8f9fa; padding: 20px; border-radius: 10px;">
                <p><strong>Idade:</strong> {a['idade']} anos</p>
                <p><strong>Curso:</strong> {a['curso']}</p>
                <p><strong>Nota:</strong> {a['nota']}</p>
                <p style="color: {cor}; font-size: 20px; font-weight: bold;">
                    {situacao}
                </p>
            </div>
            <p><a href="/alunos">← Voltar para lista</a></p>
        </body>
        </html>
        """
    else:
        return f"""
        <html>
        <body style="font-family: Arial; max-width: 500px; margin: 50px auto;">
            <h1>❌ Aluno não encontrado</h1>
            <p>Não existe aluno com a chave "{chave}".</p>
            <p><a href="/alunos">← Ver todos os alunos</a></p>
        </body>
        </html>
        """, 404


# ============================================================
# DESAFIO EXTRA - Conversor de Temperatura
# ============================================================

@app.route("/converter/<float:celsius>")
def converter_temperatura(celsius):
    """Converte Celsius para Fahrenheit e Kelvin"""
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    return f"""
    <html>
    <body style="font-family: Arial; max-width: 500px; margin: 50px auto;">
        <h1>🌡️ Conversor de Temperatura</h1>
        <div style="background: #ecf0f1; padding: 20px; border-radius: 10px;
                    text-align: center;">
            <p style="font-size: 24px;">{celsius}°C</p>
            <p style="font-size: 20px;">= {fahrenheit:.1f}°F</p>
            <p style="font-size: 20px;">= {kelvin:.1f} K</p>
        </div>
        <p>Tente: <code>/converter/100.0</code>, <code>/converter/0.0</code></p>
        <p><a href="/">← Voltar</a></p>
    </body>
    </html>
    """


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: Esquecer o parâmetro na função
# @app.route("/usuario/<nome>")
# def perfil():  ← ERRO! Falta o parâmetro 'nome'
# Correto: def perfil(nome):

# ERRO 2: Tipo errado na URL
# @app.route("/produto/<int:id>")
# Se acessar /produto/abc → erro 404 (não é inteiro)

# ERRO 3: Esquecer que Python diferencia maiúsculas
# /usuario/Maria e /usuario/maria são rotas DIFERENTES


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ <variavel> na rota captura partes da URL
# ✓ <int:variavel> aceita apenas números inteiros
# ✓ <float:variavel> aceita números decimais
# ✓ Múltiplas variáveis na mesma rota são possíveis
# ✓ Python gera HTML dinâmico (loops, condições)
# ✓ Uma rota dinâmica substitui infinitas rotas fixas
# ============================================================


if __name__ == "__main__":
    print("=" * 50)
    print("  Servidor rodando!")
    print("  Abra no navegador: http://localhost:5000")
    print("  Para parar: aperte Ctrl+C no terminal")
    print("=" * 50)
    app.run(debug=True)
