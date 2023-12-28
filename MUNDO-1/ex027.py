nome_completo = str(input('Digite um nome: ').strip())

primeiro = nome_completo.split()[0]
ultimo = nome_completo.split()[-1]


print(nome_completo)
print(f'O primeiro nome é, {primeiro}')
print(f'O ultimo nome é, {ultimo}')
