import json


tarefas = []


def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)


def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    prioridade = input("Prioridade da tarefa (baixa/média/alta): ").lower()
    while prioridade != 'baixa' and prioridade != 'média' and prioridade != 'alta':
      print('Prioridade inválida. Digite (baixa/média/alta)')
      prioridade = input("Prioridade da tarefa (baixa/média/alta): ").lower()
    status = "pendente"  # Padrão ao adicionar uma tarefa
    tarefas.append({"nome": nome, "descricao": descricao, "prioridade": prioridade, "status": status})
    salvar_tarefas()  


def atualizar_tarefa():
    mostrar_tarefas()
    id_tarefa_str = input("Digite o ID da tarefa que deseja atualizar: ")

    # Verificar se a entrada é um número
    if not id_tarefa_str.isdigit():
        print("ID inválido. Digite um número.")
        return

    id_tarefa = int(id_tarefa_str)

    if id_tarefa < 1 or id_tarefa > len(tarefas):
        print("ID inválido.")
        return

    tarefa = tarefas[id_tarefa - 1]
    print("Informações atuais da tarefa:")
    exibir_tarefa(tarefa)
    campo_para_atualizar = input("Digite o campo que deseja atualizar (nome/descrição/prioridade/status): ").lower()
    novo_valor = input(f"Digite o novo valor para {campo_para_atualizar}: ")
    tarefa[campo_para_atualizar] = novo_valor
    print("Tarefa atualizada com sucesso.")
    exibir_tarefa(tarefa)
    salvar_tarefas()  # Salvar as tarefas após atualizar


def excluir_tarefa():
    mostrar_tarefas()
    id_tarefa = int(input("Digite o ID da tarefa que deseja excluir: "))
    if id_tarefa < 1 or id_tarefa > len(tarefas):
        print("ID inválido.")
        return
    tarefa = tarefas.pop(id_tarefa - 1)
    print("Tarefa excluída com sucesso:")
    exibir_tarefa(tarefa)
    salvar_tarefas()


def mostrar_tarefas():
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"ID: {i}")
        exibir_tarefa(tarefa)


def exibir_tarefa(tarefa):
    print(f"Nome: {tarefa['nome']}")
    print(f"Descrição: {tarefa['descricao']}")
    print(f"Prioridade: {tarefa['prioridade']}")
    print(f"Status: {tarefa['status']}")
    print("-----------")


def filtrar_tarefas():
    status_filtro = input("Filtrar por status (pendente/concluída): ").lower()
    prioridade_filtro = input("Filtrar por prioridade (baixa/média/alta): ").lower()

    tarefas_filtradas = [tarefa for tarefa in tarefas if (status_filtro in tarefa['status']) and (prioridade_filtro in tarefa['prioridade'])]

    print("\nTarefas filtradas:")
    for tarefa in tarefas_filtradas:
        exibir_tarefa(tarefa)


def priorizar_tarefas():
    tarefas_ordenadas = sorted(tarefas, key=lambda x: ("alta", "média", "baixa").index(x["prioridade"]))
    print("\nLista de Tarefas Priorizadas:")
    for tarefa in tarefas_ordenadas:
        exibir_tarefa(tarefa)


def estatisticas_tarefas():
    total_tarefas = len(tarefas)
    tarefas_pendentes = sum(1 for tarefa in tarefas if tarefa['status'] == 'pendente')
    tarefas_concluidas = sum(1 for tarefa in tarefas if tarefa['status'] != 'pendente')

    print(f"\nEstatísticas das Tarefas:")
    print(f"Total de Tarefas: {total_tarefas}")
    print(f"Tarefas Pendentes: {tarefas_pendentes}")
    print(f"Tarefas Concluídas: {tarefas_concluidas}")


def exibir_menu():
    print("\nEscolha uma opção:")
    print("1. Adicionar Tarefa")
    print("2. Atualizar Tarefa")
    print("3. Excluir Tarefa")
    print("4. Mostrar Tarefas")
    print("5. Filtrar Tarefas")
    print("6. Priorizar Tarefas")
    print("7. Estatísticas das Tarefas")
    print("0. Sair")

tarefas = carregar_tarefas()


while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada (0 a 7): ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        atualizar_tarefa()
    elif opcao == "3":
        excluir_tarefa()
    elif opcao == "4":
        mostrar_tarefas()
    elif opcao == "5":
        filtrar_tarefas()
    elif opcao == "6":
        priorizar_tarefas()
    elif opcao == "7":
        estatisticas_tarefas()
    elif opcao == "0":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")