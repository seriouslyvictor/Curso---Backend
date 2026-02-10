# ============================================================
# LIÇÃO 2.1 - FUNÇÕES: RECEITAS REUTILIZÁVEIS
# ============================================================
# Objetivo: Criar blocos de código que podem ser reutilizados
# Analogia: Uma receita de bolo ensina como fazer um bolo.
#           Você não reescreve a receita toda vez - só segue!
#           Funções são receitas para o computador.
# ============================================================

# -----------------------------
# PARTE 1: Por que funções?
# -----------------------------
# Imagine que você quer cumprimentar várias pessoas.
# Sem função, você repetiria código:

print("=== SEM FUNÇÃO (repetitivo) ===")
print("Olá, Maria!")
print("Seja bem-vinda ao nosso programa!")
print("-" * 30)

print("Olá, João!")
print("Seja bem-vindo ao nosso programa!")
print("-" * 30)

print("Olá, Ana!")
print("Seja bem-vinda ao nosso programa!")
print("-" * 30)

# Muito código repetido! Vamos melhorar com função.


# -----------------------------
# PARTE 2: Criando sua primeira função
# -----------------------------
# def = "define" uma função
# O código dentro só roda quando você CHAMA a função

print("\n=== COM FUNÇÃO (organizado) ===")

def saudar():
    """Esta função mostra uma saudação genérica"""
    print("Olá! Seja bem-vindo ao nosso programa!")
    print("-" * 30)

# Chamando a função 3 vezes:
saudar()
saudar()
saudar()


# -----------------------------
# PARTE 3: Funções com parâmetros
# -----------------------------
# Parâmetros são "ingredientes" que a função precisa

print("\n=== FUNÇÃO COM PARÂMETRO ===")

def saudar_pessoa(nome):
    """Sauda uma pessoa específica pelo nome"""
    print(f"Olá, {nome}!")
    print("Seja bem-vindo ao nosso programa!")
    print("-" * 30)

# Agora podemos personalizar:
saudar_pessoa("Maria")
saudar_pessoa("João")
saudar_pessoa("Carlos")


# Função com múltiplos parâmetros:
def apresentar(nome, idade, cidade):
    """Apresenta uma pessoa com várias informações"""
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Cidade: {cidade}")
    print()

apresentar("Ana", 17, "São Paulo")
apresentar("Pedro", 16, "Rio de Janeiro")


# -----------------------------
# PARTE 4: Funções que retornam valores
# -----------------------------
# return = a função "devolve" um resultado

print("=== FUNÇÃO COM RETURN ===")

def somar(a, b):
    """Soma dois números e retorna o resultado"""
    resultado = a + b
    return resultado

# Usando a função:
total = somar(5, 3)
print(f"5 + 3 = {total}")

# Podemos usar direto no print:
print(f"10 + 20 = {somar(10, 20)}")

# Ou em outras operações:
x = somar(100, 50)
y = somar(x, 25)
print(f"Resultado encadeado: {y}")


# Mais exemplos de return:
def dobrar(numero):
    """Retorna o dobro de um número"""
    return numero * 2

def eh_maior_de_idade(idade):
    """Retorna True se maior de idade, False se não"""
    return idade >= 18

def calcular_media(nota1, nota2, nota3):
    """Calcula a média de três notas"""
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return media

print(f"\nDobro de 7: {dobrar(7)}")
print(f"15 anos é maior de idade? {eh_maior_de_idade(15)}")
print(f"21 anos é maior de idade? {eh_maior_de_idade(21)}")
print(f"Média de 8, 7, 9: {calcular_media(8, 7, 9):.1f}")


# -----------------------------
# PARTE 5: Parâmetros com valor padrão
# -----------------------------
# Você pode definir valores padrão para parâmetros

print("\n=== PARÂMETROS COM VALOR PADRÃO ===")

def potencia(base, expoente=2):
    """Calcula base elevada ao expoente (padrão: ao quadrado)"""
    return base ** expoente

# Se não passar expoente, usa o padrão (2):
print(f"5² = {potencia(5)}")
print(f"5³ = {potencia(5, 3)}")
print(f"2¹⁰ = {potencia(2, 10)}")


def criar_email(nome, dominio="gmail.com"):
    """Cria um email. Domínio padrão é gmail.com"""
    nome_limpo = nome.lower().replace(" ", ".")
    return f"{nome_limpo}@{dominio}"

print(f"\nEmail: {criar_email('Maria Silva')}")
print(f"Email: {criar_email('João Pedro', 'hotmail.com')}")


# -----------------------------
# PARTE 6: Funções chamando funções
# -----------------------------
# Funções podem usar outras funções!

print("\n=== FUNÇÕES CHAMANDO FUNÇÕES ===")

def calcular_area_quadrado(lado):
    """Calcula área do quadrado"""
    return lado * lado

def calcular_area_retangulo(largura, altura):
    """Calcula área do retângulo"""
    return largura * altura

def calcular_area_triangulo(base, altura):
    """Calcula área do triângulo"""
    return (base * altura) / 2

def mostrar_areas():
    """Mostra várias áreas calculadas"""
    print("Áreas calculadas:")
    print(f"  Quadrado (lado 5): {calcular_area_quadrado(5)}")
    print(f"  Retângulo (4x6): {calcular_area_retangulo(4, 6)}")
    print(f"  Triângulo (base 8, altura 3): {calcular_area_triangulo(8, 3)}")

mostrar_areas()


# ============================================================
# EXERCÍCIO 2.1 - CALCULADORA COM FUNÇÕES
# ============================================================
# Crie uma calculadora com funções separadas para cada operação

print("\n" + "=" * 50)
print("          CALCULADORA COM FUNÇÕES")
print("=" * 50)


def adicionar(a, b):
    """Soma dois números"""
    return a + b


def subtrair(a, b):
    """Subtrai b de a"""
    return a - b


def multiplicar(a, b):
    """Multiplica dois números"""
    return a * b


def dividir(a, b):
    """Divide a por b. Retorna mensagem se dividir por zero"""
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


def mostrar_menu():
    """Mostra o menu de opções"""
    print("\n--- MENU ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
    print("-" * 12)


def obter_numeros():
    """Pede dois números ao usuário e retorna eles"""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2  # Retorna dois valores!


# Loop principal da calculadora
continuar = True

while continuar:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("\nAté logo!")
        continuar = False

    elif opcao in ["1", "2", "3", "4"]:
        num1, num2 = obter_numeros()

        if opcao == "1":
            resultado = adicionar(num1, num2)
            print(f"\n{num1} + {num2} = {resultado}")

        elif opcao == "2":
            resultado = subtrair(num1, num2)
            print(f"\n{num1} - {num2} = {resultado}")

        elif opcao == "3":
            resultado = multiplicar(num1, num2)
            print(f"\n{num1} × {num2} = {resultado}")

        elif opcao == "4":
            resultado = dividir(num1, num2)
            print(f"\n{num1} ÷ {num2} = {resultado}")

    else:
        print("\nOpção inválida!")


# ============================================================
# DESAFIO EXTRA - Calculadora de Notas
# ============================================================

print("\n" + "=" * 50)
print("        CALCULADORA DE NOTAS")
print("=" * 50)


def calcular_media_ponderada(nota1, nota2, nota3, peso1=1, peso2=1, peso3=1):
    """Calcula média ponderada de três notas"""
    soma_pesos = peso1 + peso2 + peso3
    soma_notas = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
    return soma_notas / soma_pesos


def determinar_situacao(media):
    """Retorna a situação do aluno baseada na média"""
    if media >= 7:
        return "APROVADO"
    elif media >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"


def mostrar_boletim(nome, n1, n2, n3):
    """Mostra o boletim completo do aluno"""
    media = calcular_media_ponderada(n1, n2, n3)
    situacao = determinar_situacao(media)

    print(f"\n{'=' * 35}")
    print(f"  BOLETIM - {nome.upper()}")
    print(f"{'=' * 35}")
    print(f"  Nota 1: {n1}")
    print(f"  Nota 2: {n2}")
    print(f"  Nota 3: {n3}")
    print(f"  Média: {media:.1f}")
    print(f"  Situação: {situacao}")
    print(f"{'=' * 35}")


# Testando:
mostrar_boletim("Maria Silva", 8.5, 7.0, 9.0)
mostrar_boletim("João Pedro", 5.0, 4.5, 6.0)
mostrar_boletim("Ana Santos", 3.0, 4.0, 2.5)


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: Esquecer os parênteses ao chamar função
# saudar  # Isso não chama a função! Precisa: saudar()

# ERRO 2: Esquecer o return
# def somar(a, b):
#     resultado = a + b
#     # Esqueceu o return! A função retorna None

# ERRO 3: Usar variável de dentro da função fora dela
# def exemplo():
#     x = 10
# print(x)  # ERRO! x só existe dentro da função

# ERRO 4: Ordem errada de parâmetros com valor padrão
# def funcao(a=1, b):  # ERRO! Padrão deve vir depois
# Correto: def funcao(b, a=1):


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ def cria uma função
# ✓ Parâmetros são "ingredientes" da função
# ✓ return devolve um resultado
# ✓ Parâmetros podem ter valores padrão
# ✓ Funções podem chamar outras funções
# ✓ Código fica mais organizado e reutilizável
# ============================================================
