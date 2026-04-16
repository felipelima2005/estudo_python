
'''
Desafio nivel 3: Jogo de Adivinhação
'''
import random


print('')
print('---Bem-vindo ao Jogo de Adivinhação---')
print('')

aleatorio = random.randint(1,100)
contador = 0

chute = int(input('Chute algum número de 1 a 100: '))

while True:
    if chute > aleatorio:
        chute = int(input('Muito alto! Tente novamente: '))
        contador += 1
        continue
    elif chute == aleatorio:
        print('Parabéns você adivinhou o número aleatório!!')
        contador += 1
        break
    else:
        chute = int(input('Muito baixo! Tente novamente: '))
        contador += 1
        continue

    

print(f'Quantidade de tentativas: {contador}')


