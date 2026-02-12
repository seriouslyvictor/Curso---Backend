# ============================================================
# LIÇÃO 5.2 - MODELOS: TABELAS COMO CLASSES PYTHON (2h)
# ============================================================
# Objetivo: Entender que cada modelo é uma classe Python,
#           cada coluna é um atributo, e cada linha é um objeto.
#
# No Módulo 2, usávamos dicionários para guardar dados:
#   post = {"titulo": "Meu Post", "conteudo": "..."}
#
# Agora usamos CLASSES, e o banco de dados lembra tudo:
#   post = Post(titulo="Meu Post", conteudo="...")
#   db.session.add(post)
#   db.session.commit()  # Salvo para sempre!
#
# Conceitos desta lição:
# - db.Model: base para todos os modelos
# - db.Column: define uma coluna (campo)
# - Tipos: String, Integer, Text, DateTime
# - primary_key: identificador único
# - default: valor padrão
# - nullable: campo obrigatório ou não
# ============================================================

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog_posts.db"
db = SQLAlchemy(app)


# ============================================================
# MODELO POST (Postagem do Blog)
# ============================================================
# Este modelo será a base do nosso blog!
# Cada Post tem: id, título, conteúdo e data de criação.
#
# Comparação com dicionário (Módulo 2):
#
#   ANTES (dicionário - some quando o programa fecha):
#   post = {
#       "id": 1,
#       "titulo": "Meu primeiro post",
#       "conteudo": "Olá mundo!",
#       "criado_em": "2025-01-15 10:00"
#   }
#
#   AGORA (modelo - fica salvo no banco para sempre):
#   class Post(db.Model):
#       id = db.Column(db.Integer, primary_key=True)
#       titulo = db.Column(db.String(200), nullable=False)
#       conteudo = db.Column(db.Text, nullable=False)
#       criado_em = db.Column(db.DateTime, default=datetime.now)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Post {self.id}: {self.titulo}>"


# ============================================================
# O QUE CADA PARTE SIGNIFICA?
# ============================================================
#
# class Post(db.Model):
#   ↑ "Post" é o nome da tabela (em minúsculas: "post")
#   ↑ "db.Model" diz que esta classe é uma tabela do banco
#
# id = db.Column(db.Integer, primary_key=True)
#   ↑ Identificador único, gerado automaticamente
#   ↑ Como o número da carteirinha: cada aluno tem um diferente
#
# titulo = db.Column(db.String(200), nullable=False)
#   ↑ Texto com no máximo 200 caracteres
#   ↑ nullable=False = OBRIGATÓRIO (não pode ficar vazio)
#
# conteudo = db.Column(db.Text, nullable=False)
#   ↑ Texto longo, sem limite de tamanho
#   ↑ Perfeito para o corpo de um post
#
# criado_em = db.Column(db.DateTime, default=datetime.now)
#   ↑ Data e hora
#   ↑ default=datetime.now = se não informar, usa a hora atual
# ============================================================


# ============================================================
# CRIAR BANCO E DADOS INICIAIS
# ============================================================

with app.app_context():
    db.create_all()

    if Post.query.count() == 0:
        posts_iniciais = [
            Post(
                titulo="Bem-vindo ao meu blog!",
                conteudo="Este é o meu primeiro post. Estou aprendendo a "
                         "criar um blog com Python e Flask. É incrível ver "
                         "como poucas linhas de código criam algo tão legal!",
            ),
            Post(
                titulo="O que aprendi sobre bancos de dados",
                conteudo="Bancos de dados são como planilhas super poderosas. "
                         "Eles guardam informações permanentemente e conseguem "
                         "buscar qualquer coisa muito rápido. Estou usando "
                         "SQLite, que guarda tudo em um arquivo só!",
            ),
            Post(
                titulo="Python é demais!",
                conteudo="Comecei o curso sem saber nada de programação. "
                         "Agora já sei criar sites com Flask e guardar dados "
                         "em bancos de dados. Cada módulo me surpreende mais!",
            ),
        ]
        db.session.add_all(posts_iniciais)
        db.session.commit()
        print(f"{len(posts_iniciais)} posts criados!")


# ============================================================
# CONSULTAS NO SHELL (para testar no terminal)
# ============================================================
# Você pode testar consultas no terminal Python:
#
# >>> from 2_modelos_sqlalchemy import app, db, Post
# >>> with app.app_context():
# ...     # Buscar todos
# ...     posts = Post.query.all()
# ...     print(posts)
# ...
# ...     # Buscar por ID
# ...     post = Post.query.get(1)
# ...     print(post.titulo)
# ...
# ...     # Adicionar novo post
# ...     novo = Post(titulo="Novo post", conteudo="Conteúdo aqui")
# ...     db.session.add(novo)
# ...     db.session.commit()
# ============================================================


with app.app_context():
    print("\n" + "=" * 50)
    print("POSTS NO BANCO DE DADOS")
    print("=" * 50)

    posts = Post.query.all()
    for post in posts:
        print(f"\n[{post.id}] {post.titulo}")
        print(f"    Criado em: {post.criado_em.strftime('%d/%m/%Y %H:%M')}")
        print(f"    {post.conteudo[:80]}...")


# ============================================================
# ROTAS
# ============================================================

@app.route("/")
def lista_posts():
    """Lista todos os posts do blog"""
    posts = Post.query.order_by(Post.criado_em.desc()).all()
    return render_template("posts_modelo.html", posts=posts)


@app.route("/post/<int:post_id>")
def ver_post(post_id):
    """Mostra um post específico"""
    # get_or_404: busca pelo ID. Se não encontrar, mostra erro 404.
    post = Post.query.get_or_404(post_id)
    return render_template("posts_modelo.html", posts=[post], destaque=True)


# ============================================================
# EXERCÍCIO
# ============================================================
# 1. Crie o modelo Post com id, titulo, conteudo, criado_em
# 2. Adicione posts pelo shell do Python
# 3. Consulte e mostre os posts no navegador
#
# DESAFIO EXTRA:
# - Adicione um campo "autor" ao modelo
# - Crie uma rota /post/<id> que mostra um post individual
# - Ordene os posts do mais recente para o mais antigo
# ============================================================


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  Lição 5.2 - Modelos como Classes Python")
    print("  Abra no navegador: http://localhost:5000")
    print("  ")
    print("  Páginas:")
    print("    /          → Lista de posts")
    print("    /post/1    → Ver post individual")
    print("  ")
    print("  Para parar: aperte Ctrl+C")
    print("=" * 50)
    app.run(debug=True)
