# ============================================================
# LIÇÃO 2.6 - MINI-PROJETO: AGENDA DE CONTATOS
# ============================================================
# Objetivo: Criar uma agenda completa que integra tudo do Módulo 2
#
# Este projeto usa:
#   - Funções (Lição 2.1)
#   - Dicionários (Lição 2.2)
#   - Arquivos e JSON (Lição 2.3)
#   - Tratamento de erros (Lição 2.4)
#   - Módulos (Lição 2.5)
# ============================================================

import json
import os
from datetime import datetime

# ============================================================
# CONFIGURAÇÕES
# ============================================================

ARQUIVO_CONTATOS = "agenda_contatos.json"
VERSAO = "1.0"

# ============================================================
# FUNÇÕES DE DADOS (manipulação de contatos)
# ============================================================

def carregar_contatos():
    """
    Carrega os contatos do arquivo JSON.
    Retorna lista vazia se arquivo não existir.
    """
    try:
        if os.path.exists(ARQUIVO_CONTATOS):
            with open(ARQUIVO_CONTATOS, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        return []
    except json.JSONDecodeError:
        print("⚠ Erro ao ler arquivo. Iniciando agenda vazia.")
        return []
    except Exception as e:
        print(f"⚠ Erro inesperado: {e}")
        return []


def salvar_contatos(contatos):
    """
    Salva a lista de contatos no arquivo JSON.
    Retorna True se salvou com sucesso, False se houve erro.
    """
    try:
        with open(ARQUIVO_CONTATOS, "w", encoding="utf-8") as arquivo:
            json.dump(contatos, arquivo, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"⚠ Erro ao salvar: {e}")
        return False


def buscar_por_nome(contatos, termo):
    """
    Busca contatos que contenham o termo no nome.
    Retorna lista de contatos encontrados.
    """
    termo = termo.lower().strip()
    encontrados = []

    for contato in contatos:
        if termo in contato["nome"].lower():
            encontrados.append(contato)

    return encontrados


def buscar_por_id(contatos, id_contato):
    """
    Busca um contato pelo ID.
    Retorna o contato ou None se não encontrar.
    """
    for contato in contatos:
        if contato["id"] == id_contato:
            return contato
    return None


def gerar_id(contatos):
    """Gera um novo ID único para o contato."""
    if len(contatos) == 0:
        return 1

    maior_id = max(c["id"] for c in contatos)
    return maior_id + 1


# ============================================================
# FUNÇÕES DE VALIDAÇÃO
# ============================================================

def validar_email(email):
    """
    Valida formato básico de email.
    Retorna True se válido, False se inválido.
    """
    email = email.strip()
    if not email:  # Email vazio é permitido
        return True
    if "@" not in email:
        return False
    if "." not in email.split("@")[1]:
        return False
    return True


def validar_telefone(telefone):
    """
    Valida formato básico de telefone.
    Aceita apenas números, espaços, parênteses e hífen.
    """
    telefone = telefone.strip()
    if not telefone:  # Telefone vazio é permitido
        return True

    caracteres_validos = "0123456789 ()-+"
    for char in telefone:
        if char not in caracteres_validos:
            return False

    # Deve ter pelo menos 8 dígitos
    digitos = sum(1 for c in telefone if c.isdigit())
    return digitos >= 8


def validar_nome(nome):
    """
    Valida o nome do contato.
    Retorna True se válido, False se inválido.
    """
    nome = nome.strip()
    if len(nome) < 2:
        return False
    return True


# ============================================================
# FUNÇÕES DE INTERFACE (interação com usuário)
# ============================================================

def exibir_cabecalho():
    """Exibe o cabeçalho do programa."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa tela
    print("=" * 55)
    print("            📒 AGENDA DE CONTATOS")
    print(f"                 Versão {VERSAO}")
    print("=" * 55)


def exibir_menu():
    """Exibe o menu principal."""
    print("\n┌─────────────────────────────────┐")
    print("│         MENU PRINCIPAL          │")
    print("├─────────────────────────────────┤")
    print("│  1. ➕ Adicionar contato        │")
    print("│  2. 📋 Listar contatos          │")
    print("│  3. 🔍 Buscar contato           │")
    print("│  4. ✏️  Editar contato           │")
    print("│  5. 🗑️  Excluir contato          │")
    print("│  6. 📊 Estatísticas             │")
    print("│  7. 💾 Exportar para texto      │")
    print("│  0. 🚪 Sair                     │")
    print("└─────────────────────────────────┘")


def exibir_contato(contato, detalhado=False):
    """Exibe um contato formatado."""
    print(f"\n  📌 {contato['nome']}")
    print(f"     📞 {contato.get('telefone', 'Não informado')}")
    print(f"     📧 {contato.get('email', 'Não informado')}")

    if detalhado:
        print(f"     🏷️  Categoria: {contato.get('categoria', 'Geral')}")
        if contato.get('notas'):
            print(f"     📝 Notas: {contato['notas']}")
        print(f"     🆔 ID: {contato['id']}")
        print(f"     📅 Criado em: {contato.get('criado_em', 'Desconhecido')}")


def pedir_texto(mensagem, obrigatorio=True, validador=None):
    """
    Pede um texto ao usuário com validação opcional.

    Args:
        mensagem: Texto a exibir
        obrigatorio: Se True, não aceita vazio
        validador: Função de validação (retorna True/False)

    Returns:
        String digitada pelo usuário
    """
    while True:
        valor = input(mensagem).strip()

        if not valor and not obrigatorio:
            return valor

        if not valor and obrigatorio:
            print("⚠ Este campo é obrigatório!")
            continue

        if validador and not validador(valor):
            print("⚠ Valor inválido! Tente novamente.")
            continue

        return valor


def pedir_confirmacao(mensagem):
    """Pede confirmação sim/não ao usuário."""
    while True:
        resposta = input(f"{mensagem} (s/n): ").lower().strip()
        if resposta in ["s", "sim"]:
            return True
        if resposta in ["n", "nao", "não"]:
            return False
        print("⚠ Digite 's' para sim ou 'n' para não.")


# ============================================================
# FUNÇÕES DE AÇÕES (operações principais)
# ============================================================

def adicionar_contato(contatos):
    """Adiciona um novo contato à agenda."""
    print("\n--- ADICIONAR CONTATO ---\n")

    # Coleta dados
    nome = pedir_texto("Nome: ", obrigatorio=True, validador=validar_nome)
    telefone = pedir_texto("Telefone: ", obrigatorio=False, validador=validar_telefone)
    email = pedir_texto("Email: ", obrigatorio=False, validador=validar_email)

    print("\nCategorias: Família, Amigos, Trabalho, Outros")
    categoria = pedir_texto("Categoria (Enter para 'Geral'): ", obrigatorio=False)
    if not categoria:
        categoria = "Geral"

    notas = pedir_texto("Notas (opcional): ", obrigatorio=False)

    # Cria o contato
    novo_contato = {
        "id": gerar_id(contatos),
        "nome": nome.title(),
        "telefone": telefone if telefone else None,
        "email": email.lower() if email else None,
        "categoria": categoria.title(),
        "notas": notas if notas else None,
        "criado_em": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    # Confirmação
    print("\n--- Confirme os dados ---")
    exibir_contato(novo_contato, detalhado=True)

    if pedir_confirmacao("\nSalvar este contato?"):
        contatos.append(novo_contato)
        if salvar_contatos(contatos):
            print("\n✅ Contato adicionado com sucesso!")
        else:
            print("\n⚠ Contato adicionado, mas houve erro ao salvar.")
    else:
        print("\n❌ Operação cancelada.")


def listar_contatos(contatos):
    """Lista todos os contatos."""
    print("\n--- LISTA DE CONTATOS ---")

    if len(contatos) == 0:
        print("\n📭 A agenda está vazia.")
        return

    # Ordena por nome
    contatos_ordenados = sorted(contatos, key=lambda c: c["nome"])

    print(f"\n📒 Total: {len(contatos)} contato(s)\n")
    print("-" * 50)

    for contato in contatos_ordenados:
        categoria = contato.get("categoria", "Geral")
        print(f"  [{contato['id']:03d}] {contato['nome']:<25} ({categoria})")
        if contato.get("telefone"):
            print(f"        📞 {contato['telefone']}")

    print("-" * 50)


def buscar_contato(contatos):
    """Busca contatos por nome."""
    print("\n--- BUSCAR CONTATO ---\n")

    if len(contatos) == 0:
        print("📭 A agenda está vazia.")
        return

    termo = pedir_texto("Digite o nome (ou parte dele): ")
    encontrados = buscar_por_nome(contatos, termo)

    if len(encontrados) == 0:
        print(f"\n❌ Nenhum contato encontrado com '{termo}'.")
    else:
        print(f"\n✅ Encontrado(s) {len(encontrados)} contato(s):\n")
        for contato in encontrados:
            exibir_contato(contato, detalhado=True)


def editar_contato(contatos):
    """Edita um contato existente."""
    print("\n--- EDITAR CONTATO ---\n")

    if len(contatos) == 0:
        print("📭 A agenda está vazia.")
        return

    # Busca o contato
    termo = pedir_texto("Nome do contato para editar: ")
    encontrados = buscar_por_nome(contatos, termo)

    if len(encontrados) == 0:
        print(f"\n❌ Nenhum contato encontrado com '{termo}'.")
        return

    # Se encontrou vários, mostra lista
    if len(encontrados) > 1:
        print("\nVários contatos encontrados:")
        for c in encontrados:
            print(f"  [{c['id']}] {c['nome']}")
        try:
            id_escolhido = int(pedir_texto("\nDigite o ID do contato: "))
            contato = buscar_por_id(contatos, id_escolhido)
        except ValueError:
            print("❌ ID inválido.")
            return
    else:
        contato = encontrados[0]

    if not contato:
        print("❌ Contato não encontrado.")
        return

    # Mostra contato atual
    print("\nContato atual:")
    exibir_contato(contato, detalhado=True)

    # Edição
    print("\n(Pressione Enter para manter o valor atual)\n")

    novo_nome = input(f"Nome [{contato['nome']}]: ").strip()
    if novo_nome and validar_nome(novo_nome):
        contato["nome"] = novo_nome.title()

    novo_tel = input(f"Telefone [{contato.get('telefone', '')}]: ").strip()
    if novo_tel:
        if validar_telefone(novo_tel):
            contato["telefone"] = novo_tel
        else:
            print("⚠ Telefone inválido, mantendo anterior.")

    novo_email = input(f"Email [{contato.get('email', '')}]: ").strip()
    if novo_email:
        if validar_email(novo_email):
            contato["email"] = novo_email.lower()
        else:
            print("⚠ Email inválido, mantendo anterior.")

    nova_cat = input(f"Categoria [{contato.get('categoria', 'Geral')}]: ").strip()
    if nova_cat:
        contato["categoria"] = nova_cat.title()

    novas_notas = input(f"Notas [{contato.get('notas', '')}]: ").strip()
    if novas_notas:
        contato["notas"] = novas_notas

    # Salva
    if salvar_contatos(contatos):
        print("\n✅ Contato atualizado com sucesso!")
    else:
        print("\n⚠ Erro ao salvar alterações.")


def excluir_contato(contatos):
    """Exclui um contato da agenda."""
    print("\n--- EXCLUIR CONTATO ---\n")

    if len(contatos) == 0:
        print("📭 A agenda está vazia.")
        return

    termo = pedir_texto("Nome do contato para excluir: ")
    encontrados = buscar_por_nome(contatos, termo)

    if len(encontrados) == 0:
        print(f"\n❌ Nenhum contato encontrado com '{termo}'.")
        return

    # Mostra encontrados
    for contato in encontrados:
        exibir_contato(contato)

    if len(encontrados) > 1:
        try:
            id_escolhido = int(pedir_texto("\nDigite o ID do contato a excluir: "))
            contato = buscar_por_id(contatos, id_escolhido)
        except ValueError:
            print("❌ ID inválido.")
            return
    else:
        contato = encontrados[0]

    if not contato:
        print("❌ Contato não encontrado.")
        return

    # Confirmação
    if pedir_confirmacao(f"\n⚠️ Excluir '{contato['nome']}'?"):
        contatos.remove(contato)
        if salvar_contatos(contatos):
            print("\n✅ Contato excluído com sucesso!")
        else:
            print("\n⚠ Erro ao salvar alterações.")
    else:
        print("\n❌ Operação cancelada.")


def mostrar_estatisticas(contatos):
    """Mostra estatísticas da agenda."""
    print("\n--- ESTATÍSTICAS ---\n")

    total = len(contatos)
    print(f"📊 Total de contatos: {total}")

    if total == 0:
        return

    # Contagem por categoria
    categorias = {}
    for c in contatos:
        cat = c.get("categoria", "Geral")
        categorias[cat] = categorias.get(cat, 0) + 1

    print("\n📁 Por categoria:")
    for cat, qtd in sorted(categorias.items()):
        porcentagem = (qtd / total) * 100
        print(f"   {cat}: {qtd} ({porcentagem:.0f}%)")

    # Com email/telefone
    com_email = sum(1 for c in contatos if c.get("email"))
    com_telefone = sum(1 for c in contatos if c.get("telefone"))

    print(f"\n📧 Com email: {com_email}")
    print(f"📞 Com telefone: {com_telefone}")


def exportar_para_texto(contatos):
    """Exporta contatos para um arquivo de texto."""
    print("\n--- EXPORTAR CONTATOS ---\n")

    if len(contatos) == 0:
        print("📭 A agenda está vazia.")
        return

    nome_arquivo = "contatos_exportados.txt"

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write("=" * 50 + "\n")
            f.write("        AGENDA DE CONTATOS\n")
            f.write(f"        Exportado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            f.write("=" * 50 + "\n\n")

            for c in sorted(contatos, key=lambda x: x["nome"]):
                f.write(f"Nome: {c['nome']}\n")
                if c.get("telefone"):
                    f.write(f"Telefone: {c['telefone']}\n")
                if c.get("email"):
                    f.write(f"Email: {c['email']}\n")
                f.write(f"Categoria: {c.get('categoria', 'Geral')}\n")
                if c.get("notas"):
                    f.write(f"Notas: {c['notas']}\n")
                f.write("-" * 30 + "\n\n")

            f.write(f"\nTotal: {len(contatos)} contato(s)\n")

        print(f"✅ Contatos exportados para '{nome_arquivo}'!")

    except Exception as e:
        print(f"❌ Erro ao exportar: {e}")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    """Função principal do programa."""
    # Carrega contatos existentes
    contatos = carregar_contatos()

    exibir_cabecalho()
    print(f"\n📂 {len(contatos)} contato(s) carregado(s).")

    # Loop principal
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            adicionar_contato(contatos)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            buscar_contato(contatos)
        elif opcao == "4":
            editar_contato(contatos)
        elif opcao == "5":
            excluir_contato(contatos)
        elif opcao == "6":
            mostrar_estatisticas(contatos)
        elif opcao == "7":
            exportar_para_texto(contatos)
        elif opcao == "0":
            print("\n👋 Até logo! Seus contatos foram salvos.")
            break
        else:
            print("\n⚠ Opção inválida! Digite um número de 0 a 7.")

        input("\nPressione Enter para continuar...")


# Executa o programa
if __name__ == "__main__":
    main()


# ============================================================
# DESAFIOS EXTRAS PARA O ALUNO
# ============================================================
#
# 1. Adicionar campo "aniversário" e mostrar aniversariantes do mês
# 2. Implementar busca por telefone ou email
# 3. Adicionar opção de favoritar contatos
# 4. Criar backup automático do arquivo JSON
# 5. Implementar importação de contatos de arquivo texto
# 6. Adicionar foto do contato (como URL)
# 7. Criar sistema de grupos (um contato em vários grupos)
#
# ============================================================


# ============================================================
# O QUE VOCÊ APRENDEU NESTE MÓDULO:
# ============================================================
# ✓ Funções para organizar e reutilizar código
# ✓ Dicionários para estruturar dados
# ✓ Arquivos JSON para persistência de dados
# ✓ try/except para tratar erros graciosamente
# ✓ Módulos para organizar projetos grandes
# ✓ Validação de dados do usuário
# ✓ Interface de menu interativo
#
# PARABÉNS! Você completou o Módulo 2! 🎉
# Você já sabe criar programas organizados e robustos!
# ============================================================
