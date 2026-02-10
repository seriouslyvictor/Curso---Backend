# ============================================================
# LIÇÃO 1.5 - LISTAS E COLEÇÕES DO DIA A DIA
# ============================================================
# Objetivo: Trabalhar com coleções de dados (listas)
# Analogia: Uma playlist é uma lista de músicas.
#           Você pode adicionar, remover e reorganizar músicas.
# ============================================================

# -----------------------------
# PARTE 1: Criando listas
# -----------------------------
# Listas guardam vários valores em uma única variável

# Uma lista de frutas
frutas = ["maçã", "banana", "laranja", "uva"]
print("Minhas frutas:", frutas)

# Uma lista de números
notas = [8.5, 7.0, 9.2, 6.8, 10.0]
print("Minhas notas:", notas)

# Uma lista vazia (para preencher depois)
compras = []
print("Lista de compras:", compras)

# Listas podem misturar tipos (mas evite fazer isso)
misturada = ["João", 25, True, 1.75]


# -----------------------------
# PARTE 2: Acessando itens (índices)
# -----------------------------
# Cada item tem uma posição (índice), começando do ZERO!

#                0         1         2        3
alunos = ["Ana", "Bruno", "Carla", "Daniel"]

print("\n=== Acessando itens ===")
print(f"Primeiro aluno: {alunos[0]}")   # Ana
print(f"Segundo aluno: {alunos[1]}")    # Bruno
print(f"Terceiro aluno: {alunos[2]}")   # Carla
print(f"Quarto aluno: {alunos[3]}")     # Daniel

# Índices negativos contam do final!
print(f"Último aluno: {alunos[-1]}")    # Daniel
print(f"Penúltimo: {alunos[-2]}")       # Carla


# -----------------------------
# PARTE 3: Modificando itens
# -----------------------------
# Você pode mudar um item específico

cores = ["vermelho", "azul", "verde"]
print(f"\nAntes: {cores}")

cores[1] = "amarelo"  # Muda "azul" para "amarelo"
print(f"Depois: {cores}")


# -----------------------------
# PARTE 4: Adicionando itens
# -----------------------------
# .append() adiciona no final
# .insert() adiciona em posição específica

tarefas = ["estudar", "limpar"]
print(f"\n=== Adicionando itens ===")
print(f"Inicial: {tarefas}")

tarefas.append("exercitar")  # Adiciona no final
print(f"Após append: {tarefas}")

tarefas.insert(0, "acordar")  # Adiciona na posição 0 (início)
print(f"Após insert: {tarefas}")


# -----------------------------
# PARTE 5: Removendo itens
# -----------------------------
# .remove() remove pelo valor
# .pop() remove pela posição (ou o último)
# del remove pela posição

animais = ["gato", "cachorro", "pássaro", "peixe"]
print(f"\n=== Removendo itens ===")
print(f"Inicial: {animais}")

animais.remove("pássaro")  # Remove pelo nome
print(f"Após remove: {animais}")

animal_removido = animais.pop()  # Remove e retorna o último
print(f"Removido com pop: {animal_removido}")
print(f"Lista agora: {animais}")

animais.pop(0)  # Remove o primeiro (índice 0)
print(f"Após pop(0): {animais}")


# -----------------------------
# PARTE 6: Operações úteis
# -----------------------------

numeros = [5, 2, 8, 1, 9, 3, 7]

print("\n=== Operações úteis ===")
print(f"Lista: {numeros}")
print(f"Tamanho (len): {len(numeros)}")    # Quantos itens
print(f"Maior (max): {max(numeros)}")       # Maior valor
print(f"Menor (min): {min(numeros)}")       # Menor valor
print(f"Soma (sum): {sum(numeros)}")        # Soma todos

# Verificar se item existe
if 8 in numeros:
    print("O número 8 está na lista!")

if 100 not in numeros:
    print("O número 100 NÃO está na lista.")

# Ordenar
numeros.sort()  # Ordena a lista original
print(f"Ordenada: {numeros}")

numeros.reverse()  # Inverte a ordem
print(f"Invertida: {numeros}")


# -----------------------------
# PARTE 7: Percorrendo listas
# -----------------------------

print("\n=== Percorrendo listas ===")

comidas = ["pizza", "hambúrguer", "sushi", "açaí"]

# Jeito simples
print("Minhas comidas favoritas:")
for comida in comidas:
    print(f"  - {comida}")

# Com índice (quando você precisa saber a posição)
print("\nCom posição:")
for i, comida in enumerate(comidas):
    print(f"  {i + 1}. {comida}")


# ============================================================
# EXERCÍCIO 1.5 - LISTA DE COMPRAS
# ============================================================
# Crie um gerenciador de lista de compras que permite:
# - Adicionar itens
# - Remover itens
# - Ver a lista completa
# - Ver quantos itens tem

print("\n" + "=" * 50)
print("       GERENCIADOR DE LISTA DE COMPRAS")
print("=" * 50)

# Nossa lista de compras (começa vazia)
lista_compras = []

# O programa vai rodar até o usuário escolher sair
continuar = True

while continuar:
    print("\n--- MENU ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Ver lista")
    print("4. Sair")

    opcao = input("\nEscolha uma opção (1-4): ")

    if opcao == "1":
        # ADICIONAR ITEM
        item = input("Digite o item para adicionar: ")
        lista_compras.append(item)
        print(f"✓ '{item}' foi adicionado à lista!")

    elif opcao == "2":
        # REMOVER ITEM
        if len(lista_compras) == 0:
            print("A lista está vazia!")
        else:
            item = input("Digite o item para remover: ")
            if item in lista_compras:
                lista_compras.remove(item)
                print(f"✓ '{item}' foi removido da lista!")
            else:
                print(f"✗ '{item}' não está na lista.")

    elif opcao == "3":
        # VER LISTA
        if len(lista_compras) == 0:
            print("\n📝 A lista está vazia!")
        else:
            print(f"\n📝 LISTA DE COMPRAS ({len(lista_compras)} itens):")
            print("-" * 30)
            for i, item in enumerate(lista_compras, 1):
                print(f"  {i}. {item}")
            print("-" * 30)

    elif opcao == "4":
        # SAIR
        print("\nAté logo! 👋")
        continuar = False

    else:
        print("Opção inválida! Digite 1, 2, 3 ou 4.")


# ============================================================
# DESAFIO EXTRA - Sistema de Notas
# ============================================================

print("\n" + "=" * 50)
print("         CALCULADORA DE MÉDIA")
print("=" * 50)

notas_aluno = []

print("\nDigite as notas do aluno (ou 'fim' para calcular):\n")

while True:
    entrada = input("Nota: ")

    if entrada.lower() == "fim":
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas_aluno.append(nota)
            print(f"  ✓ Nota {nota} adicionada")
        else:
            print("  ✗ A nota deve ser entre 0 e 10")
    except ValueError:
        print("  ✗ Digite um número válido ou 'fim'")

# Calcular resultados
if len(notas_aluno) > 0:
    media = sum(notas_aluno) / len(notas_aluno)
    maior_nota = max(notas_aluno)
    menor_nota = min(notas_aluno)

    print("\n" + "-" * 30)
    print(f"Notas: {notas_aluno}")
    print(f"Quantidade de notas: {len(notas_aluno)}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Média: {media:.1f}")
    print("-" * 30)

    if media >= 7:
        print("Resultado: APROVADO ✓")
    elif media >= 5:
        print("Resultado: RECUPERAÇÃO")
    else:
        print("Resultado: REPROVADO ✗")
else:
    print("\nNenhuma nota foi digitada!")


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: Acessar índice que não existe
# lista = ["a", "b", "c"]
# print(lista[3])  # ERRO! Só existe 0, 1, 2

# ERRO 2: Esquecer que índice começa em 0
# lista = ["primeiro", "segundo", "terceiro"]
# lista[1]  # Isso é "segundo", não "primeiro"!

# ERRO 3: Modificar lista enquanto percorre
# for item in lista:
#     lista.remove(item)  # Pode causar problemas!


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ Listas guardam múltiplos valores: [a, b, c]
# ✓ Índices começam em 0: lista[0] é o primeiro
# ✓ append() adiciona no final
# ✓ remove() remove pelo valor
# ✓ pop() remove pela posição
# ✓ len() conta quantos itens
# ✓ in verifica se item existe
# ✓ for item in lista: percorre cada item
# ============================================================
