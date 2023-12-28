#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai pensar em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

pc = randint(0, 10)
acertou = False
palpites = 0


while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True

print(f'Acertou com {palpites} tentativas. Parabéns!')
    
    
    
