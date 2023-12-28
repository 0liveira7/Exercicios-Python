# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite um número inteiro para calcular o fatorial: '))

contador = 1 
fatorial = 1

while contador <= numero:
    fatorial *= contador
    contador += 1
        
print(f'O fatorial de {numero} é {fatorial}')
