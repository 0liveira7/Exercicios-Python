#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho 
# e quantas mulheres têm menos de 20 anos.


soma = 0
media = 0
maioridadehomem = 0
nomevelho = 0
totalmulher20 = 0


for p in range(1, 5):
    print(f'----- {p}° PESSOA  -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
        
media = soma / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos.')

