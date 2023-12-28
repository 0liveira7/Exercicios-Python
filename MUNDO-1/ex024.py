nome = input('Digite o nome de uma cidade: ')

primeiro_nome = nome.split()[0]

if 'santo' in primeiro_nome:
    print(f'A cidade {nome}, contém santo no primeiro nome.') 
    
else:
    print(f'A cidade {nome}, não contém santo no primeiro nome')



