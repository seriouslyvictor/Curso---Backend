# ============================================================
# LIÇÃO 2.3 - LEITURA E ESCRITA DE ARQUIVOS
# ============================================================
# Objetivo: Fazer o programa salvar e carregar dados
# Motivação: Até agora, tudo desaparece quando o programa fecha.
#            Com arquivos, seus dados ficam salvos para sempre!
# ============================================================

# -----------------------------
# PARTE 1: Por que arquivos?
# -----------------------------
# Sem arquivos:
# - Você cria uma lista de tarefas
# - Fecha o programa
# - Perdeu tudo! Precisa digitar de novo

# Com arquivos:
# - Você cria uma lista de tarefas
# - Salva em um arquivo
# - Fecha o programa
# - Abre de novo
# - Suas tarefas ainda estão lá!


# -----------------------------
# PARTE 2: Escrevendo em arquivos
# -----------------------------
# open() abre um arquivo
# "w" = write (escrever) - CUIDADO: apaga conteúdo anterior!

print("=== ESCREVENDO EM ARQUIVO ===")

# Criando e escrevendo em um arquivo
arquivo = open("meu_arquivo.txt", "w", encoding="utf-8")
arquivo.write("Olá! Esta é a primeira linha.\n")
arquivo.write("Esta é a segunda linha.\n")
arquivo.write("E esta é a terceira!\n")
arquivo.close()  # Sempre feche o arquivo!

print("Arquivo 'meu_arquivo.txt' criado com sucesso!")


# Jeito moderno (melhor) - usando 'with':
# O arquivo fecha automaticamente quando sai do bloco
with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Mensagem importante!\n")
    arquivo.write("Não esqueça de estudar Python.\n")

print("Arquivo 'mensagem.txt' criado!")


# -----------------------------
# PARTE 3: Lendo arquivos
# -----------------------------
# "r" = read (ler)

print("\n=== LENDO ARQUIVOS ===")

# Lendo todo o conteúdo de uma vez:
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo completo:")
    print(conteudo)

# Lendo linha por linha:
print("Linha por linha:")
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(f"  > {linha.strip()}")  # strip() remove o \n

# Lendo como lista de linhas:
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print(f"\nTotal de linhas: {len(linhas)}")


# -----------------------------
# PARTE 4: Adicionando conteúdo (append)
# -----------------------------
# "a" = append (adicionar) - NÃO apaga o conteúdo existente

print("\n=== ADICIONANDO CONTEÚDO ===")

with open("meu_arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Esta linha foi adicionada depois!\n")
    arquivo.write("E esta também!\n")

print("Linhas adicionadas ao arquivo!")

# Verificando:
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    print("\nConteúdo atualizado:")
    print(arquivo.read())


# -----------------------------
# PARTE 5: Trabalhando com JSON
# -----------------------------
# JSON é perfeito para salvar listas e dicionários!
# JSON = JavaScript Object Notation (formato universal de dados)

import json

print("=== SALVANDO COM JSON ===")

# Dados estruturados (lista de dicionários)
alunos = [
    {"nome": "Ana", "idade": 16, "nota": 9.0},
    {"nome": "Bruno", "idade": 17, "nota": 7.5},
    {"nome": "Carla", "idade": 16, "nota": 8.5}
]

# Salvando em JSON:
with open("alunos.json", "w", encoding="utf-8") as arquivo:
    json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

print("Dados salvos em 'alunos.json'!")

# Lendo do JSON:
with open("alunos.json", "r", encoding="utf-8") as arquivo:
    alunos_carregados = json.load(arquivo)

print("\nDados carregados do arquivo:")
for aluno in alunos_carregados:
    print(f"  - {aluno['nome']}: nota {aluno['nota']}")


# Salvando um dicionário simples:
configuracoes = {
    "tema": "escuro",
    "idioma": "português",
    "volume": 80,
    "notificacoes": True
}

with open("config.json", "w", encoding="utf-8") as arquivo:
    json.dump(configuracoes, arquivo, indent=4, ensure_ascii=False)

print("\nConfigurações salvas em 'config.json'!")


# -----------------------------
# PARTE 6: Verificando se arquivo existe
# -----------------------------
import os

print("\n=== VERIFICANDO ARQUIVOS ===")

# Verificando existência:
if os.path.exists("alunos.json"):
    print("✓ O arquivo 'alunos.json' existe!")
else:
    print("✗ O arquivo não foi encontrado.")

# Lista de arquivos na pasta:
print("\nArquivos na pasta atual:")
for arquivo in os.listdir("."):
    if arquivo.endswith((".txt", ".json")):
        print(f"  - {arquivo}")


# ============================================================
# EXERCÍCIO 2.3 - LISTA DE TAREFAS PERSISTENTE
# ============================================================

print("\n" + "=" * 50)
print("        LISTA DE TAREFAS (com salvamento)")
print("=" * 50)

ARQUIVO_TAREFAS = "tarefas.json"


def carregar_tarefas():
    """Carrega tarefas do arquivo JSON"""
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []  # Retorna lista vazia se arquivo não existe


def salvar_tarefas(tarefas):
    """Salva tarefas no arquivo JSON"""
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=2, ensure_ascii=False)


def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa"""
    descricao = input("Descrição da tarefa: ")
    tarefa = {
        "descricao": descricao,
        "concluida": False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print(f"✓ Tarefa adicionada!")


def listar_tarefas(tarefas):
    """Lista todas as tarefas"""
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n--- SUAS TAREFAS ---")
    for i, tarefa in enumerate(tarefas, 1):
        status = "✓" if tarefa["concluida"] else "○"
        print(f"  {i}. [{status}] {tarefa['descricao']}")
    print("-" * 25)


def concluir_tarefa(tarefas):
    """Marca uma tarefa como concluída"""
    listar_tarefas(tarefas)
    if len(tarefas) == 0:
        return

    try:
        numero = int(input("Número da tarefa para concluir: "))
        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            salvar_tarefas(tarefas)
            print("✓ Tarefa marcada como concluída!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite um número válido!")


def remover_tarefa(tarefas):
    """Remove uma tarefa da lista"""
    listar_tarefas(tarefas)
    if len(tarefas) == 0:
        return

    try:
        numero = int(input("Número da tarefa para remover: "))
        if 1 <= numero <= len(tarefas):
            removida = tarefas.pop(numero - 1)
            salvar_tarefas(tarefas)
            print(f"✓ Tarefa '{removida['descricao']}' removida!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite um número válido!")


# Carregar tarefas existentes
minhas_tarefas = carregar_tarefas()
print(f"\n{len(minhas_tarefas)} tarefa(s) carregada(s) do arquivo.")

# Menu principal
while True:
    print("\n--- MENU ---")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        adicionar_tarefa(minhas_tarefas)
    elif opcao == "2":
        listar_tarefas(minhas_tarefas)
    elif opcao == "3":
        concluir_tarefa(minhas_tarefas)
    elif opcao == "4":
        remover_tarefa(minhas_tarefas)
    elif opcao == "5":
        print(f"\nTarefas salvas em '{ARQUIVO_TAREFAS}'")
        print("Até logo!")
        break
    else:
        print("Opção inválida!")


# ============================================================
# DESAFIO EXTRA - DIÁRIO PESSOAL
# ============================================================

print("\n" + "=" * 50)
print("            DIÁRIO PESSOAL")
print("=" * 50)

from datetime import datetime

ARQUIVO_DIARIO = "diario.json"


def carregar_diario():
    if os.path.exists(ARQUIVO_DIARIO):
        with open(ARQUIVO_DIARIO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_diario(entradas):
    with open(ARQUIVO_DIARIO, "w", encoding="utf-8") as f:
        json.dump(entradas, f, indent=2, ensure_ascii=False)


def nova_entrada(diario):
    print("\nEscreva sua entrada do diário (digite 'FIM' para terminar):")
    linhas = []
    while True:
        linha = input()
        if linha.upper() == "FIM":
            break
        linhas.append(linha)

    if linhas:
        entrada = {
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "texto": "\n".join(linhas)
        }
        diario.append(entrada)
        salvar_diario(diario)
        print("✓ Entrada salva!")


def ver_entradas(diario):
    if len(diario) == 0:
        print("\nDiário vazio.")
        return

    print("\n--- ENTRADAS DO DIÁRIO ---")
    for i, entrada in enumerate(diario, 1):
        print(f"\n[{entrada['data']}]")
        print(entrada['texto'])
        print("-" * 30)


# Menu do diário
meu_diario = carregar_diario()

while True:
    print("\n--- DIÁRIO ---")
    print("1. Nova entrada")
    print("2. Ver entradas")
    print("3. Sair")

    op = input("Opção: ")

    if op == "1":
        nova_entrada(meu_diario)
    elif op == "2":
        ver_entradas(meu_diario)
    elif op == "3":
        print("Até logo!")
        break


# ============================================================
# LIMPEZA: Removendo arquivos de teste
# ============================================================
# Descomente para limpar os arquivos criados:
# import os
# for arquivo in ["meu_arquivo.txt", "mensagem.txt", "alunos.json", "config.json"]:
#     if os.path.exists(arquivo):
#         os.remove(arquivo)
#         print(f"Arquivo '{arquivo}' removido.")


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: Esquecer de fechar o arquivo
# arquivo = open("teste.txt", "w")
# arquivo.write("texto")
# # Esqueceu arquivo.close()!
# Solução: Use 'with' que fecha automaticamente

# ERRO 2: Abrir arquivo inexistente para leitura
# arquivo = open("nao_existe.txt", "r")  # ERRO!
# Solução: Verifique com os.path.exists() antes

# ERRO 3: Esquecer o encoding
# arquivo = open("texto.txt", "w")  # Pode dar erro com acentos
# Solução: open("texto.txt", "w", encoding="utf-8")

# ERRO 4: Usar "w" quando queria "a"
# "w" apaga todo o conteúdo existente!
# "a" adiciona ao final sem apagar


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ open() abre arquivos
# ✓ Modos: "r" (ler), "w" (escrever), "a" (adicionar)
# ✓ Use 'with' para fechar automaticamente
# ✓ .read() lê tudo, .readlines() lê como lista
# ✓ .write() escreve no arquivo
# ✓ JSON para salvar listas e dicionários
# ✓ json.dump() salva, json.load() carrega
# ✓ os.path.exists() verifica se arquivo existe
# ============================================================
