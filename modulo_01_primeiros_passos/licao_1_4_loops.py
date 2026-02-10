# ============================================================
# LIÇÃO 1.4 - AÇÕES REPETIDAS: LOOPS
# ============================================================
# Objetivo: Fazer o computador repetir tarefas automaticamente
# Analogia: Quando você manda a mesma mensagem para 10 amigos,
#           você não escreve 10 vezes. Loops fazem isso!
# ============================================================

# -----------------------------
# PARTE 1: Por que loops?
# -----------------------------
# Imagine imprimir "Olá!" 5 vezes sem loop:

print("Sem loop (repetitivo e chato):")
print("Olá!")
print("Olá!")
print("Olá!")
print("Olá!")
print("Olá!")

# E se fossem 100 vezes? 1000 vezes? Impossível!
# Loops resolvem isso.


# -----------------------------
# PARTE 2: O loop FOR
# -----------------------------
# for = "para cada" - repete um número definido de vezes

print("\n=== Loop FOR ===")

# range(5) cria uma sequência: 0, 1, 2, 3, 4
for i in range(5):
    print(f"Esta é a repetição número {i}")

# Note: range(5) vai de 0 até 4 (não inclui o 5!)


# Podemos escolher onde começar e onde terminar:
print("\nContando de 1 até 5:")
for numero in range(1, 6):  # Começa em 1, para antes do 6
    print(numero)

# Podemos pular números:
print("\nNúmeros pares de 0 a 10:")
for numero in range(0, 11, 2):  # De 0 a 10, pulando de 2 em 2
    print(numero)


# -----------------------------
# PARTE 3: FOR com listas
# -----------------------------
# Podemos percorrer uma lista de coisas

print("\n=== FOR com listas ===")

frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in frutas:
    print(f"Eu gosto de {fruta}!")

# Outro exemplo: nomes de amigos
amigos = ["Ana", "Carlos", "Maria", "João"]

print("\nMandando mensagem para todos os amigos:")
for amigo in amigos:
    print(f"Olá, {amigo}! Tudo bem?")


# -----------------------------
# PARTE 4: O loop WHILE
# -----------------------------
# while = "enquanto" - repete ENQUANTO uma condição for verdadeira

print("\n=== Loop WHILE ===")

# Exemplo: contagem regressiva
contador = 5

while contador > 0:
    print(contador)
    contador = contador - 1  # Diminui 1 a cada vez

print("Lançar! 🚀")

# CUIDADO: Se a condição nunca ficar falsa, o loop é infinito!
# Sempre garanta que a condição vai mudar.


# -----------------------------
# PARTE 5: Acumuladores
# -----------------------------
# Podemos usar loops para somar, contar, etc.

print("\n=== Somando números ===")

# Somar todos os números de 1 a 10
soma = 0  # Começa do zero

for numero in range(1, 11):
    soma = soma + numero
    print(f"Somando {numero}... Total: {soma}")

print(f"Soma final: {soma}")


# Contando quantos números são pares
print("\nContando números pares de 1 a 20:")
quantidade_pares = 0

for numero in range(1, 21):
    if numero % 2 == 0:  # % é o resto da divisão. Se resto é 0, é par!
        quantidade_pares = quantidade_pares + 1

print(f"Existem {quantidade_pares} números pares entre 1 e 20")


# -----------------------------
# PARTE 6: break e continue
# -----------------------------
# break = para o loop imediatamente
# continue = pula para a próxima repetição

print("\n=== break e continue ===")

# Procurando um número específico (break)
print("Procurando o número 7:")
for numero in range(1, 20):
    if numero == 7:
        print("Encontrei o 7! Parando...")
        break
    print(f"Verificando {numero}...")

# Pulando números ímpares (continue)
print("\nImprimindo só os pares:")
for numero in range(1, 11):
    if numero % 2 != 0:  # Se for ímpar
        continue  # Pula para o próximo
    print(numero)


# ============================================================
# EXERCÍCIO 1.4A - Tabuada
# ============================================================
# O usuário escolhe um número e você mostra a tabuada completa

print("\n" + "=" * 40)
print("        GERADOR DE TABUADA")
print("=" * 40)

numero = int(input("\nDigite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
print("-" * 20)

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")


# ============================================================
# EXERCÍCIO 1.4B - Contagem Regressiva
# ============================================================
# Crie uma contagem regressiva de 10 até 0 com "Lançamento!"

print("\n" + "=" * 40)
print("      CONTAGEM REGRESSIVA ESPACIAL")
print("=" * 40)

print("\nPreparando lançamento...")
print()

contador = 10

while contador >= 0:
    if contador == 0:
        print("🚀 LANÇAMENTO! 🚀")
    else:
        print(f"   {contador}...")
    contador = contador - 1

print("\nFoguete em órbita! Missão cumprida!")


# ============================================================
# DESAFIO EXTRA - Jogo de Adivinhação
# ============================================================
# O computador "pensa" em um número e você tenta adivinhar

import random  # Biblioteca para gerar números aleatórios

print("\n" + "=" * 40)
print("      JOGO DE ADIVINHAÇÃO")
print("=" * 40)

numero_secreto = random.randint(1, 20)  # Número entre 1 e 20
tentativas = 0
acertou = False

print("\nPensei em um número entre 1 e 20.")
print("Tente adivinhar!\n")

while not acertou:
    palpite = int(input("Seu palpite: "))
    tentativas = tentativas + 1

    if palpite == numero_secreto:
        acertou = True
        print(f"\n🎉 Parabéns! Você acertou em {tentativas} tentativas!")
    elif palpite < numero_secreto:
        print("📈 Muito baixo! Tente um número maior.")
    else:
        print("📉 Muito alto! Tente um número menor.")


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: Esquecer de atualizar a variável no while
# contador = 5
# while contador > 0:
#     print(contador)
#     # Esqueceu: contador = contador - 1
#     # Isso causa loop infinito!

# ERRO 2: Confundir range()
# range(5) = 0, 1, 2, 3, 4 (não inclui o 5!)
# range(1, 5) = 1, 2, 3, 4 (começa em 1, não inclui 5)
# range(0, 10, 2) = 0, 2, 4, 6, 8 (de 2 em 2)

# ERRO 3: Esquecer a indentação
# for i in range(5):
# print(i)  # ERRO! Precisa de espaços


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ for loop: repete um número definido de vezes
# ✓ range(n): gera números de 0 até n-1
# ✓ range(início, fim): gera de início até fim-1
# ✓ for item in lista: percorre cada item de uma lista
# ✓ while loop: repete enquanto condição for verdadeira
# ✓ Acumuladores: variáveis que somam/contam durante o loop
# ✓ break: para o loop
# ✓ continue: pula para próxima iteração
# ============================================================
