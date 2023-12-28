#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('digite um número para ver sua tabuada: '))

for i in range(1, 11):
    cont = i * n
    print(f'{n} x {i} = {cont}')
    
    
