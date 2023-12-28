# #Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


finalizar = False

while not finalizar:
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite outro valor: '))
    maior = max(v1, v2)
    print('''
           
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

''')
    opcao = int(input('O que você quer fazer com esses valores: '))
    if opcao == 1:
        soma = v1 + v2
        print(f'A soma de {v1} + {v2} é {soma}')
    elif opcao == 2:
        multi = v1 * v2
        print(f'A multiplicação de {v1} x {v2} é {multi}')
    elif opcao == 3:
        print(f'O maior número de {v1} e {v2} é o {maior}')
    elif opcao == 4:
        print('Digite novamente novos valores: ')
    elif opcao == 5:
        break

        
        
