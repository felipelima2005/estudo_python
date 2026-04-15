'''
Desafio nivel 1: Tabuada
'''

print('---Bem-Vindo a sua Tabuada---')


contador = 0
tabuada = int(input('Você quer a tabuada de qual número: '))

while contador != 11:
    resultado = contador * tabuada
    print(f'{contador} x {tabuada} = {resultado}')
    contador += 1