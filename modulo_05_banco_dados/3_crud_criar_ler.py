# ============================================================
# LIÇÃO 5.3 - CRUD: CRIAR E LER (2h)
# ============================================================
# Objetivo: Aprender o padrão mais importante do desenvolvimento
#           web: formulário → salvar no banco → mostrar na lista.
#
# CRUD é uma sigla para as 4 operações básicas de qualquer
# sistema que guarda dados:
#
#   C = Create (Criar)    → Adicionar dados novos
#   R = Read (Ler)        → Buscar e mostrar dados
#   U = Update (Atualizar) → Editar dados existentes (próxima lição)
#   D = Delete (Excluir)   → Remover dados (próxima lição)
#
# Nesta lição, vamos fazer o C e o R:
# - Formulário HTML para CRIAR um post
# - Página para LER (listar) todos os posts
# - Página para LER (ver) um post individual
#
# O PADRÃO QUE SE REPETE EM TODO LUGAR:
#   1. Usuário preenche formulário
#   2. Formulário envia dados (POST)
#   3. Python recebe e salva no banco
#   4. Python redireciona para a lista
#   5. Lista mostra os dados do banco
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog_crud.db"
db = SQLAlchemy(app)


# ============================================================
# MODELO
# ============================================================

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Post {self.id}: {self.titulo}>"


# Criar banco e dados iniciais
with app.app_context():
    db.create_all()

    if Post.query.count() == 0:
        posts_iniciais = [
            Post(
                titulo="Meu primeiro post!",
                conteudo="Estou aprendendo a criar um blog com banco de dados. "
                         "Agora meus posts ficam salvos para sempre!",
            ),
            Post(
                titulo="Aprendendo CRUD",
                conteudo="CRUD significa Create, Read, Update, Delete. "
                         "São as 4 operações básicas de qualquer sistema. "
                         "Hoje vou aprender as duas primeiras!",
            ),
        ]
        db.session.add_all(posts_iniciais)
        db.session.commit()
        print("Posts iniciais criados!")


# ============================================================
# READ (LER): LISTAR TODOS OS POSTS
# ============================================================
# Post.query.order_by(Post.criado_em.desc()) significa:
# "busque todos os posts, ordenados do mais recente pro mais antigo"
#
# Comparação com o Módulo 4 (sem banco):
#   ANTES: tarefas (lista na memória, some quando reinicia)
#   AGORA: Post.query.all() (busca do banco, permanente!)

@app.route("/")
def lista_posts():
    """Página principal: lista todos os posts"""
    mensagem = request.args.get("msg")
    posts = Post.query.order_by(Post.criado_em.desc()).all()
    total = Post.query.count()
    return render_template(
        "posts_lista.html",
        posts=posts,
        total=total,
        mensagem=mensagem,
    )


# ============================================================
# READ (LER): VER UM POST INDIVIDUAL
# ============================================================
# get_or_404(id) faz duas coisas:
# 1. Busca o post pelo ID
# 2. Se não encontrar, mostra página de erro 404
#
# É melhor que query.get(id) porque trata o erro automaticamente.

@app.route("/post/<int:post_id>")
def ver_post(post_id):
    """Mostra um post específico"""
    post = Post.query.get_or_404(post_id)
    return render_template("posts_ver.html", post=post)


# ============================================================
# CREATE (CRIAR): FORMULÁRIO + SALVAR
# ============================================================
# Esta rota faz DUAS coisas:
#
# GET /novo  → Mostra o formulário vazio
# POST /novo → Recebe os dados e salva no banco
#
# Comparação com o Módulo 4:
#   ANTES: tarefas.append(tarefa)     → salva na memória
#   AGORA: db.session.add(post)       → salva no banco
#          db.session.commit()         → confirma o salvamento
#
# O fluxo:
#   1. Usuário acessa /novo (GET) → vê o formulário
#   2. Preenche e clica "Publicar" → envia POST para /novo
#   3. Python cria o Post e salva no banco
#   4. Python redireciona para / com mensagem de sucesso

@app.route("/novo", methods=["GET", "POST"])
def novo_post():
    """GET: mostra formulário. POST: cria o post."""
    if request.method == "POST":
        # Receber dados do formulário
        titulo = request.form["titulo"]
        conteudo = request.form["conteudo"]

        # Criar o objeto Post
        post = Post(titulo=titulo, conteudo=conteudo)

        # Salvar no banco de dados
        db.session.add(post)      # Coloca na fila
        db.session.commit()       # Salva de verdade

        print(f"Novo post criado: {post.titulo} (ID: {post.id})")

        # Redirecionar para a lista com mensagem
        return redirect(url_for("lista_posts", msg="Post publicado com sucesso!"))

    return render_template("posts_novo.html")


# ============================================================
# O QUE ACONTECEU?
# ============================================================
# Antes (Módulo 4 - TaskPy):
#   - Dados ficavam em uma lista Python na memória
#   - Quando o servidor reiniciava, tudo sumia
#   - Usávamos: tarefas.append(tarefa)
#
# Agora (Módulo 5 - com banco de dados):
#   - Dados ficam salvos em um arquivo .db
#   - Quando o servidor reinicia, os dados continuam lá!
#   - Usamos: db.session.add(post) + db.session.commit()
#
# TESTE: Crie um post, pare o servidor (Ctrl+C), rode de novo.
# O post ainda está lá! Isso é a magia do banco de dados.
# ============================================================


# ============================================================
# EXERCÍCIO
# ============================================================
# 1. Crie a rota /novo com formulário para criar posts
# 2. Crie a rota / para listar todos os posts
# 3. Crie a rota /post/<id> para ver um post individual
# 4. Teste: crie 3 posts, pare o servidor, rode de novo
#    → Os posts devem continuar lá!
#
# DESAFIO EXTRA:
# - Adicione validação: título não pode estar vazio
# - Mostre quantos posts existem no total
# - Adicione um campo "autor" ao formulário
# ============================================================


if __name__ == "__main__":
    print("=" * 50)
    print("  Lição 5.3 - CRUD: Criar e Ler")
    print("  Abra no navegador: http://localhost:5000")
    print("  ")
    print("  Páginas:")
    print("    /        → Lista de posts")
    print("    /novo    → Criar novo post")
    print("    /post/1  → Ver post individual")
    print("  ")
    print("  Para parar: aperte Ctrl+C")
    print("=" * 50)
    app.run(debug=True)
