# Módulo 5: Bancos de Dados e Persistência

**Duração:** 14 horas
**Pré-requisitos:** Módulos 1, 2, 3 e 4 completos

## Objetivo do Módulo

Os alunos aprendem a guardar dados permanentemente usando bancos de dados. O blog começa a tomar forma real: posts ficam salvos mesmo depois de reiniciar o servidor. Ao final, cada aluno terá um blog completo com CRUD, categorias, busca e paginação.

## Estrutura das Lições

| Lição | Arquivo | Tópico | Duração |
|-------|---------|--------|---------|
| 5.1 | `1_intro_banco_dados.py` | O que é um banco de dados? SQLite + SQLAlchemy | 2h |
| 5.2 | `2_modelos_sqlalchemy.py` | Modelos como classes Python | 2h |
| 5.3 | `3_crud_criar_ler.py` | CRUD: Criar e Ler posts | 2h |
| 5.4 | `4_crud_editar_excluir.py` | CRUD: Editar e Excluir posts | 2h |
| 5.5 | `5_relacionamentos.py` | Relacionamentos: Posts e Categorias | 2h |
| 5.6 | `6_busca_paginacao.py` | Busca por palavra-chave e paginação | 2h |
| 5.7 | `7_projeto_blog.py` | Projeto integrador: BlogPy | 2h |

## Conceitos Aprendidos

### Lição 5.1 - Introdução a Bancos de Dados
- O que é um banco de dados (analogia com planilhas)
- SQLite: banco de dados em um arquivo só
- Configurar Flask-SQLAlchemy
- Criar modelos com `db.Model` e `db.Column`
- Tipos de coluna: `String`, `Integer`, `Text`, `DateTime`
- Consultas básicas: `query.all()`, `query.get()`, `query.filter_by()`

### Lição 5.2 - Modelos como Classes Python
- Modelos como classes (comparação com dicionários)
- `primary_key`, `nullable`, `default`
- `__repr__()` para debug
- Adicionar e consultar dados no shell
- `order_by()` para ordenar resultados

### Lição 5.3 - CRUD: Criar e Ler
- O padrão CRUD (Create, Read, Update, Delete)
- Formulário → `request.form` → `db.session.add()` → `commit()`
- Listar todos: `query.order_by().all()`
- Ver individual: `query.get_or_404()`
- Redirecionar com mensagem após criar

### Lição 5.4 - CRUD: Editar e Excluir
- Formulário pré-preenchido com dados existentes
- Editar: atualizar atributos + `commit()` (sem `add()`)
- Excluir: `db.session.delete()` + `commit()`
- Confirmação antes de excluir (JavaScript `confirm()`)
- CRUD completo: o padrão que se repete em todo sistema

### Lição 5.5 - Relacionamentos entre Dados
- Chave estrangeira: `db.ForeignKey()`
- Relacionamento um-para-muitos: `db.relationship()`
- `backref` para acesso bidirecional
- Acessar dados relacionados: `post.categoria`, `categoria.posts`
- Filtrar por categoria: `filter_by(categoria_id=id)`

### Lição 5.6 - Busca e Paginação
- Busca com `.filter()` e `.like()`
- Combinar condições com `db.or_()`
- Paginação com `.paginate(page, per_page)`
- Objeto paginação: `items`, `pages`, `has_prev`, `has_next`
- Query parameters: `request.args.get("q")`, `request.args.get("page")`

## Estrutura de Arquivos

```
modulo_05_banco_dados/
├── 1_intro_banco_dados.py
├── 2_modelos_sqlalchemy.py
├── 3_crud_criar_ler.py
├── 4_crud_editar_excluir.py
├── 5_relacionamentos.py
├── 6_busca_paginacao.py
├── 7_projeto_blog.py
├── requirements.txt
├── README.md
└── templates/
    ├── alunos.html                (5.1)
    ├── posts_modelo.html          (5.2)
    ├── posts_base.html            (5.3, 5.4)
    ├── posts_lista.html           (5.3, 5.4)
    ├── posts_novo.html            (5.3, 5.4)
    ├── posts_ver.html             (5.4)
    ├── posts_editar.html          (5.4)
    ├── categorias_base.html       (5.5, 5.6)
    ├── categorias_lista.html      (5.5)
    ├── categorias_ver.html        (5.5)
    ├── categorias_novo.html       (5.5)
    ├── categorias_editar.html     (5.5)
    ├── busca_lista.html           (5.6)
    ├── busca_ver.html             (5.6)
    ├── busca_novo.html            (5.6)
    ├── busca_editar.html          (5.6)
    └── blog/                      (5.7 - projeto final)
        ├── base.html
        ├── inicio.html
        ├── ver_post.html
        ├── novo_post.html
        ├── editar_post.html
        ├── busca.html
        ├── categorias.html
        └── sobre.html
```

## Entregável Final

**BlogPy - Blog com Banco de Dados** com:
- Banco de dados SQLite com SQLAlchemy
- Modelos Post e Categoria com relacionamento
- CRUD completo: criar, ler, editar e excluir posts
- Categorias com filtro
- Busca por palavra-chave
- Paginação (5 posts por página)
- Design responsivo com barra lateral

## Para Executar

```bash
# 1. Instale as dependências
pip install flask flask-sqlalchemy

# 2. Navegue até a pasta
cd modulo_05_banco_dados

# 3. Execute uma lição (cada lição roda independente)
python 1_intro_banco_dados.py

# 4. Abra no navegador
# http://localhost:5000

# 5. Para parar o servidor: Ctrl+C

# IMPORTANTE: Cada lição cria seu próprio banco de dados (.db)
# Os dados persistem entre execuções!
```

## Dicas para Instrutores

- O momento mágico é quando o aluno para o servidor, roda de novo, e os dados ainda estão lá. Pare e celebre!
- Cada lição roda independente — execute apenas UMA por vez (cada uma usa a porta 5000)
- Os arquivos .db são criados automaticamente na pasta do módulo
- Se quiser recomeçar do zero, basta apagar o arquivo .db correspondente
- Na lição 5.1, mostre os dados no terminal antes do navegador para reforçar o conceito
- Na lição 5.4, peça aos alunos para testar a persistência: criar post → parar servidor → rodar de novo → post ainda lá!

## Recursos Externos

- [Documentação do Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [SQLAlchemy - Tipos de Coluna](https://docs.sqlalchemy.org/en/20/core/types.html)
