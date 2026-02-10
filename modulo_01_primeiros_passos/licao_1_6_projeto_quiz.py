# ============================================================
# LIÇÃO 1.6 - MINI-PROJETO: QUIZ INTERATIVO
# ============================================================
# Objetivo: Criar um jogo de perguntas e respostas completo
# Este projeto usa TUDO que você aprendeu:
#   - print() e input() (Lição 1.1 e 1.2)
#   - Variáveis e f-strings (Lição 1.2)
#   - if/elif/else (Lição 1.3)
#   - Loops for e while (Lição 1.4)
#   - Listas (Lição 1.5)
# ============================================================


# ============================================================
# VERSÃO 1: QUIZ SIMPLES
# ============================================================
# Começamos com algo básico e vamos melhorando!

def quiz_simples():
    """
    Quiz mais simples possível - bom para entender a estrutura
    """
    print("\n" + "=" * 50)
    print("       QUIZ SIMPLES - VERSÃO BÁSICA")
    print("=" * 50)

    # Variável para guardar os pontos
    pontos = 0

    # PERGUNTA 1
    print("\nPergunta 1: Qual é a capital do Brasil?")
    resposta = input("Sua resposta: ")

    if resposta.lower() == "brasília" or resposta.lower() == "brasilia":
        print("✓ Correto!")
        pontos = pontos + 1
    else:
        print("✗ Errado! A resposta era Brasília.")

    # PERGUNTA 2
    print("\nPergunta 2: Quanto é 7 x 8?")
    resposta = input("Sua resposta: ")

    if resposta == "56":
        print("✓ Correto!")
        pontos = pontos + 1
    else:
        print("✗ Errado! A resposta era 56.")

    # PERGUNTA 3
    print("\nPergunta 3: Qual é a cor do céu em um dia limpo?")
    resposta = input("Sua resposta: ")

    if resposta.lower() == "azul":
        print("✓ Correto!")
        pontos = pontos + 1
    else:
        print("✗ Errado! A resposta era azul.")

    # RESULTADO FINAL
    print("\n" + "=" * 50)
    print(f"RESULTADO: Você acertou {pontos} de 3 perguntas!")
    print("=" * 50)


# ============================================================
# VERSÃO 2: QUIZ COM LISTAS
# ============================================================
# Usando listas, o código fica mais organizado e fácil de expandir

def quiz_com_listas():
    """
    Quiz usando listas - muito mais fácil de adicionar perguntas!
    """
    print("\n" + "=" * 50)
    print("        QUIZ BRASIL - VERSÃO MELHORADA")
    print("=" * 50)

    # Listas de perguntas e respostas
    perguntas = [
        "Qual é a capital do Brasil?",
        "Qual é o maior estado do Brasil em área?",
        "Em que ano o Brasil foi descoberto?",
        "Qual é o rio mais longo do Brasil?",
        "Quantos estados tem o Brasil?"
    ]

    respostas_corretas = [
        "brasília",
        "amazonas",
        "1500",
        "amazonas",
        "26"
    ]

    # Variáveis de controle
    pontos = 0
    total_perguntas = len(perguntas)

    # Loop pelas perguntas
    for i in range(total_perguntas):
        print(f"\nPergunta {i + 1} de {total_perguntas}:")
        print(perguntas[i])

        resposta_usuario = input("Sua resposta: ").lower().strip()

        if resposta_usuario == respostas_corretas[i]:
            print("✓ Correto! 🎉")
            pontos = pontos + 1
        else:
            print(f"✗ Errado! A resposta correta era: {respostas_corretas[i].title()}")

    # Resultado
    porcentagem = (pontos / total_perguntas) * 100

    print("\n" + "=" * 50)
    print("                RESULTADO FINAL")
    print("=" * 50)
    print(f"Acertos: {pontos} de {total_perguntas}")
    print(f"Porcentagem: {porcentagem:.0f}%")

    # Feedback baseado no desempenho
    if porcentagem == 100:
        print("🏆 PERFEITO! Você é um gênio!")
    elif porcentagem >= 80:
        print("🥇 Excelente! Muito bem!")
    elif porcentagem >= 60:
        print("🥈 Bom trabalho! Continue praticando!")
    elif porcentagem >= 40:
        print("🥉 Razoável. Estude mais um pouco!")
    else:
        print("📚 Precisa estudar mais. Não desista!")

    print("=" * 50)


# ============================================================
# VERSÃO 3: QUIZ COM MÚLTIPLA ESCOLHA
# ============================================================
# Mais fácil para o usuário e mais divertido!

def quiz_multipla_escolha():
    """
    Quiz com opções A, B, C, D - mais interativo!
    """
    print("\n" + "=" * 50)
    print("      QUIZ CULTURA POP - MÚLTIPLA ESCOLHA")
    print("=" * 50)

    # Estrutura: [pergunta, [opções], resposta correta]
    quiz = [
        [
            "Qual rede social é conhecida pelo passarinho azul?",
            ["A) Instagram", "B) Facebook", "C) Twitter/X", "D) TikTok"],
            "c"
        ],
        [
            "Quem criou o personagem Mickey Mouse?",
            ["A) Pixar", "B) Walt Disney", "C) Stan Lee", "D) Steven Spielberg"],
            "b"
        ],
        [
            "Qual é o jogo mais vendido de todos os tempos?",
            ["A) GTA V", "B) Fortnite", "C) Minecraft", "D) FIFA"],
            "c"
        ],
        [
            "Qual é a rede social de vídeos curtos mais popular entre jovens?",
            ["A) YouTube", "B) Snapchat", "C) LinkedIn", "D) TikTok"],
            "d"
        ],
        [
            "Em qual país foi criado o anime?",
            ["A) China", "B) Coreia do Sul", "C) Japão", "D) Estados Unidos"],
            "c"
        ]
    ]

    pontos = 0

    print("\nResponda com a letra da opção (A, B, C ou D)\n")

    for i, pergunta_dados in enumerate(quiz):
        pergunta = pergunta_dados[0]
        opcoes = pergunta_dados[1]
        resposta_correta = pergunta_dados[2]

        print(f"Pergunta {i + 1}: {pergunta}")
        for opcao in opcoes:
            print(f"   {opcao}")

        resposta = input("Sua resposta: ").lower().strip()

        if resposta == resposta_correta:
            print("✓ Correto! 🎉\n")
            pontos = pontos + 1
        else:
            print(f"✗ Errado! A resposta era: {resposta_correta.upper()}\n")

    # Resultado
    print("=" * 50)
    print(f"RESULTADO: {pontos} de {len(quiz)} pontos")

    if pontos == len(quiz):
        print("🏆 PERFEITO! Você manja de cultura pop!")
    elif pontos >= len(quiz) * 0.6:
        print("👍 Muito bom! Você está por dentro!")
    else:
        print("📱 Tá na hora de atualizar seus conhecimentos!")
    print("=" * 50)


# ============================================================
# VERSÃO 4: QUIZ COMPLETO COM MENU
# ============================================================
# Versão final com todas as funcionalidades

import random  # Para embaralhar perguntas

def quiz_completo():
    """
    Quiz completo com menu, categorias e ranking
    """

    # Banco de perguntas por categoria
    perguntas_geografia = [
        ["Qual é o maior país do mundo em área?", "russia", "rússia"],
        ["Qual continente tem mais países?", "africa", "áfrica"],
        ["Qual é a montanha mais alta do mundo?", "everest", "monte everest"],
        ["Em qual continente fica o Egito?", "africa", "áfrica"],
        ["Qual país tem formato de bota?", "italia", "itália"]
    ]

    perguntas_matematica = [
        ["Quanto é 15 x 15?", "225"],
        ["Qual é a raiz quadrada de 144?", "12"],
        ["Quanto é 100 dividido por 4?", "25"],
        ["Qual é o resultado de 2 elevado a 5?", "32"],
        ["Quanto é 17 + 28?", "45"]
    ]

    perguntas_ciencias = [
        ["Qual é o planeta mais próximo do Sol?", "mercurio", "mercúrio"],
        ["Qual é o elemento químico do ouro?", "au"],
        ["Quantos ossos tem o corpo humano adulto?", "206"],
        ["Qual é a fórmula da água?", "h2o"],
        ["Qual é o maior órgão do corpo humano?", "pele"]
    ]

    def jogar_categoria(nome_categoria, perguntas):
        """Função que roda o quiz de uma categoria"""
        print(f"\n{'=' * 50}")
        print(f"        QUIZ DE {nome_categoria.upper()}")
        print(f"{'=' * 50}")

        # Embaralha as perguntas
        perguntas_embaralhadas = perguntas.copy()
        random.shuffle(perguntas_embaralhadas)

        # Seleciona 5 perguntas (ou menos se não tiver)
        perguntas_selecionadas = perguntas_embaralhadas[:5]

        pontos = 0

        for i, pergunta in enumerate(perguntas_selecionadas, 1):
            texto_pergunta = pergunta[0]
            respostas_aceitas = [r.lower() for r in pergunta[1:]]

            print(f"\nPergunta {i}: {texto_pergunta}")
            resposta = input("Sua resposta: ").lower().strip()

            if resposta in respostas_aceitas:
                print("✓ CORRETO! +1 ponto")
                pontos += 1
            else:
                print(f"✗ Errado! Resposta: {pergunta[1].title()}")

        # Resultado da categoria
        print(f"\n{'-' * 50}")
        print(f"Pontuação em {nome_categoria}: {pontos}/{len(perguntas_selecionadas)}")
        return pontos

    # MENU PRINCIPAL
    print("\n" + "=" * 50)
    print("          🎮 SUPER QUIZ 🎮")
    print("=" * 50)

    nome_jogador = input("\nDigite seu nome: ")
    print(f"\nOlá, {nome_jogador}! Bem-vindo ao Super Quiz!")

    pontuacao_total = 0
    categorias_jogadas = 0

    while True:
        print("\n" + "-" * 40)
        print("MENU PRINCIPAL")
        print("-" * 40)
        print("1. Quiz de Geografia")
        print("2. Quiz de Matemática")
        print("3. Quiz de Ciências")
        print("4. Jogar Todas as Categorias")
        print("5. Ver Pontuação")
        print("6. Sair")
        print("-" * 40)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pontos = jogar_categoria("Geografia", perguntas_geografia)
            pontuacao_total += pontos
            categorias_jogadas += 1

        elif opcao == "2":
            pontos = jogar_categoria("Matemática", perguntas_matematica)
            pontuacao_total += pontos
            categorias_jogadas += 1

        elif opcao == "3":
            pontos = jogar_categoria("Ciências", perguntas_ciencias)
            pontuacao_total += pontos
            categorias_jogadas += 1

        elif opcao == "4":
            print("\n🎯 MODO DESAFIO: Todas as categorias!")
            pontos_geo = jogar_categoria("Geografia", perguntas_geografia)
            pontos_mat = jogar_categoria("Matemática", perguntas_matematica)
            pontos_cie = jogar_categoria("Ciências", perguntas_ciencias)

            total_desafio = pontos_geo + pontos_mat + pontos_cie
            pontuacao_total += total_desafio
            categorias_jogadas += 3

            print("\n" + "=" * 50)
            print("        RESULTADO DO DESAFIO")
            print("=" * 50)
            print(f"Geografia: {pontos_geo}/5")
            print(f"Matemática: {pontos_mat}/5")
            print(f"Ciências: {pontos_cie}/5")
            print(f"TOTAL: {total_desafio}/15")

            if total_desafio >= 12:
                print("🏆 INCRÍVEL! Você é um gênio!")
            elif total_desafio >= 8:
                print("🥈 Muito bom! Parabéns!")
            else:
                print("📚 Continue estudando!")
            print("=" * 50)

        elif opcao == "5":
            print("\n" + "-" * 40)
            print(f"PONTUAÇÃO DE {nome_jogador.upper()}")
            print("-" * 40)
            print(f"Pontos totais: {pontuacao_total}")
            print(f"Categorias jogadas: {categorias_jogadas}")
            if categorias_jogadas > 0:
                media = pontuacao_total / categorias_jogadas
                print(f"Média por categoria: {media:.1f}")
            print("-" * 40)

        elif opcao == "6":
            print(f"\nObrigado por jogar, {nome_jogador}!")
            print(f"Sua pontuação final: {pontuacao_total} pontos")
            print("Até a próxima! 👋")
            break

        else:
            print("❌ Opção inválida! Digite 1, 2, 3, 4, 5 ou 6.")


# ============================================================
# MENU PARA ESCOLHER QUAL VERSÃO RODAR
# ============================================================

print("=" * 50)
print("     LIÇÃO 1.6 - MINI-PROJETO: QUIZ")
print("=" * 50)
print("\nEste arquivo tem 4 versões do quiz:")
print("1. Quiz Simples (para entender a estrutura)")
print("2. Quiz com Listas (código mais organizado)")
print("3. Quiz Múltipla Escolha (mais interativo)")
print("4. Quiz Completo (com menu e categorias)")
print("=" * 50)

escolha = input("\nEscolha uma versão para rodar (1-4): ")

if escolha == "1":
    quiz_simples()
elif escolha == "2":
    quiz_com_listas()
elif escolha == "3":
    quiz_multipla_escolha()
elif escolha == "4":
    quiz_completo()
else:
    print("Opção inválida! Rodando o Quiz Completo...")
    quiz_completo()


# ============================================================
# DESAFIO PARA O ALUNO
# ============================================================
# Agora é sua vez! Crie seu próprio quiz sobre um tema que
# você gosta: música, esportes, filmes, jogos, etc.
#
# Requisitos mínimos:
# - 5 perguntas ou mais
# - Sistema de pontuação
# - Mensagem de resultado no final
#
# Desafios extras:
# - Adicionar múltipla escolha
# - Embaralhar a ordem das perguntas
# - Adicionar níveis de dificuldade
# - Mostrar quanto tempo levou para responder
# - Salvar o recorde em um arquivo
# ============================================================


# ============================================================
# O QUE VOCÊ APRENDEU NESTE MÓDULO:
# ============================================================
# ✓ print() - mostrar mensagens na tela
# ✓ Variáveis - guardar dados em "caixas"
# ✓ f-strings - misturar texto com variáveis
# ✓ input() - receber dados do usuário
# ✓ int() e float() - converter texto para número
# ✓ if/elif/else - tomar decisões
# ✓ for e while - repetir ações
# ✓ Listas - guardar coleções de dados
# ✓ Funções - organizar código em blocos reutilizáveis
#
# PARABÉNS! Você completou o Módulo 1! 🎉
# Você já sabe programar!
# ============================================================
