# ============================================================
# LIÇÃO 5.1 - O QUE É UM BANCO DE DADOS? (2h)
# ============================================================
# Objetivo: Entender o que é um banco de dados e criar o
#           primeiro banco usando Flask-SQLAlchemy.
#
# Até agora, nossos dados ficavam na memória do programa.
# Quando o servidor parava, tudo sumia! Um banco de dados
# resolve isso: ele guarda os dados em um arquivo permanente.
#
# Analogia: Um banco de dados é como uma planilha super
# organizada. Cada TABELA é uma aba. Cada LINHA é uma entrada.
# Cada COLUNA é um campo. Mas diferente de uma planilha, o
# banco consegue guardar milhões de linhas e encontrar
# qualquer coisa em milissegundos.
#
# Vamos usar SQLite: um banco de dados que fica em UM arquivo
# só. Não precisa instalar nada além do Flask-SQLAlchemy!
# ============================================================

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


# ============================================================
# CONFIGURAÇÃO DO BANCO DE DADOS
# ============================================================
# Esta linha diz ao Flask ONDE guardar o banco de dados.
# "sqlite:///alunos.db" significa: use SQLite e crie um
# arquivo chamado "alunos.db" na mesma pasta.
#
# É como dizer: "Guarde minha planilha neste arquivo."

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///alunos.db"

# Cria o objeto que conecta Flask ao banco de dados
db = SQLAlchemy(app)


# ============================================================
# MODELO: A "PLANTA" DA TABELA
# ============================================================
# Um modelo é uma classe Python que descreve uma tabela.
# Cada atributo da classe vira uma COLUNA na tabela.
# Cada objeto criado a partir da classe vira uma LINHA.
#
# Pense assim:
#   Classe = desenho da tabela (quais colunas tem)
#   Objeto = uma linha preenchida com dados
#
# Comparação com o Módulo 2 (dicionário):
#   Antes:  aluno = {"nome": "Maria", "idade": 17}
#   Agora:  aluno = Aluno(nome="Maria", idade=17)
#
# A diferença? O banco de dados LEMBRA o aluno para sempre!

class Aluno(db.Model):
    # Cada coluna tem um tipo (String, Integer, DateTime...)
    id = db.Column(db.Integer, primary_key=True)          # Identificador único
    nome = db.Column(db.String(100), nullable=False)       # Nome (obrigatório)
    idade = db.Column(db.Integer, nullable=False)          # Idade (obrigatório)
    curso = db.Column(db.String(100), default="Python")    # Curso (padrão: Python)
    criado_em = db.Column(db.DateTime, default=datetime.now)  # Data de cadastro

    def __repr__(self):
        """Como o aluno aparece no terminal (para debug)"""
        return f"<Aluno {self.nome}>"


# ============================================================
# O QUE SIGNIFICAM OS TIPOS DE COLUNA?
# ============================================================
#
# db.Integer       → Número inteiro (1, 2, 3...)
# db.String(100)   → Texto com no máximo 100 caracteres
# db.Text          → Texto longo (sem limite prático)
# db.DateTime      → Data e hora
# db.Boolean       → Verdadeiro ou Falso
# db.Float         → Número decimal (3.14, 9.99...)
#
# Opções importantes:
#   primary_key=True  → Identificador único (como CPF)
#   nullable=False    → Campo obrigatório
#   default=valor     → Valor padrão se não informar
# ============================================================


# ============================================================
# CRIAR O BANCO E ADICIONAR DADOS INICIAIS
# ============================================================

with app.app_context():
    # Cria todas as tabelas (se não existirem)
    db.create_all()
    print("Banco de dados criado!")

    # Só adiciona dados se a tabela estiver vazia
    if Aluno.query.count() == 0:
        # Criando objetos Aluno (cada um será uma linha na tabela)
        alunos_iniciais = [
            Aluno(nome="Maria Silva", idade=17, curso="Python Backend"),
            Aluno(nome="João Santos", idade=16, curso="Python Backend"),
            Aluno(nome="Ana Oliveira", idade=18, curso="Web Design"),
            Aluno(nome="Pedro Costa", idade=17, curso="Python Backend"),
            Aluno(nome="Lucia Ferreira", idade=16, curso="Data Science"),
        ]

        # db.session.add_all() = "coloque todos na fila para salvar"
        db.session.add_all(alunos_iniciais)

        # db.session.commit() = "agora salve de verdade no banco"
        db.session.commit()

        print(f"{len(alunos_iniciais)} alunos adicionados!")
    else:
        print(f"Banco já tem {Aluno.query.count()} alunos.")


# ============================================================
# CONSULTAS (QUERIES): BUSCANDO DADOS NO BANCO
# ============================================================
# Agora que temos dados, vamos buscar!
# Isso é o equivalente a "pesquisar na planilha".

with app.app_context():
    print("\n" + "=" * 50)
    print("EXEMPLOS DE CONSULTAS")
    print("=" * 50)

    # 1. Buscar TODOS os alunos
    todos = Aluno.query.all()
    print(f"\nTodos os alunos ({len(todos)}):")
    for aluno in todos:
        print(f"  - {aluno.nome}, {aluno.idade} anos, {aluno.curso}")

    # 2. Buscar UM aluno pelo ID
    primeiro = Aluno.query.get(1)
    print(f"\nPrimeiro aluno: {primeiro.nome}")

    # 3. Filtrar alunos (WHERE)
    alunos_python = Aluno.query.filter_by(curso="Python Backend").all()
    print(f"\nAlunos de Python Backend ({len(alunos_python)}):")
    for aluno in alunos_python:
        print(f"  - {aluno.nome}")

    # 4. Filtrar com condição (maior que)
    maiores = Aluno.query.filter(Aluno.idade >= 17).all()
    print(f"\nAlunos com 17+ anos ({len(maiores)}):")
    for aluno in maiores:
        print(f"  - {aluno.nome}, {aluno.idade} anos")

    # 5. Ordenar resultados
    por_nome = Aluno.query.order_by(Aluno.nome).all()
    print(f"\nAlunos em ordem alfabética:")
    for aluno in por_nome:
        print(f"  - {aluno.nome}")

    # 6. Contar registros
    total = Aluno.query.count()
    print(f"\nTotal de alunos: {total}")


# ============================================================
# ROTA: MOSTRAR ALUNOS NO NAVEGADOR
# ============================================================

@app.route("/")
def lista_alunos():
    """Mostra todos os alunos em uma página web"""
    alunos = Aluno.query.order_by(Aluno.nome).all()
    total = Aluno.query.count()
    return render_template("alunos.html", alunos=alunos, total=total)


@app.route("/curso/<nome_curso>")
def alunos_por_curso(nome_curso):
    """Filtra alunos por curso"""
    alunos = Aluno.query.filter_by(curso=nome_curso).all()
    total = len(alunos)
    return render_template(
        "alunos.html",
        alunos=alunos,
        total=total,
        filtro=nome_curso,
    )


# ============================================================
# EXERCÍCIO
# ============================================================
# 1. Crie uma tabela "Aluno" com nome, idade, curso
# 2. Adicione 5 alunos
# 3. Consulte todos os alunos
# 4. Filtre por curso
# 5. Acesse http://localhost:5000 para ver a lista no navegador
#
# DESAFIO EXTRA:
# - Adicione um campo "email" ao modelo Aluno
# - Crie uma rota /aluno/<id> que mostra os detalhes de um aluno
# - Adicione mais cursos e filtre por curso na URL
# ============================================================


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  Lição 5.1 - Introdução a Bancos de Dados")
    print("  Abra no navegador: http://localhost:5000")
    print("  ")
    print("  Páginas:")
    print("    /                    → Todos os alunos")
    print("    /curso/Python Backend → Filtrar por curso")
    print("  ")
    print("  Para parar: aperte Ctrl+C")
    print("=" * 50)
    app.run(debug=True)
