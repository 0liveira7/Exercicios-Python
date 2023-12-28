frase = input('Digite uma frase: ').upper().strip()

quantidade_a = frase.count('A')
 
primeira = frase.find('A') + 1
ultima = frase.rfind('A') + 1


print(f'A quantidade de vezes que a letra A aparece é {quantidade_a}')
print(f'A primeira posição da letra A aparece em {primeira}')
print(f'A última posição da letra A surge na posição {ultima}')

 

