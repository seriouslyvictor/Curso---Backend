# ============================================================
# LIÇÃO 4.6 - MINI-PROJETO: WEB APP v1 (TaskPy)
# ============================================================
# Objetivo: Criar uma aplicação web completa que usa TUDO que
#           aprendemos no Módulo 4!
#
# O TaskPy é um gerenciador de tarefas com:
# ✓ Múltiplas páginas com navegação (4.1, 4.2)
# ✓ Rotas dinâmicas /concluir/<id> (4.2)
# ✓ Templates com Jinja2 (4.3)
# ✓ Herança de templates - base.html (4.4)
# ✓ Formulários POST para criar tarefas (4.5)
#
# Arquivos usados:
# - templates/projeto/base.html        → layout do projeto
# - templates/projeto/inicio.html      → lista de tarefas
# - templates/projeto/nova_tarefa.html  → formulário
# - templates/projeto/sobre.html       → página sobre
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)


# ============================================================
# DADOS (simula banco de dados)
# ============================================================
# No Módulo 5, vamos trocar esta lista por um banco de dados!
# Por enquanto, os dados ficam na memória do programa.

# Contador para gerar IDs únicos
proximo_id = 4

tarefas = [
    {
        "id": 1,
        "titulo": "Estudar Flask",
        "descricao": "Completar o módulo 4 do curso",
        "prioridade": "alta",
        "concluida": False,
        "criada_em": "2025-01-15 10:00",
    },
    {
        "id": 2,
        "titulo": "Fazer exercícios de Python",
        "descricao": "Revisar listas e dicionários",
        "prioridade": "media",
        "concluida": True,
        "criada_em": "2025-01-14 14:30",
    },
    {
        "id": 3,
        "titulo": "Criar portfólio no GitHub",
        "descricao": "",
        "prioridade": "baixa",
        "concluida": False,
        "criada_em": "2025-01-13 09:00",
    },
]


# ============================================================
# ROTAS HTML (para humanos no navegador)
# ============================================================

@app.route("/")
def inicio():
    """Página principal: lista todas as tarefas"""
    mensagem = request.args.get("msg")

    # Calcular estatísticas
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t["concluida"])
    pendentes = total - concluidas

    return render_template(
        "projeto/inicio.html",
        tarefas=tarefas,
        total=total,
        concluidas=concluidas,
        pendentes=pendentes,
        mensagem=mensagem,
    )


@app.route("/nova", methods=["GET", "POST"])
def nova_tarefa():
    """GET: mostra formulário. POST: cria a tarefa."""
    global proximo_id

    if request.method == "POST":
        # Receber dados do formulário
        tarefa = {
            "id": proximo_id,
            "titulo": request.form["titulo"],
            "descricao": request.form.get("descricao", ""),
            "prioridade": request.form.get("prioridade", "media"),
            "concluida": False,
            "criada_em": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        tarefas.append(tarefa)
        proximo_id += 1

        print(f"Nova tarefa criada: {tarefa['titulo']}")

        # Redirecionar para a lista com mensagem de sucesso
        return redirect(url_for("inicio", msg="Tarefa criada com sucesso!"))

    return render_template("projeto/nova_tarefa.html")


@app.route("/concluir/<int:tarefa_id>", methods=["POST"])
def concluir_tarefa(tarefa_id):
    """Marca uma tarefa como concluída"""
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["concluida"] = True
            return redirect(url_for("inicio", msg=f"'{tarefa['titulo']}' concluída!"))

    return redirect(url_for("inicio", msg="Tarefa não encontrada"))


@app.route("/excluir/<int:tarefa_id>", methods=["POST"])
def excluir_tarefa(tarefa_id):
    """Remove uma tarefa da lista"""
    global tarefas
    titulo = ""
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            titulo = tarefa["titulo"]
            break

    tarefas = [t for t in tarefas if t["id"] != tarefa_id]

    if titulo:
        return redirect(url_for("inicio", msg=f"'{titulo}' excluída!"))
    return redirect(url_for("inicio", msg="Tarefa não encontrada"))


@app.route("/sobre")
def sobre():
    """Página sobre o projeto"""
    return render_template("projeto/sobre.html")


# ============================================================
# DESAFIO EXTRA
# ============================================================
# 1. Adicione um campo "categoria" às tarefas (estudo, trabalho, pessoal)
# 2. Adicione a funcionalidade de editar tarefa
# 3. Use flash messages para feedback ao usuário


# ============================================================
# O QUE ESTE PROJETO USA:
# ============================================================
# ✓ Flask como servidor web (4.1)
# ✓ Rotas fixas e dinâmicas (4.1, 4.2)
# ✓ Templates com Jinja2: {{ }}, {% if %}, {% for %} (4.3)
# ✓ Herança de templates com base.html (4.4)
# ✓ Formulários POST e request.form (4.5)
# ✓ redirect() e url_for() (4.5)
#
# PRÓXIMO PASSO (Módulo 5):
# Trocar a lista na memória por um BANCO DE DADOS
# para que as tarefas não sumam quando o servidor reiniciar!
# ============================================================


if __name__ == "__main__":
    print("=" * 50)
    print("  TaskPy - Gerenciador de Tarefas")
    print("  Abra no navegador: http://localhost:5000")
    print("  ")
    print("  Páginas:")
    print("    /        → Lista de tarefas")
    print("    /nova    → Criar tarefa")
    print("    /sobre   → Sobre o projeto")
    print("  ")
    print("  Para parar: aperte Ctrl+C")
    print("=" * 50)
    app.run(debug=True)
