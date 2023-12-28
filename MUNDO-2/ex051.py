#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(termo, 10, razao):
    termo += razao
    
    print(f'{termo}', end=' -> ')
    
print('Acabou!')

