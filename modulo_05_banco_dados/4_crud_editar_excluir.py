# ============================================================
# LIÇÃO 5.4 - CRUD: EDITAR E EXCLUIR (2h)
# ============================================================
# Objetivo: Completar o CRUD! Agora vamos adicionar as
#           operações de Update (editar) e Delete (excluir).
#
# Revisão do CRUD completo:
#   C = Create → /novo (POST)        ✓ Lição 5.3
#   R = Read   → / e /post/<id>      ✓ Lição 5.3
#   U = Update → /editar/<id> (POST) ← ESTA LIÇÃO
#   D = Delete → /excluir/<id> (POST) ← ESTA LIÇÃO
#
# Conceitos novos:
# - Formulário pré-preenchido com dados existentes
# - get_or_404(): buscar ou mostrar erro 404
# - Atualizar atributos e fazer commit
# - db.session.delete() para remover registros
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog_crud.db"
db = SQLAlchemy(app)


# ============================================================
# MODELO (mesmo da lição 5.3)
# ============================================================

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Post {self.id}: {self.titulo}>"


with app.app_context():
    db.create_all()

    if Post.query.count() == 0:
        posts = [
            Post(
                titulo="Meu primeiro post!",
                conteudo="Estou aprendendo CRUD - as 4 operações básicas "
                         "de qualquer sistema com banco de dados.",
            ),
            Post(
                titulo="Aprendendo a editar posts",
                conteudo="Agora eu consigo não só criar e ler, mas também "
                         "editar e excluir posts. O CRUD está completo!",
            ),
            Post(
                titulo="Python é demais!",
                conteudo="Com poucas linhas de código eu tenho um blog "
                         "completo funcionando. Isso é muito legal!",
            ),
        ]
        db.session.add_all(posts)
        db.session.commit()
        print("Posts iniciais criados!")


# ============================================================
# READ (LER): LISTAR E VER
# ============================================================

@app.route("/")
def lista_posts():
    """Lista todos os posts"""
    mensagem = request.args.get("msg")
    posts = Post.query.order_by(Post.criado_em.desc()).all()
    total = Post.query.count()
    return render_template(
        "posts_lista.html",
        posts=posts,
        total=total,
        mensagem=mensagem,
    )


@app.route("/post/<int:post_id>")
def ver_post(post_id):
    """Mostra um post específico"""
    post = Post.query.get_or_404(post_id)
    return render_template("posts_ver.html", post=post)


# ============================================================
# CREATE (CRIAR)
# ============================================================

@app.route("/novo", methods=["GET", "POST"])
def novo_post():
    """Cria um novo post"""
    if request.method == "POST":
        post = Post(
            titulo=request.form["titulo"],
            conteudo=request.form["conteudo"],
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("lista_posts", msg="Post publicado!"))

    return render_template("posts_novo.html")


# ============================================================
# UPDATE (EDITAR): O POST JÁ EXISTE, VAMOS MUDAR ELE
# ============================================================
# O formulário de edição é parecido com o de criação, mas:
# 1. Precisa buscar o post existente no banco
# 2. O formulário vem PRÉ-PREENCHIDO com os dados atuais
# 3. Ao salvar, ATUALIZAMOS o post existente (não criamos novo)
#
# Comparação:
#   CRIAR:  post = Post(titulo=...) → db.session.add(post)
#   EDITAR: post.titulo = novo_titulo → db.session.commit()
#
# Perceba: para editar, não usamos add()!
# Basta mudar os atributos e fazer commit().
# O SQLAlchemy percebe que o objeto mudou e atualiza no banco.

@app.route("/editar/<int:post_id>", methods=["GET", "POST"])
def editar_post(post_id):
    """GET: mostra formulário preenchido. POST: salva alterações."""
    # Buscar o post (ou mostrar 404)
    post = Post.query.get_or_404(post_id)

    if request.method == "POST":
        # Atualizar os atributos do post
        post.titulo = request.form["titulo"]
        post.conteudo = request.form["conteudo"]

        # Não precisa de add()! Só commit.
        db.session.commit()

        print(f"Post editado: {post.titulo}")
        return redirect(url_for("ver_post", post_id=post.id))

    # GET: mostra formulário com dados atuais
    return render_template("posts_editar.html", post=post)


# ============================================================
# DELETE (EXCLUIR): REMOVER UM POST DO BANCO
# ============================================================
# Para excluir, usamos db.session.delete(objeto).
#
# IMPORTANTE: Excluir é perigoso! Não tem "desfazer".
# Por isso usamos um confirm() no JavaScript do botão.
#
# Comparação com Módulo 4:
#   ANTES: tarefas = [t for t in tarefas if t["id"] != id]
#   AGORA: db.session.delete(post) + db.session.commit()

@app.route("/excluir/<int:post_id>", methods=["POST"])
def excluir_post(post_id):
    """Remove um post do banco de dados"""
    post = Post.query.get_or_404(post_id)
    titulo = post.titulo

    # Deletar do banco
    db.session.delete(post)
    db.session.commit()

    print(f"Post excluído: {titulo}")
    return redirect(url_for("lista_posts", msg=f"'{titulo}' excluído!"))


# ============================================================
# CRUD COMPLETO!
# ============================================================
# Agora temos as 4 operações:
#
#   Create → POST /novo         → db.session.add() + commit()
#   Read   → GET / e /post/<id> → Post.query.all() / get_or_404()
#   Update → POST /editar/<id>  → post.titulo = ... + commit()
#   Delete → POST /excluir/<id> → db.session.delete() + commit()
#
# Este padrão CRUD se repete em praticamente todos os sistemas:
# - Redes sociais (criar/ler/editar/excluir posts)
# - Lojas online (criar/ler/editar/excluir produtos)
# - Bancos (criar/ler/editar/excluir contas)
# ============================================================


# ============================================================
# EXERCÍCIO
# ============================================================
# 1. Complete o CRUD para posts (Criar, Ler, Editar, Excluir)
# 2. Teste cada operação no navegador
# 3. Pare o servidor e rode novamente - os dados persistem!
#
# DESAFIO EXTRA:
# - Adicione uma confirmação antes de excluir
# - Mostre a data da última edição em posts editados
# - Adicione um campo "publicado" (True/False) para rascunhos
# ============================================================


if __name__ == "__main__":
    print("=" * 50)
    print("  Lição 5.4 - CRUD Completo (Editar e Excluir)")
    print("  Abra no navegador: http://localhost:5000")
    print("  ")
    print("  Páginas:")
    print("    /              → Lista de posts")
    print("    /novo          → Criar novo post")
    print("    /post/1        → Ver post")
    print("    /editar/1      → Editar post")
    print("    /excluir/1     → Excluir post (POST)")
    print("  ")
    print("  Para parar: aperte Ctrl+C")
    print("=" * 50)
    app.run(debug=True)
