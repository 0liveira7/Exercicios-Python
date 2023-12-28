#usando o choice
from random import choice
num = int(input('Digite um número inteiro: '))
print('==='*20)
print('Escolha a base de conversão')
print('==='*20)

print('a.  para Binário')
print('b.  para Octal')
print('c.  para Hexadecimal')

print('Digite sua escolha : ')
choice = input()


if choice == 'a':
    print(f'O número {num} em Binário é: ' + bin(num)[2:])

if choice == 'b':
    print(f'O número {num} em Octal é: ' + oct(num)[2:])

if choice == 'c':
    print(f'O número {num} em Hexadecimal é: ' + hex(num)[2:])
    
else:
    print('Opção inválida, tente novamente!')

