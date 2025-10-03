# Gerenciador de tarefas - Manipulação de Arquivos 
ARQUIVO = "tarefas.txt"

# Função para carregar as tarefas
def carregar_tarefas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as file:
            return [linha.strip().split(" | ") for linha in file.readlines()]
    except FileNotFoundError:
        return[]
    
# Função para salvar as tarefas 
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as file:
        for tarefa, status in tarefas:
            file.write(f"{tarefa} | {status}\n")

 # Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append([descricao, "❌ Pendente"])
    salvar_tarefas(tarefas)
    print(f"Tarefa" '{descrição}' "adicionada com sucesso!\n")

# Função par alistar todas as tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.\n")
    else:
        for i, (descricao, status) in enumerate(tarefas,start=1):
            print(f"{i}. {descricao} - {status}")
        print()

# função para marcar uma tarefa como concluída
def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) -1
        if 0 <= indice < len(tarefas):
            print(f"Tarefa '{tarefas[indice][0]} marcada como concluída e removida! \n")
            del tarefas[indice] #Remove a tarefa automaticamente
            salvar_tarefas(tarefas)
        else:
            print("Número inválido. \n")
    except ValueError:
        print("Por favor, digite um número válido. \n")

# Função para excluir uma tarefa manualmente
def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja excluir: ")) - 1
        if 0 <= indice < len(tarefas):
            print(f"Tarefa '{tarefas[indice][0]}') excluída com sucesso! \n" )
            del tarefas[indice]
            salvar_tarefas(tarefas)
        else:
            print("Número inválido.\n")
    except ValueError:
        print(" Por favr, digite um número válido. \\n")

# Menu principal
def main():
    tarefas = carregar_tarefas()

    while True:
        print("1. Adicionar Tarefa")
        print("2. listar tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Excluir tarefa")
        print("5. Sair")
        escolha = input("escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            concluir_tarefa(tarefas)
        elif escolha == "4":
            excluir_tarefa(tarefas)
        elif escolha == "5":
            print("Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
