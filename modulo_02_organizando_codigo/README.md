# Módulo 2: Organizando Código e Dados

**Duração:** 12 horas
**Pré-requisitos:** Módulo 1 completo

## Objetivo do Módulo

Ensinar os alunos a escrever código reutilizável, trabalhar com estruturas de dados mais complexas, salvar informações em arquivos e criar programas que não quebram com erros.

## Estrutura das Lições

| Lição | Arquivo | Tópico | Duração |
|-------|---------|--------|---------|
| 2.1 | `1_funcoes.py` | Funções, parâmetros, return | 2h |
| 2.2 | `2_dicionarios.py` | Dicionários, chaves, valores | 2h |
| 2.3 | `3_arquivos.py` | Leitura/escrita, JSON | 2h |
| 2.4 | `4_erros.py` | try/except, validação | 2h |
| 2.5 | `5_modulos.py` | import, biblioteca padrão | 2h |
| 2.6 | `6_projeto_agenda.py` | Projeto integrador | 2h |

## Conceitos Aprendidos

### Lição 2.1 - Funções
- `def` para criar funções
- Parâmetros e argumentos
- `return` para devolver valores
- Valores padrão de parâmetros

### Lição 2.2 - Dicionários
- Estrutura `{chave: valor}`
- Métodos `.keys()`, `.values()`, `.items()`
- Acesso seguro com `.get()`
- Listas de dicionários

### Lição 2.3 - Arquivos
- `open()` com modos "r", "w", "a"
- Uso do `with` para fechar automaticamente
- JSON para dados estruturados
- `json.dump()` e `json.load()`

### Lição 2.4 - Tratamento de Erros
- Blocos `try/except`
- Erros específicos (ValueError, TypeError, etc.)
- `else` e `finally`
- Criando erros com `raise`

### Lição 2.5 - Módulos
- `import` e `from...import`
- Módulos `random`, `datetime`, `math`, `os`
- Criando seus próprios módulos
- Instalando pacotes com `pip`

## Entregável Final

**Agenda de Contatos** com:
- Adicionar, listar, buscar, editar e excluir contatos
- Dados salvos em arquivo JSON
- Tratamento de erros
- Validação de dados

## Para Executar

```bash
cd modulo_02_organizando_codigo
python 1_funcoes.py
```

## Arquivos Gerados

O projeto da agenda cria:
- `agenda_contatos.json` - Dados dos contatos
- `contatos_exportados.txt` - Exportação em texto

## Dica para Instrutores

Mostre primeiro o código repetitivo e desorganizado, depois mostre como funções e módulos resolvem o problema. Deixe os alunos "sentirem a dor" antes de oferecer a solução.
