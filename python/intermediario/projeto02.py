'''
Desafio nivel 2: Cadastro de alunos
'''

lista = {}
contador = 0

print('')
print('---Bem-vindo a sua ficha de alunos---')
print('')

lista ['Felipe'] = 8.5
lista ['Elias'] = 7
lista ['Milena'] = 6

for nome, nota in lista.items():
    print(f'{nome} --> {nota}')
print('')
media = (sum(lista.values()))/len(lista.keys())
print(f'Média da turma --> {media:.2f}')
print('')
aprovados = []

for nome, nota in lista.items():
    if nota >= 7:
     aprovados.append(nome)

print(f'Aprovados: {','.join(aprovados)}')