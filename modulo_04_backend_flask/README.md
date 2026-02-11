# Módulo 4: Backend com Flask

**Duração:** 12 horas
**Pré-requisitos:** Módulos 1, 2 e 3 completos

## Objetivo do Módulo

Conectar Python à web. Os alunos aprendem que as páginas bonitas do Módulo 3 podem ser alimentadas por código Python que toma decisões e gera conteúdo dinamicamente.

## Estrutura das Lições

| Lição | Arquivo | Tópico | Duração |
|-------|---------|--------|---------|
| 4.1 | `1_hello_flask.py` | Primeiro servidor, rotas, localhost | 2h |
| 4.2 | `2_rotas_paginas.py` | Rotas dinâmicas, variáveis na URL | 2h |
| 4.3 | `3_templates_jinja.py` | Templates Jinja2, {{ }}, {% if %}, {% for %} | 2h |
| 4.4 | `4_heranca_templates.py` | Herança de templates, base.html, static/ | 2h |
| 4.5 | `5_formularios_post.py` | Formulários, POST, request.form | 2h |
| 4.6 | `6_projeto_webapp.py` | Projeto integrador: TaskPy | 2h |

## Conceitos Aprendidos

### Lição 4.1 - Hello Flask
- Instalar Flask com `pip install flask`
- Criar app Flask e rotas com `@app.route()`
- Retornar HTML como string
- `localhost` e porta 5000
- `debug=True` para recarregar automático

### Lição 4.2 - Rotas Dinâmicas
- Variáveis na URL: `<nome>`, `<int:id>`
- Múltiplas variáveis na mesma rota
- Gerar HTML dinâmico com loops e condições Python
- Tipos de variáveis: string, int, float

### Lição 4.3 - Templates com Jinja2
- `render_template()` para carregar HTML
- `{{ variavel }}` para mostrar valores
- `{% if %}` / `{% elif %}` / `{% else %}` / `{% endif %}`
- `{% for item in lista %}` / `{% endfor %}`
- Filtros: `|length`, `|format`

### Lição 4.4 - Herança de Templates
- `{% extends "base.html" %}` para herdar layout
- `{% block nome %}` / `{% endblock %}` para blocos
- Pasta `static/` para CSS, imagens, JavaScript
- `url_for('static', filename='...')` para arquivos estáticos
- `@app.context_processor` para variáveis globais

### Lição 4.5 - Formulários e POST
- GET vs POST
- `method="POST"` no formulário HTML
- `request.form` para receber dados
- `methods=["GET", "POST"]` na rota
- `redirect()` e `url_for()` para redirecionamento
- `request.method` para verificar tipo de requisição

## Estrutura de Arquivos

```
modulo_04_backend_flask/
├── 1_hello_flask.py
├── 2_rotas_paginas.py
├── 3_templates_jinja.py
├── 4_heranca_templates.py
├── 5_formularios_post.py
├── 6_projeto_webapp.py
├── requirements.txt
├── README.md
├── static/
│   └── estilo.css
└── templates/
    ├── saudacao.html           (4.3)
    ├── lista_frutas.html       (4.3)
    ├── alunos_template.html    (4.3)
    ├── base.html               (4.4)
    ├── inicio.html             (4.4)
    ├── sobre.html              (4.4)
    ├── galeria.html            (4.4)
    ├── contato.html            (4.4)
    ├── formulario.html         (4.5)
    ├── resultado.html          (4.5)
    ├── enquete.html            (4.5)
    └── projeto/                (4.6)
        ├── base.html
        ├── inicio.html
        ├── nova_tarefa.html
        └── sobre.html
```

## Entregável Final

**TaskPy - Gerenciador de Tarefas** com:
- Múltiplas páginas com navegação
- Rotas dinâmicas para concluir/excluir tarefas
- Templates com herança (base.html)
- Formulário POST para criar tarefas
- Estatísticas de tarefas

## Para Executar

```bash
# 1. Instale o Flask
pip install flask

# 2. Navegue até a pasta
cd modulo_04_backend_flask

# 3. Execute uma lição (cada lição roda independente)
python 1_hello_flask.py

# 4. Abra no navegador
# http://localhost:5000

# 5. Para parar o servidor: Ctrl+C
```

## Dicas para Instrutores

- O momento mágico é na Lição 4.1: quando o aluno roda 5 linhas e vê uma página no navegador. Pare e celebre!
- Cada lição roda independente — execute apenas UMA por vez (cada uma usa a porta 5000)
- Incentive os alunos a experimentarem com rotas e templates — cada mudança aparece no navegador ao salvar

## Recursos Externos

- [Documentação do Flask](https://flask.palletsprojects.com/)
- [Jinja2 Template Designer](https://jinja.palletsprojects.com/templates/)
- [HTTP Status Codes](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status)
