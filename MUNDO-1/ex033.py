n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print(f'O Maior número é \033[33;44m{maior}\033[m')
print(f'O Menor número é \033[33;44m{menor}\033[m')

