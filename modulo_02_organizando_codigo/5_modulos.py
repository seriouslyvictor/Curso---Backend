# ============================================================
# LIÇÃO 2.5 - MÓDULOS E IMPORTS
# ============================================================
# Objetivo: Organizar código em múltiplos arquivos e usar
#           bibliotecas prontas
# Analogia: Assim como você não fabrica sua própria panela
#           para cozinhar, você não precisa criar tudo do zero.
#           Use ferramentas prontas!
# ============================================================

# -----------------------------
# PARTE 1: Por que módulos?
# -----------------------------
# Imagine um programa com 10.000 linhas em um único arquivo.
# Impossível de entender e manter!
#
# Módulos permitem:
# - Dividir código em arquivos menores
# - Reutilizar código em vários projetos
# - Usar código que outros programadores criaram


# -----------------------------
# PARTE 2: Importando módulos da biblioteca padrão
# -----------------------------
# Python já vem com MUITOS módulos prontos!

print("=== MÓDULOS DA BIBLIOTECA PADRÃO ===")

# MÓDULO RANDOM - números aleatórios
import random

numero_aleatorio = random.randint(1, 100)
print(f"Número aleatório (1-100): {numero_aleatorio}")

lista = ["maçã", "banana", "laranja", "uva"]
fruta_escolhida = random.choice(lista)
print(f"Fruta sorteada: {fruta_escolhida}")

random.shuffle(lista)  # Embaralha a lista
print(f"Lista embaralhada: {lista}")


# MÓDULO DATETIME - datas e horas
from datetime import datetime, date, timedelta

agora = datetime.now()
print(f"\nData e hora atual: {agora.strftime('%d/%m/%Y %H:%M')}")

hoje = date.today()
print(f"Hoje é: {hoje.strftime('%A, %d de %B de %Y')}")

amanha = hoje + timedelta(days=1)
print(f"Amanhã será: {amanha.strftime('%d/%m/%Y')}")

daqui_30_dias = hoje + timedelta(days=30)
print(f"Daqui 30 dias: {daqui_30_dias.strftime('%d/%m/%Y')}")


# MÓDULO MATH - funções matemáticas
import math

print(f"\nPi: {math.pi}")
print(f"Raiz quadrada de 16: {math.sqrt(16)}")
print(f"2 elevado a 10: {math.pow(2, 10)}")
print(f"Arredondando 3.7 para cima: {math.ceil(3.7)}")
print(f"Arredondando 3.7 para baixo: {math.floor(3.7)}")


# MÓDULO OS - sistema operacional
import os

print(f"\nPasta atual: {os.getcwd()}")
print(f"Seu usuário: {os.getenv('USERNAME', 'desconhecido')}")


# MÓDULO STRING - constantes úteis
import string

print(f"\nLetras: {string.ascii_letters[:10]}...")
print(f"Dígitos: {string.digits}")
print(f"Pontuação: {string.punctuation}")


# -----------------------------
# PARTE 3: Formas de importar
# -----------------------------

print("\n=== FORMAS DE IMPORTAR ===")

# Forma 1: import modulo (precisa usar modulo.funcao)
import random
num = random.randint(1, 10)
print(f"random.randint: {num}")

# Forma 2: from modulo import funcao (usa direto)
from random import randint, choice
num = randint(1, 10)  # Não precisa do "random."
print(f"randint direto: {num}")

# Forma 3: import modulo as apelido (atalho)
import datetime as dt
agora = dt.datetime.now()
print(f"Com apelido: {agora}")

# Forma 4: from modulo import * (importa tudo - EVITE!)
# from random import *  # Pode causar conflitos de nomes


# -----------------------------
# PARTE 4: Criando seus próprios módulos
# -----------------------------
# Qualquer arquivo .py é um módulo!

print("\n=== CRIANDO MÓDULOS ===")

# Vamos criar um módulo de utilidades
codigo_utilidades = '''# utilidades.py - Módulo de funções úteis

def saudar(nome):
    """Retorna uma saudação personalizada"""
    return f"Olá, {nome}! Bem-vindo!"

def calcular_media(notas):
    """Calcula a média de uma lista de notas"""
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def formatar_moeda(valor):
    """Formata um valor como moeda brasileira"""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def validar_cpf(cpf):
    """Valida formato básico de CPF (apenas formato, não validade real)"""
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    return len(cpf_limpo) == 11 and cpf_limpo.isdigit()

# Constantes
VERSAO = "1.0.0"
AUTOR = "Seu Nome"
'''

# Salvando o módulo
with open("utilidades.py", "w", encoding="utf-8") as f:
    f.write(codigo_utilidades)

print("Módulo 'utilidades.py' criado!")

# Agora podemos importar e usar:
import utilidades

print(utilidades.saudar("Maria"))
print(f"Média: {utilidades.calcular_media([8.5, 7.0, 9.0])}")
print(utilidades.formatar_moeda(1234.56))
print(f"CPF válido? {utilidades.validar_cpf('123.456.789-00')}")
print(f"Versão do módulo: {utilidades.VERSAO}")


# -----------------------------
# PARTE 5: Organizando em pastas (pacotes)
# -----------------------------
# Quando o projeto cresce, organize em pastas!

print("\n=== ESTRUTURA DE PROJETO ===")
print("""
Uma estrutura comum de projeto:

meu_projeto/
├── main.py              # Arquivo principal
├── config.py            # Configurações
├── utils/               # Pasta de utilidades
│   ├── __init__.py      # Indica que é um pacote
│   ├── texto.py         # Funções de texto
│   └── numeros.py       # Funções numéricas
├── dados/               # Pasta de dados
│   ├── __init__.py
│   └── banco.py         # Funções de banco de dados
└── requirements.txt     # Dependências externas
""")


# -----------------------------
# PARTE 6: Instalando pacotes externos (pip)
# -----------------------------

print("=== PACOTES EXTERNOS COM PIP ===")
print("""
O pip instala pacotes criados por outros programadores.

Comandos básicos:
  pip install nome_pacote     # Instala um pacote
  pip uninstall nome_pacote   # Remove um pacote
  pip list                    # Lista pacotes instalados
  pip freeze > requirements.txt  # Salva dependências

Pacotes populares:
  requests  - Fazer requisições HTTP (acessar APIs)
  flask     - Criar sites e APIs web
  pandas    - Análise de dados
  pillow    - Manipular imagens
  pygame    - Criar jogos
""")


# ============================================================
# EXERCÍCIO 2.5 - SISTEMA DE SENHA SEGURA
# ============================================================

print("\n" + "=" * 50)
print("      GERADOR DE SENHAS SEGURAS")
print("=" * 50)

import random
import string


def gerar_senha(tamanho=12, usar_especiais=True, usar_numeros=True, usar_maiusculas=True):
    """
    Gera uma senha aleatória segura.

    Args:
        tamanho: Quantidade de caracteres (padrão 12)
        usar_especiais: Incluir !@#$% etc (padrão True)
        usar_numeros: Incluir números (padrão True)
        usar_maiusculas: Incluir maiúsculas (padrão True)

    Returns:
        String com a senha gerada
    """
    # Começa com letras minúsculas
    caracteres = string.ascii_lowercase

    # Adiciona conforme opções
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += "!@#$%&*"

    # Gera a senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def avaliar_forca(senha):
    """Avalia a força de uma senha"""
    pontos = 0

    if len(senha) >= 8:
        pontos += 1
    if len(senha) >= 12:
        pontos += 1
    if any(c.isupper() for c in senha):
        pontos += 1
    if any(c.islower() for c in senha):
        pontos += 1
    if any(c.isdigit() for c in senha):
        pontos += 1
    if any(c in "!@#$%&*" for c in senha):
        pontos += 1

    if pontos <= 2:
        return "Fraca 😟"
    elif pontos <= 4:
        return "Média 😐"
    else:
        return "Forte 💪"


# Menu do gerador
while True:
    print("\n--- GERADOR DE SENHAS ---")
    print("1. Gerar senha rápida (12 caracteres)")
    print("2. Gerar senha personalizada")
    print("3. Avaliar uma senha")
    print("4. Sair")

    opcao = input("\nOpção: ")

    if opcao == "1":
        senha = gerar_senha()
        print(f"\n🔐 Senha gerada: {senha}")
        print(f"   Força: {avaliar_forca(senha)}")

    elif opcao == "2":
        try:
            tam = int(input("Tamanho da senha (8-50): "))
            tam = max(8, min(50, tam))  # Garante entre 8 e 50

            especiais = input("Incluir caracteres especiais? (s/n): ").lower() == "s"
            numeros = input("Incluir números? (s/n): ").lower() == "s"
            maiusculas = input("Incluir maiúsculas? (s/n): ").lower() == "s"

            senha = gerar_senha(tam, especiais, numeros, maiusculas)
            print(f"\n🔐 Senha gerada: {senha}")
            print(f"   Força: {avaliar_forca(senha)}")
        except ValueError:
            print("Tamanho inválido!")

    elif opcao == "3":
        senha = input("Digite a senha para avaliar: ")
        print(f"   Força: {avaliar_forca(senha)}")

    elif opcao == "4":
        print("\nAté logo!")
        break


# ============================================================
# DESAFIO EXTRA - JOGO DO DIA SORTUDO
# ============================================================

print("\n" + "=" * 50)
print("         JOGO DO DIA SORTUDO")
print("=" * 50)

from datetime import date
import random


def calcular_numeros_sorte(data_nascimento):
    """Calcula números da sorte baseado na data de nascimento"""
    # Usa a data como semente para gerar sempre os mesmos números
    partes = data_nascimento.split("/")
    dia, mes, ano = int(partes[0]), int(partes[1]), int(partes[2])

    # Combina com data de hoje para variar por dia
    hoje = date.today()
    semente = dia + mes + ano + hoje.day + hoje.month

    random.seed(semente)

    numeros = sorted(random.sample(range(1, 61), 6))
    return numeros


def calcular_frase_do_dia(data_nascimento):
    """Retorna uma frase motivacional do dia"""
    frases = [
        "Hoje é um ótimo dia para começar algo novo!",
        "Sua energia positiva vai atrair coisas boas.",
        "Confie em você, você é capaz!",
        "Pequenos passos levam a grandes conquistas.",
        "O universo conspira a seu favor hoje.",
        "Sua criatividade está em alta!",
        "É hora de colocar suas ideias em prática.",
        "Boas surpresas estão a caminho!",
        "Mantenha o foco e você alcançará seus objetivos.",
        "Hoje é dia de agradecer e celebrar!"
    ]

    partes = data_nascimento.split("/")
    hoje = date.today()
    indice = (int(partes[0]) + hoje.day) % len(frases)

    return frases[indice]


# Executar jogo
print("\nDescubra seus números da sorte de hoje!\n")

nascimento = input("Sua data de nascimento (dd/mm/aaaa): ")

try:
    numeros = calcular_numeros_sorte(nascimento)
    frase = calcular_frase_do_dia(nascimento)

    print(f"\n🍀 Seus números da sorte para hoje:")
    print(f"   {numeros}")
    print(f"\n✨ Frase do dia:")
    print(f"   {frase}")
except:
    print("Data inválida! Use o formato dd/mm/aaaa")


# ============================================================
# LIMPEZA
# ============================================================
import os
if os.path.exists("utilidades.py"):
    os.remove("utilidades.py")
    print("\n(Arquivo utilidades.py removido)")


# ============================================================
# RESUMO DE MÓDULOS ÚTEIS
# ============================================================
#
# random    - Números aleatórios, escolhas, embaralhamento
# datetime  - Datas, horas, durações
# math      - Funções matemáticas avançadas
# os        - Interação com sistema operacional
# json      - Ler/escrever arquivos JSON
# string    - Constantes de caracteres
# re        - Expressões regulares
# time      - Pausas, medição de tempo
# copy      - Cópias de objetos
# collections - Estruturas de dados especiais
#
# ============================================================


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ import modulo - importa o módulo inteiro
# ✓ from modulo import funcao - importa só o que precisa
# ✓ import modulo as apelido - cria um atalho
# ✓ Qualquer arquivo .py é um módulo
# ✓ pip install - instala pacotes externos
# ✓ random, datetime, math - módulos úteis da biblioteca
# ✓ Organize projetos grandes em múltiplos arquivos
# ============================================================
