#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.


s = 0
cont = 0


for i in range(1, 7):
    num = int(input(f'Digite o {i}° valor : '))
    if num % 2 == 0: 
        s += num
        cont += 1
        

print(f'Você informou {cont} numeros PARES e a soma deu {s}')

