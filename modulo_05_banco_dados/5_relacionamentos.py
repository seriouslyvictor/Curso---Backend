# ============================================================
# LIÇÃO 5.5 - RELACIONAMENTOS ENTRE DADOS (2h)
# ============================================================
# Objetivo: Aprender como diferentes tabelas se conectam.
#
# No Instagram, cada post pertence a UM usuário, mas cada
# usuário tem MUITOS posts. Isso é um RELACIONAMENTO.
#
# No nosso blog, cada post pertence a UMA categoria, mas
# cada categoria tem MUITOS posts. Mesmo padrão!
#
# Tipos de relacionamento:
#   Um-para-Muitos (1:N) → Uma categoria tem muitos posts
#   Muitos-para-Um (N:1) → Muitos posts pertencem a uma categoria
#
# Como funciona no banco de dados:
#   - A tabela Post ganha uma coluna "categoria_id"
#   - Essa coluna guarda o ID da categoria
#   - Isso é chamado de CHAVE ESTRANGEIRA (Foreign Key)
#
# Analogia: É como o código da cidade no endereço.
# Você não escreve "São Paulo" toda vez, só o código "SP".
# O banco sabe que "SP" = "São Paulo" pela tabela de cidades.
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog_categorias.db"
db = SQLAlchemy(app)


# ============================================================
# MODELO: CATEGORIA
# ============================================================
# Uma categoria é simples: tem um id e um nome.
# O campo "posts" não é uma coluna real no banco!
# É um atalho do SQLAlchemy para acessar os posts da categoria.

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)

    # relationship() cria um atalho: categoria.posts
    # backref="categoria" cria o atalho inverso: post.categoria
    posts = db.relationship("Post", backref="categoria", lazy=True)

    def __repr__(self):
        return f"<Categoria {self.nome}>"


# ============================================================
# MODELO: POST (com categoria)
# ============================================================
# Novidade: o campo categoria_id é uma CHAVE ESTRANGEIRA.
# Ele conecta cada post a uma categoria.
#
# db.ForeignKey("categoria.id") significa:
# "Este campo guarda o ID de uma linha da tabela Categoria"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.now)

    # CHAVE ESTRANGEIRA: conecta o post a uma categoria
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"))

    def __repr__(self):
        return f"<Post {self.id}: {self.titulo}>"


# ============================================================
# COMO OS RELACIONAMENTOS FUNCIONAM NA PRÁTICA
# ============================================================
#
# Acessar a categoria de um post:
#   post = Post.query.get(1)
#   print(post.categoria.nome)  # "Tecnologia"
#
# Acessar os posts de uma categoria:
#   cat = Categoria.query.get(1)
#   for post in cat.posts:
#       print(post.titulo)
#
# Criar post com categoria:
#   cat = Categoria.query.filter_by(nome="Python").first()
#   post = Post(titulo="Novo post", conteudo="...", categoria_id=cat.id)
# ============================================================


# Criar banco e dados iniciais
with app.app_context():
    db.create_all()

    if Categoria.query.count() == 0:
        categorias = [
            Categoria(nome="Tecnologia"),
            Categoria(nome="Python"),
            Categoria(nome="Dia a Dia"),
            Categoria(nome="Estudos"),
        ]
        db.session.add_all(categorias)
        db.session.commit()
        print("Categorias criadas!")

        # Buscar categorias para associar aos posts
        tech = Categoria.query.filter_by(nome="Tecnologia").first()
        python = Categoria.query.filter_by(nome="Python").first()
        dia = Categoria.query.filter_by(nome="Dia a Dia").first()
        estudos = Categoria.query.filter_by(nome="Estudos").first()

        posts = [
            Post(
                titulo="O que são bancos de dados?",
                conteudo="Bancos de dados são como planilhas super poderosas. "
                         "Eles guardam informações de forma organizada e "
                         "permanente. Estamos usando SQLite no nosso curso!",
                categoria_id=tech.id,
            ),
            Post(
                titulo="Meus primeiros passos com Python",
                conteudo="Comecei aprendendo print() e variáveis. Depois "
                         "vieram loops, listas, funções... e agora estou "
                         "criando um blog completo!",
                categoria_id=python.id,
            ),
            Post(
                titulo="Dicas para estudar programação",
                conteudo="1) Pratique todo dia, mesmo que 15 minutos. "
                         "2) Não tenha medo de errar. "
                         "3) Leia as mensagens de erro com calma. "
                         "4) Ajude seus colegas - ensinar é aprender.",
                categoria_id=estudos.id,
            ),
            Post(
                titulo="Flask é muito legal!",
                conteudo="Com apenas 5 linhas de código, você cria um "
                         "servidor web. Flask é simples mas poderoso. "
                         "Perfeito para quem está começando!",
                categoria_id=python.id,
            ),
            Post(
                titulo="Meu fim de semana",
                conteudo="Passei o sábado programando meu blog e o domingo "
                         "descansando. Equilíbrio é importante!",
                categoria_id=dia.id,
            ),
        ]
        db.session.add_all(posts)
        db.session.commit()
        print(f"{len(posts)} posts criados com categorias!")


# ============================================================
# ROTAS
# ============================================================

@app.route("/")
def lista_posts():
    """Lista todos os posts"""
    mensagem = request.args.get("msg")
    posts = Post.query.order_by(Post.criado_em.desc()).all()
    categorias = Categoria.query.order_by(Categoria.nome).all()
    return render_template(
        "categorias_lista.html",
        posts=posts,
        categorias=categorias,
        total=len(posts),
        mensagem=mensagem,
    )


@app.route("/categoria/<int:cat_id>")
def posts_por_categoria(cat_id):
    """Filtra posts por categoria"""
    categoria = Categoria.query.get_or_404(cat_id)

    # Duas formas de buscar posts de uma categoria:
    # 1. categoria.posts (usando o relationship)
    # 2. Post.query.filter_by(categoria_id=cat_id).all()
    posts = Post.query.filter_by(categoria_id=cat_id).order_by(
        Post.criado_em.desc()
    ).all()

    categorias = Categoria.query.order_by(Categoria.nome).all()
    return render_template(
        "categorias_lista.html",
        posts=posts,
        categorias=categorias,
        total=len(posts),
        categoria_atual=categoria,
    )


@app.route("/post/<int:post_id>")
def ver_post(post_id):
    """Mostra um post específico"""
    post = Post.query.get_or_404(post_id)
    return render_template("categorias_ver.html", post=post)


@app.route("/novo", methods=["GET", "POST"])
def novo_post():
    """Cria um novo post com categoria"""
    if request.method == "POST":
        post = Post(
            titulo=request.form["titulo"],
            conteudo=request.form["conteudo"],
            categoria_id=request.form.get("categoria_id") or None,
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("lista_posts", msg="Post publicado!"))

    categorias = Categoria.query.order_by(Categoria.nome).all()
    return render_template("categorias_novo.html", categorias=categorias)


@app.route("/editar/<int:post_id>", methods=["GET", "POST"])
def editar_post(post_id):
    """Edita um post existente"""
    post = Post.query.get_or_404(post_id)

    if request.method == "POST":
        post.titulo = request.form["titulo"]
        post.conteudo = request.form["conteudo"]
        post.categoria_id = request.form.get("categoria_id") or None
        db.session.commit()
        return redirect(url_for("ver_post", post_id=post.id))

    categorias = Categoria.query.order_by(Categoria.nome).all()
    return render_template(
        "categorias_editar.html", post=post, categorias=categorias
    )


@app.route("/excluir/<int:post_id>", methods=["POST"])
def excluir_post(post_id):
    """Exclui um post"""
    post = Post.query.get_or_404(post_id)
    titulo = post.titulo
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("lista_posts", msg=f"'{titulo}' excluído!"))


# ============================================================
# EXERCÍCIO
# ============================================================
# 1. Crie o modelo Categoria e adicione o campo categoria_id
#    ao Post
# 2. Crie pelo menos 3 categorias
# 3. Associe posts a categorias
# 4. Crie uma rota que filtra posts por categoria
#
# DESAFIO EXTRA:
# - Adicione um sistema de comentários (novo modelo Comment
#   com relacionamento com Post)
# - Mostre a contagem de posts por categoria na barra lateral
# - Permita criar novas categorias pelo formulário
# ============================================================


if __name__ == "__main__":
    print("=" * 50)
    print("  Lição 5.5 - Relacionamentos entre Dados")
    print("  Abra no navegador: http://localhost:5000")
    print("  ")
    print("  Páginas:")
    print("    /               → Todos os posts")
    print("    /categoria/1    → Posts de uma categoria")
    print("    /novo           → Criar post com categoria")
    print("    /post/1         → Ver post")
    print("    /editar/1       → Editar post")
    print("  ")
    print("  Para parar: aperte Ctrl+C")
    print("=" * 50)
    app.run(debug=True)
