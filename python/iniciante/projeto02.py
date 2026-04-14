'''
Desafio nivel 2: Verificador de números Impares ou Pares
'''

print('---Verificador de números---')

numero = int(input('Qual número você gostaria de verificar: '))

resto = numero % 2

if resto == 0:
    print('Este número é PAR')
else:
    print('Este número é IMPAR')