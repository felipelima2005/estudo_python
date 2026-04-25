'''
Desafio nivel 1 : Sistema de Controle de Estoque
'''

estoque = {}
op = 0

while op != 5:
    print('----- Bem-Vindo ao seu Sistema de Controle de Estoque -----')
    print('')
    print('1 - Adicionar produto (nome e quantidade)')
    print('2 - Remover produto')
    print('3 - Atualizar quantidade')
    print('4 - Listar produtos')
    print('5 - Sair')
    op = int(input('Qual opção vc deseja: '))
    match op:
        case 1:
            nome = input('Qual o nome do produto que deseja adicionar: ')
            qtd = int(input('Quantas quantidades deste produto vc deseja adicionar: '))
            estoque.update({nome:qtd})
            print('')
            print(f'{qtd} {nome}s adicionados ao seu estoque com secesso!')
            print('')
        case 2:
            remove = input('Qual produto vc deseja remover: ')
            print('')
            if remove in estoque:
                del estoque[remove]
                print(f'{remove} removido do seu estoque com secesso!')
            else:
                print(f'{remove} não existe em seu estoque')
        case 3:
            auxiliar = input('Qual produto vc deseja atualizar as quantidades: ')
            if auxiliar  in estoque.keys(): 
                atualiza = int(input('Para qual quantidade vc quer atualizar: '))
                print('')
                estoque[auxiliar] = atualiza
                print('')
                print(f'{auxiliar } --> {atualiza}')
            else:
                print('o produto não existe no seu estoque!!')
        case 4:
            print('---Aqui está seu estoque completo---')
            print('')
            for nome, qtd in estoque.items():
                print(f'{nome.upper()} ---> {qtd}')
        case 5:
            print('Saindo do estoque!!')
            break
        case _:
            print('opção não existe!')
            continue


    