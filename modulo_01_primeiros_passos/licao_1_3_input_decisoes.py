# ============================================================
# LIÇÃO 1.3 - INPUT E DECISÕES SIMPLES
# ============================================================
# Objetivo: Fazer o programa conversar com o usuário e
#           tomar decisões baseadas nas respostas
# Analogia: Seu cérebro faz decisões o dia todo:
#           "Se está chovendo, levo guarda-chuva"
#           O computador faz a mesma coisa!
# ============================================================

# -----------------------------
# PARTE 1: Recebendo dados do usuário
# -----------------------------
# input() faz o programa parar e esperar você digitar algo

print("=== Parte 1: Conhecendo o input() ===")

nome = input("Qual é o seu nome? ")
print(f"Prazer em conhecer você, {nome}!")

# ATENÇÃO: input() SEMPRE retorna TEXTO (string)
# Mesmo que você digite um número, ele vem como texto!


# -----------------------------
# PARTE 2: Convertendo texto em número
# -----------------------------
# Para fazer contas, precisamos converter texto para número

print("\n=== Parte 2: Convertendo para número ===")

idade_texto = input("Quantos anos você tem? ")
idade_numero = int(idade_texto)  # int() converte para número inteiro

# Agora podemos fazer contas!
idade_daqui_5_anos = idade_numero + 5
print(f"Daqui a 5 anos você terá {idade_daqui_5_anos} anos!")

# Jeito mais curto (converter direto):
# idade = int(input("Quantos anos você tem? "))


# -----------------------------
# PARTE 3: Tomando decisões com IF
# -----------------------------
# if = "se" em inglês
# O código dentro do if só roda SE a condição for verdadeira

print("\n=== Parte 3: Decisões simples ===")

temperatura = int(input("Qual a temperatura lá fora? "))

if temperatura > 30:
    print("Está muito quente! Beba água.")

if temperatura < 15:
    print("Está frio! Leve um casaco.")

# Note a INDENTAÇÃO (espaços antes do print)
# Tudo que está "dentro" do if precisa ter espaços


# -----------------------------
# PARTE 4: IF com ELSE (senão)
# -----------------------------
# else = "senão" - o que acontece quando a condição é falsa

print("\n=== Parte 4: Se... Senão... ===")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade.")


# -----------------------------
# PARTE 5: ELIF (senão se)
# -----------------------------
# elif = "else if" = "senão se"
# Usado quando há várias possibilidades

print("\n=== Parte 5: Várias condições ===")

nota = float(input("Qual foi sua nota? "))  # float() para decimais

if nota >= 9:
    print("Excelente! Conceito A")
elif nota >= 7:
    print("Bom! Conceito B")
elif nota >= 5:
    print("Regular. Conceito C")
else:
    print("Precisa estudar mais. Conceito D")


# -----------------------------
# PARTE 6: Operadores de comparação
# -----------------------------
# ==  igual a (DOIS sinais de igual!)
# !=  diferente de
# >   maior que
# <   menor que
# >=  maior ou igual
# <=  menor ou igual

print("\n=== Parte 6: Comparações ===")

numero = int(input("Digite um número: "))

if numero == 0:
    print("Você digitou zero!")
elif numero > 0:
    print("Número positivo")
else:
    print("Número negativo")

# Comparando texto:
resposta = input("Você gosta de programar? (sim/não) ")

if resposta == "sim":
    print("Que ótimo! Você está no lugar certo!")
elif resposta == "não":
    print("Talvez mude de ideia depois dessa aula! 😊")
else:
    print("Não entendi sua resposta...")


# ============================================================
# EXERCÍCIO 1.3 - Verificador de Idade
# ============================================================
# Crie um programa que:
# 1. Pergunta a idade da pessoa
# 2. Informa se ela pode:
#    - Votar (16 anos ou mais)
#    - Dirigir (18 anos ou mais)
#    - Ser presidente (35 anos ou mais)
# -----------------------------

print("\n" + "=" * 50)
print("      VERIFICADOR DE IDADE - SEUS DIREITOS")
print("=" * 50)

idade_usuario = int(input("\nDigite sua idade: "))

print(f"\nCom {idade_usuario} anos, você:")

# Verifica se pode votar
if idade_usuario >= 16:
    print("✓ PODE votar")
else:
    faltam = 16 - idade_usuario
    print(f"✗ NÃO pode votar ainda (faltam {faltam} anos)")

# Verifica se pode dirigir
if idade_usuario >= 18:
    print("✓ PODE tirar carteira de motorista")
else:
    faltam = 18 - idade_usuario
    print(f"✗ NÃO pode dirigir ainda (faltam {faltam} anos)")

# Verifica se pode ser presidente
if idade_usuario >= 35:
    print("✓ PODE se candidatar a Presidente da República")
else:
    faltam = 35 - idade_usuario
    print(f"✗ NÃO pode ser presidente ainda (faltam {faltam} anos)")

print()


# ============================================================
# DESAFIO EXTRA - Calculadora de IMC
# ============================================================
# O IMC (Índice de Massa Corporal) é calculado assim:
# IMC = peso / (altura * altura)
#
# Classificação:
# Abaixo de 18.5 = Abaixo do peso
# 18.5 a 24.9 = Peso normal
# 25 a 29.9 = Sobrepeso
# 30 ou mais = Obesidade

print("=" * 40)
print("      CALCULADORA DE IMC")
print("=" * 40)

peso = float(input("Seu peso em kg (ex: 70.5): "))
altura = float(input("Sua altura em metros (ex: 1.75): "))

# Cálculo do IMC
imc = peso / (altura * altura)

print(f"\nSeu IMC é: {imc:.1f}")  # :.1f = 1 casa decimal

# Classificação
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: Esquecer de converter input para número
# idade = input("Idade: ")
# if idade > 18:  # ERRO! Comparando texto com número
# Correto: idade = int(input("Idade: "))

# ERRO 2: Usar = em vez de == para comparar
# if idade = 18:  # ERRO! Isso é atribuição, não comparação
# Correto: if idade == 18:

# ERRO 3: Esquecer os dois pontos :
# if idade >= 18  # ERRO! Falta o :
# Correto: if idade >= 18:

# ERRO 4: Esquecer a indentação (espaços)
# if idade >= 18:
# print("Maior")  # ERRO! Precisa de espaços antes
# Correto:
# if idade >= 18:
#     print("Maior")


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ input() recebe dados do usuário (sempre como texto)
# ✓ int() converte texto para número inteiro
# ✓ float() converte texto para número decimal
# ✓ if/elif/else toma decisões baseadas em condições
# ✓ Operadores: == != > < >= <=
# ✓ Indentação (espaços) indica o que está "dentro" do if
# ============================================================
