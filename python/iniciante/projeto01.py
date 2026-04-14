'''
Desafio nivel 1: Calculadora Simples
'''
print('-----Bem Vindo a sua Calculadora-----')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

operacao = input('Digite a operação desejada (Soma, Subtração, Multiplicação, Divisão): ')

if operacao.lower() == 'soma':
    resultado = num1 + num2
    print(f'O resultado da soma é: {resultado}')
elif operacao.lower() == 'subtração':
    resultado = num1 - num2
    print(f'O resultado da subtração é: {resultado}')
elif operacao.lower() == 'multiplicação':
    resultado = num1 * num2
    print(f'O resultado da multiplicação é: {resultado}')
elif operacao.lower() == 'divisão':
    resultado = num1 / num2
    print(f'O resultado da divisão é: {resultado}')
else:
    print('a entrada não é compativel')
