nome = str(input('Digite o nome completo: ').strip())

print(nome.strip().upper())
print(nome.strip().lower())

espaços = nome.count(' ')
print(f'Seu nome ao todo tem {len(nome)- espaços} letras' )


separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')










