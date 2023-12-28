#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


num = int(input('Digite um numero: '))

contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

print(f'O numero {num} foi divisivel {contador} vezes')


if contador == 2:
    print('O número é PRIMO!')
else:
    print('O número não é PRIMO!')