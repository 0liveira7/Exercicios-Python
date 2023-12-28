#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

data = date.today().year
contador = 0
contador2 = 0

for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    idade = data - ano
    
    if idade >= 21:
        contador += 1
    else:
        contador2 += 1
 
print(f'Ao todo tivemos {contador} pessoa(s) maiores de idade')
print(f'E também tivemos {contador2} pessoa(s) menores de idade')