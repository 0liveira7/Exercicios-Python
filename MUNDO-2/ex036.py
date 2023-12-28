valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salário?' ))
anos = int(input('Em quantos anos você pretende pagar tudo? '))

prestacao = valor_casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${valor_casa} em {anos} anos, a prestação será de R${prestacao:.2f}')

if prestacao <= minimo:
    print(f'Empréstimo pode ser CONCEDIDO!')
else:
    print(f'Empréstimo NEGADO! ')
    