from random import randint

itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)


print('''
      
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA

      ''')

player = int(input('Qual é a jogada? '))
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[pc]}')

if pc == 0:
    print()