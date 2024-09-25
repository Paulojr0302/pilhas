import os
os.system('cls')

livros = ['livro1', 'livro2', 'livro3']

print(f'existem {len(livros)} livros na pilha, deseja adicionar ou remover algum?')
add_rmv = input(' "a" para adicionar e "r" para remover ou "n" para sair:  ')

while add_rmv != 'n':
    if add_rmv == 'a':
        adicionar = input('Digite o nome do livro: ')
        if adicionar: 
            livros.append(adicionar)
            os.system('cls')
            print(f'Livro {adicionar} incluído na pilha, sendo o {len(livros)}º livro!')
            print(livros)
        else:
            os.system('cls')
            print('Nome do livro não pode ser vazio.')
    elif add_rmv == 'r':
        if len(livros) > 0:
            livros.pop(-1)
            os.system('cls')
            print(f'Livro removido da pilha! Restantes: {livros}')
        else:
            os.system('cls')
            print('Não há mais livros na pilha para remover.')
    elif add_rmv == 'n':
        break
    else:
        print('Comando inválido!')
    
    reset = input('Existem livros novos para empilhar ou remover? (sim/nao): ')
    if reset == 'sim':
        add_rmv = input(' "a" para adicionar e "r" para remover ou "n" para sair:  ')
    elif reset == 'nao':
        break
    else:
        print('Comando inválido!')

print('FINALIZADO')
        
    
        
