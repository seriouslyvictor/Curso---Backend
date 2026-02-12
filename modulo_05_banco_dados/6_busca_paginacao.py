# ============================================================
# LIÇÃO 5.6 - BUSCA E PAGINAÇÃO (2h)
# ============================================================
# Objetivo: Adicionar busca por palavra-chave e paginação
#           para quando temos muitos posts.
#
# Problema: Quando o blog tem 100 posts, não faz sentido
# mostrar todos de uma vez. A página ficaria enorme!
#
# Solução: PAGINAÇÃO — mostrar 5 posts por página, com botões
# "Anterior" e "Próxima" para navegar.
#
# E para encontrar posts específicos, adicionamos BUSCA:
# o usuário digita uma palavra e o banco encontra todos os
# posts que contêm aquela palavra no título ou conteúdo.
#
# Conceitos novos:
# - .filter() com .like() para busca
# - .paginate() para paginação
# - Query parameters: ?q=busca&page=2
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog_busca.db"
db = SQLAlchemy(app)


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


# Criar banco e dados iniciais (mais posts para testar paginação)
with app.app_context():
    db.create_all()

    if Post.query.count() == 0:
        categorias = [
            Categoria(nome="Tecnologia"),
            Categoria(nome="Python"),
            Categoria(nome="Dia a Dia"),
            Categoria(nome="Estudos"),
        ]
        db.session.add_all(categorias)
        db.session.commit()

        tech = Categoria.query.filter_by(nome="Tecnologia").first()
        python = Categoria.query.filter_by(nome="Python").first()
        dia = Categoria.query.filter_by(nome="Dia a Dia").first()
        estudos = Categoria.query.filter_by(nome="Estudos").first()

        # Muitos posts para testar paginação!
        posts = [
            Post(titulo="Bem-vindo ao meu blog!",
                 conteudo="Este é o primeiro post do blog. Aqui vou compartilhar o que aprendo no curso de Python Backend.",
                 categoria_id=dia.id),
            Post(titulo="O que é um banco de dados?",
                 conteudo="Bancos de dados são como planilhas super poderosas. Eles guardam informações de forma permanente e organizada.",
                 categoria_id=tech.id),
            Post(titulo="Meus primeiros passos com Python",
                 conteudo="Comecei com print() e variáveis. Depois aprendi loops, listas e funções. Python é uma linguagem incrível para iniciantes!",
                 categoria_id=python.id),
            Post(titulo="Flask: criando meu primeiro servidor",
                 conteudo="Com apenas 5 linhas de código, criei um servidor web. Flask é simples e poderoso ao mesmo tempo.",
                 categoria_id=python.id),
            Post(titulo="Dicas para estudar programação",
                 conteudo="1) Pratique todo dia. 2) Não tenha medo de errar. 3) Leia mensagens de erro. 4) Ajude colegas.",
                 categoria_id=estudos.id),
            Post(titulo="HTML e CSS: a base da web",
                 conteudo="HTML é o esqueleto e CSS é a roupa. Juntos, eles criam páginas bonitas que qualquer navegador entende.",
                 categoria_id=tech.id),
            Post(titulo="O que é CRUD?",
                 conteudo="CRUD significa Create, Read, Update e Delete. São as 4 operações básicas de qualquer sistema com dados.",
                 categoria_id=tech.id),
            Post(titulo="Relacionamentos no banco de dados",
                 conteudo="Assim como no Instagram um usuário tem muitos posts, no banco de dados uma categoria tem muitos posts. Isso é um relacionamento!",
                 categoria_id=tech.id),
            Post(titulo="Python vs JavaScript",
                 conteudo="Python é ótimo para backend e ciência de dados. JavaScript domina o frontend. Saber os dois é um superpoder!",
                 categoria_id=python.id),
            Post(titulo="Como funciona a internet?",
                 conteudo="Quando você acessa um site, seu navegador envia um pedido para um servidor. O servidor processa e envia a página de volta.",
                 categoria_id=tech.id),
            Post(titulo="Meu projeto final está tomando forma",
                 conteudo="O blog está ficando completo: CRUD, categorias, busca e paginação. Mal posso esperar para fazer o deploy!",
                 categoria_id=dia.id),
            Post(titulo="A importância de versionar código",
                 conteudo="Git é como um 'desfazer' super poderoso. Você pode voltar a qualquer versão anterior do seu projeto inteiro.",
                 categoria_id=estudos.id),
        ]
        db.session.add_all(posts)
        db.session.commit()
        print(f"{len(posts)} posts criados!")


# ============================================================
# CONFIGURAÇÃO DE PAGINAÇÃO
# ============================================================
POSTS_POR_PAGINA = 5


# ============================================================
# ROTAS
# ============================================================

@app.route("/")
def lista_posts():
    """Lista posts com paginação"""
    mensagem = request.args.get("msg")

    # request.args.get("page", 1, type=int) significa:
    # "Pegue o parâmetro 'page' da URL. Se não existir, use 1."
    # type=int converte para número automaticamente.
    pagina = request.args.get("page", 1, type=int)

    # ============================================================
    # PAGINAÇÃO COM .paginate()
    # ============================================================
    # Em vez de .all() (que retorna TODOS os posts),
    # usamos .paginate() que retorna apenas uma página.
    #
    # paginate(page=1, per_page=5) retorna:
    #   paginacao.items  → lista dos posts DESTA página
    #   paginacao.pages  → total de páginas
    #   paginacao.page   → página atual
    #   paginacao.has_prev → True se tem página anterior
    #   paginacao.has_next → True se tem próxima página
    #   paginacao.prev_num → número da página anterior
    #   paginacao.next_num → número da próxima página
    #   paginacao.total    → total de itens em todas as páginas

    paginacao = Post.query.order_by(Post.criado_em.desc()).paginate(
        page=pagina,
        per_page=POSTS_POR_PAGINA,
        error_out=False,  # Não dá erro se a página não existir
    )

    categorias = Categoria.query.order_by(Categoria.nome).all()

    return render_template(
        "busca_lista.html",
        posts=paginacao.items,
        paginacao=paginacao,
        categorias=categorias,
        total=paginacao.total,
        mensagem=mensagem,
    )


@app.route("/categoria/<int:cat_id>")
def posts_por_categoria(cat_id):
    """Filtra posts por categoria com paginação"""
    categoria = Categoria.query.get_or_404(cat_id)
    pagina = request.args.get("page", 1, type=int)

    paginacao = Post.query.filter_by(categoria_id=cat_id).order_by(
        Post.criado_em.desc()
    ).paginate(page=pagina, per_page=POSTS_POR_PAGINA, error_out=False)

    categorias = Categoria.query.order_by(Categoria.nome).all()

    return render_template(
        "busca_lista.html",
        posts=paginacao.items,
        paginacao=paginacao,
        categorias=categorias,
        total=paginacao.total,
        categoria_atual=categoria,
    )


# ============================================================
# BUSCA POR PALAVRA-CHAVE
# ============================================================
# O usuário digita uma palavra, e buscamos no título E no
# conteúdo de todos os posts.
#
# .filter() com .like() funciona assim:
#   Post.titulo.like("%python%") → encontra títulos que CONTÊM "python"
#   O % significa "qualquer coisa antes ou depois"
#
# Usamos .or_() para buscar no título OU no conteúdo:
#   "Encontre posts onde o título contém X OU o conteúdo contém X"

@app.route("/busca")
def buscar():
    """Busca posts por palavra-chave"""
    # request.args.get("q") pega o parâmetro 'q' da URL
    # Exemplo: /busca?q=python → termo = "python"
    termo = request.args.get("q", "")
    pagina = request.args.get("page", 1, type=int)

    if termo:
        # Buscar no título OU no conteúdo
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
        # Se não digitou nada, mostra todos
        paginacao = Post.query.order_by(Post.criado_em.desc()).paginate(
            page=pagina, per_page=POSTS_POR_PAGINA, error_out=False
        )

    categorias = Categoria.query.order_by(Categoria.nome).all()

    return render_template(
        "busca_lista.html",
        posts=paginacao.items,
        paginacao=paginacao,
        categorias=categorias,
        total=paginacao.total,
        termo_busca=termo,
    )


@app.route("/post/<int:post_id>")
def ver_post(post_id):
    """Mostra um post específico"""
    post = Post.query.get_or_404(post_id)
    return render_template("busca_ver.html", post=post)


@app.route("/novo", methods=["GET", "POST"])
def novo_post():
    """Cria um novo post"""
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
    return render_template("busca_novo.html", categorias=categorias)


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
    return render_template("busca_editar.html", post=post, categorias=categorias)


@app.route("/excluir/<int:post_id>", methods=["POST"])
def excluir_post(post_id):
    """Exclui um post"""
    post = Post.query.get_or_404(post_id)
    titulo = post.titulo
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("lista_posts", msg=f"'{titulo}' excluído!"))


# ============================================================
# RESUMO DOS CONCEITOS
# ============================================================
#
# BUSCA:
#   Post.query.filter(Post.titulo.like("%termo%"))
#   → Encontra posts que contêm "termo" no título
#
#   db.or_(condição1, condição2)
#   → Combina condições: título OU conteúdo contém o termo
#
# PAGINAÇÃO:
#   .paginate(page=1, per_page=5)
#   → Retorna apenas 5 resultados da página 1
#
#   paginacao.items → os posts desta página
#   paginacao.has_next / has_prev → tem mais páginas?
#   paginacao.next_num / prev_num → números das páginas
#
# QUERY PARAMETERS:
#   /busca?q=python&page=2
#   → request.args.get("q") = "python"
#   → request.args.get("page", 1, type=int) = 2
# ============================================================


# ============================================================
# EXERCÍCIO
# ============================================================
# 1. Adicione busca por palavra-chave ao blog
# 2. Adicione paginação (5 posts por página)
# 3. Teste: crie 10+ posts e navegue entre as páginas
# 4. Teste: busque por uma palavra e veja os resultados
#
# DESAFIO EXTRA:
# - Adicione busca que ignora maiúsculas/minúsculas
# - Mostre "Resultados para 'python'" acima dos resultados
# - Adicione ordenação (mais recentes / mais antigos)
# ============================================================


if __name__ == "__main__":
    print("=" * 50)
    print("  Lição 5.6 - Busca e Paginação")
    print("  Abra no navegador: http://localhost:5000")
    print("  ")
    print("  Páginas:")
    print("    /               → Posts (paginados)")
    print("    /busca?q=python → Buscar posts")
    print("    /categoria/1    → Filtrar por categoria")
    print("    /novo           → Criar post")
    print("  ")
    print("  Para parar: aperte Ctrl+C")
    print("=" * 50)
    app.run(debug=True)
