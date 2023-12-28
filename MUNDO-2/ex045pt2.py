from random import choice
from time import sleep
print('''
      
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA

      ''')

player = int(input('Qual é a sua jogada? '))

lista = 'PEDRA', 'PAPEL', 'TESOURA'

pc = choice(lista)


sleep(2)
print('JO')

sleep(1)
print('KEN')

sleep(1)
print('PO')

if player == 0:
    print(f'{lista[0]} X {pc} ')
    if pc == lista[0]:
        print('EMPATE!')
    elif pc == lista[1]:
        print('Você Perdeu!')
    elif pc == lista[2]:
        print('Você Ganhou!')

elif player == 1:
    print(f'{lista[1]} X {pc} ')
    if pc == lista[1]:
        print("EMPATE!")
    elif pc == lista[2]:
        print('Você Perdeu!')
    elif pc == lista[0]:
        print('Você Ganhou!')

elif player == 2:
    print(f'{lista[2]} X {pc}')
    if  pc == lista[2]:
        print('EMPATE!')
    elif pc == lista[1]:
        print('Você Ganhou!')
    elif pc == lista[0]:
        print('Você Perdeu!')


else:
    print('Opção Inválida, tente novamente')

        
 
     
