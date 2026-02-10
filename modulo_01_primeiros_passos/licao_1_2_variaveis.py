# ============================================================
# LIÇÃO 1.2 - VARIÁVEIS E PRINT()
# ============================================================
# Objetivo: Guardar informações em "caixas" chamadas variáveis
# Analogia: Variáveis são como caixas com etiquetas.
#           A etiqueta é o nome, o conteúdo pode mudar.
# ============================================================

# -----------------------------
# PARTE 1: Criando variáveis
# -----------------------------
# Uma variável guarda um valor para usar depois

nome = "Maria"
idade = 17
cidade = "São Paulo"

# Agora podemos usar esses valores:
print(nome)
print(idade)
print(cidade)


# -----------------------------
# PARTE 2: Mudando o conteúdo
# -----------------------------
# O conteúdo da caixa pode mudar, a etiqueta continua igual

cor_favorita = "azul"
print(cor_favorita)

cor_favorita = "verde"  # Mudou!
print(cor_favorita)

cor_favorita = "roxo"   # Mudou de novo!
print(cor_favorita)


# -----------------------------
# PARTE 3: Tipos de dados
# -----------------------------
# Existem diferentes tipos de conteúdo:

# TEXTO (string) - sempre entre aspas
nome_completo = "João Pedro Silva"
escola = "Escola Estadual Centro"

# NÚMERO INTEIRO (int) - sem aspas, sem vírgula
idade = 16
ano_nascimento = 2009

# NÚMERO DECIMAL (float) - usa ponto, não vírgula!
altura = 1.75
nota = 8.5

# Veja a diferença:
numero = 42       # Isso é um número
texto = "42"      # Isso é texto! (tem aspas)


# -----------------------------
# PARTE 4: f-strings (texto formatado)
# -----------------------------
# f-strings permitem misturar texto com variáveis
# Coloque 'f' antes das aspas e use {variável}

nome = "Carlos"
idade = 15

# Jeito ANTIGO (funciona, mas é feio):
print("Olá, meu nome é " + nome + " e tenho " + str(idade) + " anos.")

# Jeito MODERNO com f-string (muito mais fácil!):
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

# Mais exemplos de f-strings:
produto = "notebook"
preco = 2500.00
print(f"O {produto} custa R$ {preco}")

pontos = 85
total = 100
print(f"Você fez {pontos} de {total} pontos!")


# -----------------------------
# PARTE 5: Fazendo contas
# -----------------------------
# Com números, você pode fazer matemática!

idade_atual = 17
idade_futura = idade_atual + 10

print(f"Tenho {idade_atual} anos agora.")
print(f"Daqui a 10 anos terei {idade_futura} anos.")

# Operações matemáticas básicas:
a = 10
b = 3

soma = a + b           # 13
subtracao = a - b      # 7
multiplicacao = a * b  # 30
divisao = a / b        # 3.333...

print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} × {b} = {multiplicacao}")
print(f"{a} ÷ {b} = {divisao}")


# ============================================================
# EXERCÍCIO 1.2 - Saudação Personalizada
# ============================================================
# Crie um programa que:
# 1. Guarda seu nome em uma variável
# 2. Guarda sua idade em outra variável
# 3. Calcula sua idade daqui a 10 anos
# 4. Mostra uma mensagem personalizada
#
# Exemplo de saída:
# "Olá, Maria! Você tem 16 anos."
# "Daqui a 10 anos você terá 26 anos."
# -----------------------------

print("\n------- Exercício 1.2 -------")

# Suas variáveis aqui:
meu_nome = "Ana"
minha_idade = 16
idade_em_10_anos = minha_idade + 10

# Suas mensagens aqui:
print(f"Olá, {meu_nome}! Você tem {minha_idade} anos.")
print(f"Daqui a 10 anos você terá {idade_em_10_anos} anos.")

print("-" * 30)


# ============================================================
# DESAFIO EXTRA
# ============================================================
# Crie um "cartão de identidade" com várias informações:

print("\n===== CARTÃO DE IDENTIDADE =====")

nome_aluno = "Pedro Santos"
idade_aluno = 17
serie = "3º ano"
escola_aluno = "E.E. Professor Lima"
materia_favorita = "Matemática"
sonho = "Ser programador"

print(f"Nome: {nome_aluno}")
print(f"Idade: {idade_aluno} anos")
print(f"Série: {serie}")
print(f"Escola: {escola_aluno}")
print(f"Matéria favorita: {materia_favorita}")
print(f"Sonho: {sonho}")

print("=" * 32)


# ============================================================
# ERROS COMUNS (para aprender com eles)
# ============================================================

# ERRO 1: Misturar texto com número sem f-string
# idade = 16
# print("Tenho " + idade + " anos")  # ERRO! Não pode somar texto com número

# ERRO 2: Esquecer as aspas em texto
# nome = Maria  # ERRO! Precisa de aspas: nome = "Maria"

# ERRO 3: Usar vírgula em vez de ponto em decimais
# altura = 1,75  # ERRO! Use ponto: altura = 1.75


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ Variáveis guardam valores (como caixas com etiquetas)
# ✓ Texto usa aspas "", números não
# ✓ f-strings facilitam misturar texto e variáveis
# ✓ Você pode fazer contas com variáveis numéricas
# ✓ O valor de uma variável pode mudar
# ============================================================
