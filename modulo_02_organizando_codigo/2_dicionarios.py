# ============================================================
# LIÇÃO 2.2 - DICIONÁRIOS: DADOS COM ETIQUETAS
# ============================================================
# Objetivo: Organizar dados com nomes (chaves) em vez de posições
# Analogia: Um dicionário é como um cartão de contato:
#           cada informação tem uma etiqueta (nome, telefone, email)
# ============================================================

# -----------------------------
# PARTE 1: O problema com listas
# -----------------------------
# Listas usam posições (índices). Isso pode ser confuso:

pessoa_lista = ["Maria", 25, "São Paulo", "maria@email.com"]

# Para acessar, precisamos lembrar a posição:
print("=== USANDO LISTA (confuso) ===")
print(f"Nome: {pessoa_lista[0]}")      # Posição 0 = nome
print(f"Idade: {pessoa_lista[1]}")     # Posição 1 = idade
print(f"Cidade: {pessoa_lista[2]}")    # Posição 2 = cidade

# E se a ordem mudar? Tudo quebra!


# -----------------------------
# PARTE 2: Criando dicionários
# -----------------------------
# Dicionários usam chaves (nomes) em vez de posições
# Formato: {chave: valor, chave: valor, ...}

print("\n=== USANDO DICIONÁRIO (claro) ===")

pessoa = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "São Paulo",
    "email": "maria@email.com"
}

# Acessando com a chave - muito mais claro!
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Cidade: {pessoa['cidade']}")
print(f"Email: {pessoa['email']}")


# -----------------------------
# PARTE 3: Operações básicas
# -----------------------------

print("\n=== OPERAÇÕES COM DICIONÁRIOS ===")

# Criando um dicionário vazio e adicionando dados:
carro = {}
carro["marca"] = "Fiat"
carro["modelo"] = "Uno"
carro["ano"] = 2020
carro["cor"] = "prata"

print(f"Carro: {carro}")

# Modificando um valor:
carro["cor"] = "preto"
print(f"Nova cor: {carro['cor']}")

# Removendo uma chave:
del carro["ano"]
print(f"Sem ano: {carro}")

# Verificando se chave existe:
if "marca" in carro:
    print("O carro tem marca definida!")

if "preco" not in carro:
    print("O carro não tem preço definido.")


# -----------------------------
# PARTE 4: Métodos úteis
# -----------------------------

print("\n=== MÉTODOS DE DICIONÁRIOS ===")

aluno = {
    "nome": "Carlos",
    "idade": 17,
    "curso": "Informática",
    "nota": 8.5
}

# .keys() - todas as chaves
print(f"Chaves: {list(aluno.keys())}")

# .values() - todos os valores
print(f"Valores: {list(aluno.values())}")

# .items() - pares chave-valor
print(f"Itens: {list(aluno.items())}")

# .get() - acessa com valor padrão se não existir
telefone = aluno.get("telefone", "Não informado")
print(f"Telefone: {telefone}")

# Tamanho (quantidade de chaves):
print(f"Quantidade de dados: {len(aluno)}")


# -----------------------------
# PARTE 5: Percorrendo dicionários
# -----------------------------

print("\n=== PERCORRENDO DICIONÁRIOS ===")

produto = {
    "nome": "Notebook",
    "preco": 2500.00,
    "marca": "Dell",
    "estoque": 15
}

# Percorrendo chaves:
print("Chaves do produto:")
for chave in produto:
    print(f"  - {chave}")

# Percorrendo valores:
print("\nValores do produto:")
for valor in produto.values():
    print(f"  - {valor}")

# Percorrendo chave E valor juntos:
print("\nDetalhes do produto:")
for chave, valor in produto.items():
    print(f"  {chave}: {valor}")


# -----------------------------
# PARTE 6: Lista de dicionários
# -----------------------------
# Podemos ter uma lista onde cada item é um dicionário
# Isso é muito comum em programação!

print("\n=== LISTA DE DICIONÁRIOS ===")

alunos = [
    {"nome": "Ana", "idade": 16, "nota": 9.0},
    {"nome": "Bruno", "idade": 17, "nota": 7.5},
    {"nome": "Carla", "idade": 16, "nota": 8.5},
    {"nome": "Daniel", "idade": 18, "nota": 6.0}
]

print("Lista de alunos:")
for aluno in alunos:
    print(f"  {aluno['nome']} - Nota: {aluno['nota']}")

# Calculando média da turma:
soma_notas = 0
for aluno in alunos:
    soma_notas += aluno["nota"]

media_turma = soma_notas / len(alunos)
print(f"\nMédia da turma: {media_turma:.1f}")

# Encontrando o melhor aluno:
melhor = alunos[0]
for aluno in alunos:
    if aluno["nota"] > melhor["nota"]:
        melhor = aluno

print(f"Melhor aluno: {melhor['nome']} com nota {melhor['nota']}")


# -----------------------------
# PARTE 7: Dicionários aninhados
# -----------------------------
# Dicionários podem conter outros dicionários!

print("\n=== DICIONÁRIOS ANINHADOS ===")

escola = {
    "nome": "Escola Estadual Centro",
    "endereco": {
        "rua": "Av. Brasil",
        "numero": 1000,
        "cidade": "São Paulo"
    },
    "contato": {
        "telefone": "(11) 1234-5678",
        "email": "contato@escola.edu.br"
    },
    "turmas": ["1A", "1B", "2A", "2B"]
}

# Acessando dados aninhados:
print(f"Escola: {escola['nome']}")
print(f"Cidade: {escola['endereco']['cidade']}")
print(f"Telefone: {escola['contato']['telefone']}")
print(f"Turmas: {escola['turmas']}")


# ============================================================
# EXERCÍCIO 2.2 - GERADOR DE CARTÃO DE PERFIL
# ============================================================

print("\n" + "=" * 50)
print("        GERADOR DE CARTÃO DE PERFIL")
print("=" * 50)


def criar_perfil():
    """Coleta dados e retorna um dicionário com o perfil"""
    print("\nPreencha seus dados:\n")

    perfil = {
        "nome": input("Nome completo: "),
        "idade": int(input("Idade: ")),
        "cidade": input("Cidade: "),
        "profissao": input("Profissão ou curso: "),
        "hobby": input("Hobby favorito: "),
        "rede_social": input("Rede social favorita: ")
    }

    return perfil


def exibir_cartao(perfil):
    """Exibe o cartão de perfil formatado"""
    largura = 40

    print("\n" + "+" + "-" * largura + "+")
    print("|" + " CARTÃO DE PERFIL ".center(largura) + "|")
    print("+" + "-" * largura + "+")

    print(f"| Nome: {perfil['nome']:<{largura - 8}}|")
    print(f"| Idade: {perfil['idade']:<{largura - 9}}|")
    print(f"| Cidade: {perfil['cidade']:<{largura - 10}}|")
    print(f"| Profissão: {perfil['profissao']:<{largura - 13}}|")
    print(f"| Hobby: {perfil['hobby']:<{largura - 9}}|")
    print(f"| Rede social: {perfil['rede_social']:<{largura - 15}}|")

    print("+" + "-" * largura + "+")


# Criar e exibir perfil:
meu_perfil = criar_perfil()
exibir_cartao(meu_perfil)


# ============================================================
# DESAFIO EXTRA - AGENDA DE CONTATOS SIMPLES
# ============================================================

print("\n" + "=" * 50)
print("          AGENDA DE CONTATOS")
print("=" * 50)

# Lista para guardar os contatos
contatos = []


def adicionar_contato():
    """Adiciona um novo contato à agenda"""
    contato = {
        "nome": input("Nome: "),
        "telefone": input("Telefone: "),
        "email": input("Email: ")
    }
    contatos.append(contato)
    print(f"\n✓ Contato '{contato['nome']}' adicionado!")


def listar_contatos():
    """Lista todos os contatos"""
    if len(contatos) == 0:
        print("\nAgenda vazia!")
        return

    print(f"\n{'=' * 45}")
    print(f"{'NOME':<15} {'TELEFONE':<15} {'EMAIL':<15}")
    print(f"{'=' * 45}")

    for contato in contatos:
        print(f"{contato['nome']:<15} {contato['telefone']:<15} {contato['email']:<15}")

    print(f"{'=' * 45}")
    print(f"Total: {len(contatos)} contato(s)")


def buscar_contato():
    """Busca um contato pelo nome"""
    nome_busca = input("Nome para buscar: ").lower()

    encontrados = []
    for contato in contatos:
        if nome_busca in contato["nome"].lower():
            encontrados.append(contato)

    if len(encontrados) == 0:
        print("\nNenhum contato encontrado.")
    else:
        print(f"\nEncontrado(s) {len(encontrados)} contato(s):")
        for c in encontrados:
            print(f"  - {c['nome']}: {c['telefone']}")


# Menu da agenda
while True:
    print("\n--- MENU AGENDA ---")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato")
    print("4. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        print("\nAté logo!")
        break
    else:
        print("\nOpção inválida!")


# ============================================================
# ERROS COMUNS
# ============================================================

# ERRO 1: Usar chave que não existe
# pessoa = {"nome": "Ana"}
# print(pessoa["idade"])  # ERRO! 'idade' não existe
# Use .get(): print(pessoa.get("idade", "Não informado"))

# ERRO 2: Confundir chave com índice
# pessoa = {"nome": "Ana"}
# print(pessoa[0])  # ERRO! Dicionário usa chave, não índice

# ERRO 3: Esquecer as aspas na chave (se for string)
# pessoa = {nome: "Ana"}  # ERRO! Deveria ser "nome"

# ERRO 4: Modificar dicionário enquanto percorre
# for chave in dicionario:
#     del dicionario[chave]  # Pode causar erro!


# ============================================================
# O QUE VOCÊ APRENDEU:
# ============================================================
# ✓ Dicionários guardam dados com chaves (nomes)
# ✓ Formato: {"chave": valor, "chave2": valor2}
# ✓ Acessar: dicionario["chave"]
# ✓ .keys(), .values(), .items() para percorrer
# ✓ .get() para acesso seguro com valor padrão
# ✓ Lista de dicionários para coleções de registros
# ✓ Dicionários podem conter outros dicionários
# ============================================================
