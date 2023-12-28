ano = int(input('Digite seu ano de nascimento: '))
data = 2023

idade = data - ano

if idade >= 5 and idade <= 9:
    print(f'Sua idade é {idade} anos, você se enquadra na categoria "MIRIM" ')

elif idade >= 10 and idade <= 14:
    print(f'Sua idade é {idade} anos, voce se enquadra na categoria "INFANTIL" ')

elif idade >= 15 and idade <= 19:
    print(f'Sua idade é {idade} anos, Você se enquadra na categoria "JUNIOR" ')

elif idade == 20:
    print(f'Você tem {idade} anos de idade, e se enquadra na categoria "SÊNIOR" ')

elif idade > 20:
    print(f'Você tem {idade} anos de idade, e já se enquadra na categoria "MASTER" ')
    
else:
    print('Opção inválida, tente novamente')