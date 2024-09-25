import os
os.system('cls')

clientes = []
opcao = ""

while opcao != "n":  
    print("\nFila atual de clientes:")
    print(clientes if clientes else "Nenhum cliente na fila.")
    
    print("\nOpções:")
    print('"a" para atender um cliente')
    print('"c" para cadastrar um novo cliente')
    print('"n" para sair')

    opcao = input("Escolha uma opção: ")

    if opcao == "c":
        cliente = input('Digite o nome do cliente: ')
        if cliente:
            clientes.append(cliente)
            os.system('cls')
            print(f'Cliente {cliente} adicionado à fila.')
        else:
            os.system('cls')
            print('Nome do cliente não pode ser vazio.')
    
    elif opcao == "a":
        if clientes:
            cliente_atendido = clientes.pop()
            os.system('cls')
            print(f'Atendendo {cliente_atendido}')
        else:
            os.system('cls')
            print('Não há clientes na fila para atender.')
    
    elif opcao == "n":
        os.system('cls')
        print("Encerrando o atendimento.")
    
    else:
        os.system('cls')
        print("Opção inválida! Tente novamente.")

print('Todos os clientes foram atendidos.')