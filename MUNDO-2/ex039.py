
ano = int(input('Digite o seu ano de nascimento: '))
data = 2004
ano_atual = 2023

idade = ano_atual - ano

if idade < 18:
    print('Você ainda irá se alistar!')

elif idade == 18:
    print('É hora de você se alistar!')

else:
    expirado = idade - 18
    print(f'Já passou {expirado} anos do tempo de alistamento!')