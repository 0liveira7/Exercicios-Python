from calendar import isleap
ano = int(input('Digite o ano: '))

if isleap(ano):
    print(f'o ano \033[30;41m{ano}\033[m é bissexto.')
    
else:
    print(f'O ano \033[7;35;43m{ano}\033[m Não é bissexto.')

