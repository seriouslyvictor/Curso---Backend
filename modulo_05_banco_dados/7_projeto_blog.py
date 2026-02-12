# ============================================================
# LIÇÃO 5.7 - MINI-PROJETO: BLOG COM BANCO DE DADOS (2h)
# ============================================================
# Objetivo: Juntar TUDO que aprendemos no Módulo 5 em um blog
#           completo e polido!
#
# O BlogPy é um blog completo com:
# ✓ Banco de dados SQLite com SQLAlchemy (5.1)
# ✓ Modelos Post e Categoria como classes Python (5.2)
# ✓ CRUD completo: criar, ler, editar e excluir posts (5.3, 5.4)
# ✓ Relacionamentos: posts pertencem a categorias (5.5)
# ✓ Busca por palavra-chave e paginação (5.6)
#
# Arquivos usados:
# - templates/blog/base.html         → layout do blog
# - templates/blog/inicio.html       → lista de posts (paginada)
# - templates/blog/ver_post.html     → post individual
# - templates/blog/novo_post.html    → formulário de criação
# - templates/blog/editar_post.html  → formulário de edição
# - templates/blog/categorias.html   → lista de categorias
# - templates/blog/busca.html        → resultados de busca
# - templates/blog/sobre.html        → página sobre
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogpy.db"
db = SQLAlchemy(app)

POSTS_POR_PAGINA = 5


# ============================================================
# MODELOS
# ============================================================

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    posts = db.relationship("Post", backref="categoria", lazy=True)

    def __repr__(self):
        return f"<Categoria {self.nome}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.now)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"))

    def __repr__(self):
        return f"<Post {self.id}: {self.titulo}>"


# ============================================================
# CRIAR BANCO E DADOS INICIAIS
# ============================================================

with app.app_context():
    db.create_all()

    if Categoria.query.count() == 0:
        categorias = [
            Categoria(nome="Tecnologia"),
            Categoria(nome="Python"),
            Categoria(nome="Dia a Dia"),
            Categoria(nome="Estudos"),
            Categoria(nome="Projetos"),
        ]
        db.session.add_all(categorias)
        db.session.commit()

        tech = Categoria.query.filter_by(nome="Tecnologia").first()
        python = Categoria.query.filter_by(nome="Python").first()
        dia = Categoria.query.filter_by(nome="Dia a Dia").first()
        estudos = Categoria.query.filter_by(nome="Estudos").first()
        projetos = Categoria.query.filter_by(nome="Projetos").first()

        posts = [
            Post(
                titulo="Bem-vindo ao BlogPy!",
                conteudo="Este é o meu blog criado com Python e Flask! "
                         "Aqui vou compartilhar tudo que estou aprendendo "
                         "no curso de Python Backend. O blog usa banco de "
                         "dados SQLite para guardar os posts permanentemente, "
                         "tem categorias, busca e paginação. Tudo feito com "
                         "poucas linhas de código Python!",
                categoria_id=projetos.id,
            ),
            Post(
                titulo="O que são bancos de dados?",
                conteudo="Bancos de dados são como planilhas super poderosas. "
                         "Eles guardam informações de forma organizada e "
                         "permanente. No nosso blog, usamos SQLite — um banco "
                         "que fica em um arquivo só! Com Flask-SQLAlchemy, "
                         "escrevemos Python em vez de SQL, o que facilita muito.",
                categoria_id=tech.id,
            ),
            Post(
                titulo="Meus primeiros passos com Python",
                conteudo="Comecei o curso sem saber nada de programação. "
                         "Primeiro aprendi print() e variáveis. Depois vieram "
                         "loops, listas e funções. No Módulo 2, organizei código "
                         "em arquivos. No Módulo 3, aprendi HTML e CSS. No "
                         "Módulo 4, criei meu primeiro servidor com Flask. "
                         "E agora, no Módulo 5, estou usando bancos de dados!",
                categoria_id=python.id,
            ),
            Post(
                titulo="CRUD: as 4 operações essenciais",
                conteudo="CRUD significa Create (criar), Read (ler), Update "
                         "(atualizar) e Delete (excluir). São as 4 operações "
                         "que qualquer sistema precisa. Redes sociais usam "
                         "CRUD para posts. Lojas usam CRUD para produtos. "
                         "O nosso blog usa CRUD para gerenciar os textos!",
                categoria_id=estudos.id,
            ),
            Post(
                titulo="Flask é incrível para iniciantes",
                conteudo="Com apenas 5 linhas de código, você cria um "
                         "servidor web. Flask é simples mas poderoso. "
                         "Junto com SQLAlchemy, é possível criar aplicações "
                         "web completas sem precisar aprender SQL avançado.",
                categoria_id=python.id,
            ),
            Post(
                titulo="Dicas para estudar programação",
                conteudo="1) Pratique todo dia, mesmo que só 15 minutos.\n"
                         "2) Não tenha medo de errar — erros são professores.\n"
                         "3) Leia as mensagens de erro com calma.\n"
                         "4) Ajude seus colegas — ensinar é a melhor forma "
                         "de aprender.\n"
                         "5) Construa projetos próprios — é o que fixa o "
                         "conhecimento de verdade!",
                categoria_id=estudos.id,
            ),
            Post(
                titulo="Como funciona a internet?",
                conteudo="Quando você acessa um site, seu navegador (cliente) "
                         "envia um pedido HTTP para um servidor. O servidor "
                         "processa o pedido, consulta o banco de dados se "
                         "necessário, e envia a resposta de volta: uma página "
                         "HTML que o navegador renderiza na tela. É isso que "
                         "nosso Flask faz nos bastidores!",
                categoria_id=tech.id,
            ),
            Post(
                titulo="Relacionamentos no banco de dados",
                conteudo="Assim como no Instagram um usuário tem muitos posts, "
                         "no nosso blog uma categoria tem muitos posts. Isso "
                         "é um relacionamento um-para-muitos. No SQLAlchemy, "
                         "usamos db.ForeignKey() e db.relationship() para "
                         "criar essas conexões entre tabelas.",
                categoria_id=tech.id,
            ),
            Post(
                titulo="Meu fim de semana de programação",
                conteudo="Passei o sábado inteiro programando meu blog! "
                         "Adicionei categorias, busca e paginação. É muito "
                         "gratificante ver tudo funcionando. No domingo, "
                         "descansei — equilíbrio é importante!",
                categoria_id=dia.id,
            ),
            Post(
                titulo="Próximos passos: autenticação e deploy",
                conteudo="O blog está ficando completo! No Módulo 6 vou "
                         "aprender a criar login e registro de usuários. "
                         "No Módulo 7, vou colocar o blog no ar para qualquer "
                         "pessoa acessar. Mal posso esperar!",
                categoria_id=projetos.id,
            ),
            Post(
                titulo="HTML e CSS: a base de tudo",
                conteudo="Antes de fazer backend, precisei aprender frontend. "
                         "HTML é o esqueleto da página (estrutura) e CSS é a "
                         "roupa (visual). Juntos, eles criam páginas bonitas "
                         "que qualquer navegador entende. No Flask, usamos "
                         "templates Jinja2 para gerar HTML dinâmico!",
                categoria_id=tech.id,
            ),
            Post(
                titulo="Por que Python é tão popular?",
                conteudo="Python é uma das linguagens mais populares do mundo. "
                         "Os motivos são claros: sintaxe simples e legível, "
                         "enorme comunidade de desenvolvedores, milhares de "
                         "bibliotecas prontas, e serve para quase tudo: web, "
                         "dados, IA, automação e muito mais!",
                categoria_id=python.id,
            ),
        ]
        db.session.add_all(posts)
        db.session.commit()
        print(f"Blog criado com {len(posts)} posts e {len(categorias)} categorias!")


# ============================================================
# ROTAS: PÁGINAS HTML
# ============================================================

@app.route("/")
def inicio():
    """Página principal com posts paginados"""
    mensagem = request.args.get("msg")
    pagina = request.args.get("page", 1, type=int)

    paginacao = Post.query.order_by(Post.criado_em.desc()).paginate(
        page=pagina, per_page=POSTS_POR_PAGINA, error_out=False
    )

    categorias = Categoria.query.order_by(Categoria.nome).all()

    return render_template(
        "blog/inicio.html",
        posts=paginacao.items,
        paginacao=paginacao,
        categorias=categorias,
        mensagem=mensagem,
    )


@app.route("/post/<int:post_id>")
def ver_post(post_id):
    """Mostra um post completo"""
    post = Post.query.get_or_404(post_id)
    return render_template("blog/ver_post.html", post=post)


@app.route("/novo", methods=["GET", "POST"])
def novo_post():
    """Cria um novo post"""
    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        conteudo = request.form["conteudo"].strip()
        categoria_id = request.form.get("categoria_id") or None

        if not titulo or not conteudo:
            categorias = Categoria.query.order_by(Categoria.nome).all()
            return render_template(
                "blog/novo_post.html",
                categorias=categorias,
                erro="Título e conteúdo são obrigatórios!",
                titulo=titulo,
                conteudo=conteudo,
            )

        post = Post(
            titulo=titulo,
            conteudo=conteudo,
            categoria_id=categoria_id,
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("inicio", msg="Post publicado com sucesso!"))

    categorias = Categoria.query.order_by(Categoria.nome).all()
    return render_template("blog/novo_post.html", categorias=categorias)


@app.route("/editar/<int:post_id>", methods=["GET", "POST"])
def editar_post(post_id):
    """Edita um post existente"""
    post = Post.query.get_or_404(post_id)

    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        conteudo = request.form["conteudo"].strip()

        if not titulo or not conteudo:
            categorias = Categoria.query.order_by(Categoria.nome).all()
            return render_template(
                "blog/editar_post.html",
                post=post,
                categorias=categorias,
                erro="Título e conteúdo são obrigatórios!",
            )

        post.titulo = titulo
        post.conteudo = conteudo
        post.categoria_id = request.form.get("categoria_id") or None
        db.session.commit()
        return redirect(url_for("ver_post", post_id=post.id))

    categorias = Categoria.query.order_by(Categoria.nome).all()
    return render_template(
        "blog/editar_post.html", post=post, categorias=categorias
    )


@app.route("/excluir/<int:post_id>", methods=["POST"])
def excluir_post(post_id):
    """Exclui um post"""
    post = Post.query.get_or_404(post_id)
    titulo = post.titulo
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("inicio", msg=f"'{titulo}' excluído com sucesso!"))


@app.route("/categoria/<int:cat_id>")
def posts_por_categoria(cat_id):
    """Filtra posts por categoria"""
    categoria = Categoria.query.get_or_404(cat_id)
    pagina = request.args.get("page", 1, type=int)

    paginacao = Post.query.filter_by(categoria_id=cat_id).order_by(
        Post.criado_em.desc()
    ).paginate(page=pagina, per_page=POSTS_POR_PAGINA, error_out=False)

    categorias = Categoria.query.order_by(Categoria.nome).all()

    return render_template(
        "blog/inicio.html",
        posts=paginacao.items,
        paginacao=paginacao,
        categorias=categorias,
        categoria_atual=categoria,
    )


@app.route("/busca")
def buscar():
    """Busca posts por palavra-chave"""
    termo = request.args.get("q", "").strip()
    pagina = request.args.get("page", 1, type=int)

    if termo:
        busca = f"%{termo}%"
        paginacao = Post.query.filter(
            db.or_(
                Post.titulo.like(busca),
                Post.conteudo.like(busca),
            )
        ).order_by(Post.criado_em.desc()).paginate(
            page=pagina, per_page=POSTS_POR_PAGINA, error_out=False
        )
    else:
        paginacao = Post.query.order_by(Post.criado_em.desc()).paginate(
            page=pagina, per_page=POSTS_POR_PAGINA, error_out=False
        )

    categorias = Categoria.query.order_by(Categoria.nome).all()

    return render_template(
        "blog/busca.html",
        posts=paginacao.items,
        paginacao=paginacao,
        categorias=categorias,
        termo_busca=termo,
    )


@app.route("/categorias")
def lista_categorias():
    """Lista todas as categorias com contagem de posts"""
    categorias = Categoria.query.order_by(Categoria.nome).all()
    return render_template("blog/categorias.html", categorias=categorias)


@app.route("/sobre")
def sobre():
    """Página sobre o blog"""
    total_posts = Post.query.count()
    total_categorias = Categoria.query.count()
    return render_template(
        "blog/sobre.html",
        total_posts=total_posts,
        total_categorias=total_categorias,
    )


# ============================================================
# O QUE ESTE PROJETO USA (tudo do Módulo 5):
# ============================================================
# ✓ SQLite + Flask-SQLAlchemy (5.1)
# ✓ Modelos como classes Python (5.2)
# ✓ CRUD: criar e ler posts (5.3)
# ✓ CRUD: editar e excluir posts (5.4)
# ✓ Relacionamentos: Post ↔ Categoria (5.5)
# ✓ Busca por palavra-chave e paginação (5.6)
#
# PRÓXIMO PASSO (Módulo 6):
# Adicionar usuários e autenticação — login, registro,
# e cada post terá um autor!
# ============================================================


# ============================================================
# DESAFIO EXTRA
# ============================================================
# 1. Adicione um sistema de comentários (novo modelo Comment
#    com relacionamento com Post)
# 2. Crie um painel admin com estatísticas (total de posts,
#    posts por categoria, post mais recente)
# 3. Exporte posts como CSV para download
# 4. Adicione "rascunho" vs "publicado" aos posts
# ============================================================


if __name__ == "__main__":
    print("=" * 50)
    print("  BlogPy - Blog com Banco de Dados")
    print("  Abra no navegador: http://localhost:5000")
    print("  ")
    print("  Páginas:")
    print("    /               → Posts (paginados)")
    print("    /novo           → Criar post")
    print("    /post/1         → Ver post")
    print("    /editar/1       → Editar post")
    print("    /busca?q=python → Buscar posts")
    print("    /categoria/1    → Posts de uma categoria")
    print("    /categorias     → Todas as categorias")
    print("    /sobre          → Sobre o blog")
    print("  ")
    print("  Para parar: aperte Ctrl+C")
    print("=" * 50)
    app.run(debug=True)
