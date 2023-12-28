km = int(input('Qual a distância da viagem que você irá fazer em Km? '))

preço_200 = 0.50 
preço_longo = 0.45

if km <= 200:
    valor = km * preço_200
    print(f'você irá pagar {valor:.2f}R$')
    
else:
    valor2 = km * preço_longo 
    print(F'VocÊ irá pagar {valor2:.2F}R$' )
    