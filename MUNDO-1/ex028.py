from random import randrange

num = int(input('Digite um número de 0 a 5 e tente acertar o que o computador está pensando: '))
pcnum = randrange(6)


if num == pcnum:
    
    print(f'Você acertou! o computador estava pensando no número: {pcnum}')

else:
    print(f'Você errou! O computador estava pensando no número: {pcnum}')
