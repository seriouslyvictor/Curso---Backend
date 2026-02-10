# ============================================================
# LIÇÃO 2.4 - TRATAMENTO DE ERROS
# ============================================================
# Objetivo: Fazer programas que não "quebram" com entradas erradas
# Motivação: O que acontece quando o usuário digita "abc" quando
#            você espera um número? O programa QUEBRA!
#            Vamos aprender a evitar isso.
# ============================================================

# -----------------------------
# PARTE 1: O problema
# -----------------------------
# Veja o que acontece quando algo dá errado:

print("=== O PROBLEMA ===")
print("Quando algo inesperado acontece, o programa para!")
print("Exemplos de erros comuns:\n")

# Descomente cada linha para ver o erro:

# ERRO 1: Converter texto para número
# numero = int("abc")  # ValueError!

# ERRO 2: Dividir por zero
# resultado = 10 / 0  # ZeroDivisionError!

# ERRO 3: Acessar índice que não existe
# lista = [1, 2, 3]
# print(lista[10])  # IndexError!

# ERRO 4: Acessar chave que não existe
# dicionario = {"nome": "Ana"}
# print(dicionario["idade"])  # KeyError!

# ERRO 5: Arquivo que não existe
# arquivo = open("arquivo_que_nao_existe.txt")  # FileNotFoundError!


# -----------------------------
# PARTE 2: try/except - A solução
# -----------------------------
# try = "tente fazer isso"
# except = "se der erro, faça isso em vez de quebrar"

print("\n=== TRY/EXCEPT BÁSICO ===")

# Sem tratamento (quebra):
# numero = int(input("Digite um número: "))

# Com tratamento (não quebra):
try:
    texto = "abc"
    numero = int(texto)
    print(f"O número é: {numero}")
except:
    print("Erro! Isso não é um número válido.")

print("O programa continuou rodando normalmente!")


# -----------------------------
# PARTE 3: Capturando erros específicos
# -----------------------------
# É melhor tratar cada tipo de erro de forma diferente

print("\n=== ERROS ESPECÍFICOS ===")

def dividir(a, b):
    """Divide a por b com tratamento de erros"""
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
        return None
    except TypeError:
        print("Erro: Os valores precisam ser números!")
        return None

print(f"10 / 2 = {dividir(10, 2)}")
print(f"10 / 0 = {dividir(10, 0)}")
print(f"'10' / 2 = {dividir('10', 2)}")


# -----------------------------
# PARTE 4: else e finally
# -----------------------------
# else = roda se NÃO houve erro
# finally = roda SEMPRE (tendo erro ou não)

print("\n=== ELSE E FINALLY ===")

def ler_arquivo(nome):
    """Tenta ler um arquivo e mostra seu conteúdo"""
    try:
        arquivo = open(nome, "r", encoding="utf-8")
        conteudo = arquivo.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome}' não encontrado!")
    else:
        # Só roda se não houve erro
        print(f"Conteúdo do arquivo:\n{conteudo}")
    finally:
        # Sempre roda (útil para limpeza)
        print("Tentativa de leitura finalizada.\n")

# Primeiro, criamos um arquivo de teste:
with open("teste.txt", "w") as f:
    f.write("Olá! Este é um teste.")

ler_arquivo("teste.txt")        # Vai funcionar
ler_arquivo("nao_existe.txt")   # Vai dar erro (mas não quebra)


# -----------------------------
# PARTE 5: Entrada segura do usuário
# -----------------------------
# Vamos criar uma função que pede números até o usuário digitar certo

print("=== ENTRADA SEGURA ===")

def pedir_numero(mensagem):
    """Pede um número ao usuário até ele digitar corretamente"""
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Isso não é um número válido! Tente novamente.\n")

def pedir_inteiro(mensagem):
    """Pede um número inteiro ao usuário"""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Digite apenas números inteiros!\n")

# Teste:
# idade = pedir_inteiro("Digite sua idade: ")
# print(f"Você tem {idade} anos.")


# -----------------------------
# PARTE 6: Criando suas próprias exceções
# -----------------------------
# Você pode criar erros personalizados!

print("\n=== VALIDAÇÃO PERSONALIZADA ===")

def validar_idade(idade):
    """Valida se a idade faz sentido"""
    if idade < 0:
        raise ValueError("Idade não pode ser negativa!")
    if idade > 150:
        raise ValueError("Idade muito alta! (máximo 150)")
    return True

# Testando:
try:
    validar_idade(25)
    print("Idade 25: Válida!")

    validar_idade(-5)
    print("Idade -5: Válida!")  # Não vai chegar aqui
except ValueError as erro:
    print(f"Idade -5: {erro}")

try:
    validar_idade(200)
except ValueError as erro:
    print(f"Idade 200: {erro}")


# -----------------------------
# PARTE 7: Mensagens de erro úteis
# -----------------------------
# Podemos capturar a mensagem do erro para mostrar ao usuário

print("\n=== MENSAGENS DE ERRO ===")

def processar_dados(dados):
    try:
        # Várias operações que podem falhar
        numero = int(dados["valor"])
        resultado = 100 / numero
        return resultado
    except KeyError as e:
        print(f"Erro: Campo '{e}' não encontrado nos dados!")
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except ZeroDivisionError:
        print("Erro: O valor não pode ser zero!")
    except Exception as e:
        # Captura qualquer outro erro
        print(f"Erro inesperado: {type(e).__name__}: {e}")
    return None

print(processar_dados({"valor": "50"}))    # Funciona
print(processar_dados({"valor": "abc"}))   # ValueError
print(processar_dados({"valor": "0"}))     # ZeroDivisionError
print(processar_dados({"numero": "10"}))   # KeyError


# ============================================================
# EXERCÍCIO 2.4 - CALCULADORA À PROVA DE ERROS
# ============================================================

print("\n" + "=" * 50)
print("      CALCULADORA À PROVA DE ERROS")
print("=" * 50)


def obter_numero(mensagem):
    """Pede um número até o usuário digitar corretamente"""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("⚠ Entrada inválida! Digite um número.\n")


def obter_operacao():
    """Pede a operação até o usuário digitar uma válida"""
    operacoes_validas = ["+", "-", "*", "/"]
    while True:
        op = input("Operação (+, -, *, /): ").strip()
        if op in operacoes_validas:
            return op
        print("⚠ Operação inválida! Use +, -, * ou /\n")


def calcular(num1, operacao, num2):
    """Realiza o cálculo com tratamento de erros"""
    try:
        if operacao == "+":
            return num1 + num2
        elif operacao == "-":
            return num1 - num2
        elif operacao == "*":
            return num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero!")
            return num1 / num2
    except ZeroDivisionError as e:
        print(f"⚠ Erro: {e}")
        return None


# Loop principal
continuar = True

while continuar:
    print("\n--- Nova Operação ---")

    numero1 = obter_numero("Primeiro número: ")
    operacao = obter_operacao()
    numero2 = obter_numero("Segundo número: ")

    resultado = calcular(numero1, operacao, numero2)

    if resultado is not None:
        print(f"\n✓ {numero1} {operacao} {numero2} = {resultado}")

    resposta = input("\nFazer outro cálculo? (s/n): ").lower()
    if resposta != "s":
        continuar = False

print("\nObrigado por usar a calculadora!")


# ============================================================
# DESAFIO EXTRA - VALIDADOR DE CADASTRO
# ============================================================

print("\n" + "=" * 50)
print("        VALIDADOR DE CADASTRO")
print("=" * 50)


def validar_nome(nome):
    """Valida o nome do usuário"""
    if len(nome.strip()) < 3:
        raise ValueError("Nome deve ter pelo menos 3 caracteres")
    if any(char.isdigit() for char in nome):
        raise ValueError("Nome não pode conter números")
    return nome.strip().title()


def validar_email(email):
    """Validação simples de email"""
    if "@" not in email:
        raise ValueError("Email deve conter @")
    if "." not in email.split("@")[1]:
        raise ValueError("Email inválido (falta domínio)")
    return email.lower().strip()


def validar_idade(idade_str):
    """Valida a idade"""
    try:
        idade = int(idade_str)
    except ValueError:
        raise ValueError("Idade deve ser um número")

    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    if idade > 120:
        raise ValueError("Idade muito alta")
    return idade


def validar_senha(senha):
    """Valida a senha"""
    if len(senha) < 6:
        raise ValueError("Senha deve ter pelo menos 6 caracteres")
    if senha.isalpha():
        raise ValueError("Senha deve conter pelo menos um número")
    if senha.isdigit():
        raise ValueError("Senha deve conter pelo menos uma letra")
    return senha


def fazer_cadastro():
    """Realiza o cadastro com validação completa"""
    print("\n--- CADASTRO ---\n")
    cadastro = {}

    # Nome
    while True:
        try:
            nome = input("Nome: ")
            cadastro["nome"] = validar_nome(nome)
            break
        except ValueError as e:
            print(f"⚠ {e}\n")

    # Email
    while True:
        try:
            email = input("Email: ")
            cadastro["email"] = validar_email(email)
            break
        except ValueError as e:
            print(f"⚠ {e}\n")

    # Idade
    while True:
        try:
            idade = input("Idade: ")
            cadastro["idade"] = validar_idade(idade)
            break
        except ValueError as e:
            print(f"⚠ {e}\n")

    # Senha
    while True:
        try:
            senha = input("Senha: ")
            cadastro["senha"] = validar_senha(senha)
            break
        except ValueError as e:
            print(f"⚠ {e}\n")

    print("\n✓ CADASTRO REALIZADO COM SUCESSO!")
    print(f"  Nome: {cadastro['nome']}")
    print(f"  Email: {cadastro['email']}")
    print(f"  Idade: {cadastro['idade']}")
    print(f"  Senha: {'*' * len(cadastro['senha'])}")

    return cadastro


# Executar cadastro
fazer_cadastro()


# ============================================================
# TIPOS DE ERROS MAIS COMUNS
# ============================================================
#
# ValueError     - Valor inválido (ex: int("abc"))
# TypeError      - Tipo errado (ex: "texto" + 5)
# ZeroDivisionError - Divisão por zero
# IndexError     - Índice fora do alcance da lista
# KeyError       - Chave não existe no dicionário
# FileNotFoundError - Arquivo não encontrado
# NameError      - Variável não definida
# AttributeError - Método não existe no objeto
#
# ============================================================


# ============================================================
# LIMPEZA
# ============================================================
import os
if os.path.exists("teste.txt"):
    os.remove("teste.txt")


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ try/except evita que o programa quebre
# ✓ Capture erros específicos (ValueError, TypeError, etc.)
# ✓ else roda quando não há erro
# ✓ finally sempre roda (para limpeza)
# ✓ raise cria seus próprios erros
# ✓ 'as e' captura a mensagem do erro
# ✓ Entrada segura = while + try/except
# ============================================================
