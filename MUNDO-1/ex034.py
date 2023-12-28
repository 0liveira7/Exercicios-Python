sal = eval(input('Digite o seu salário R$: '))

sal_base = 1250.0


if sal > sal_base:
    reajuste = sal + (sal * 10 / 100)
    print(f'Seu salário de {sal:.2f}R$ com o aumento de 10% fica no valor de {reajuste:.2f}R$')
else:
    reajuste2 = sal + (sal * 15 / 100)
    print(f'Seu salário de \033[33;34m{sal:.2f}R$\033[m com o aumento de 15% fica no valor de \033[33;34m{reajuste2:.2f}R$\033[m')
    


