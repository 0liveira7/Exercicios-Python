num = int(input('Digite um número inteiro: '))

print('==='*20)
print('Escolha a base de conversão!')
print('==='*20)

print('''
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal
      ''')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'O número {num} convertido para binário fica: {bin(num)[2:]}')

elif opção == 2:
    print(f'O número {num} convertido para Octal fica: {oct(num)[2:]}')

elif opção == 3:
    print(f'O número {num} convertido para Hexadecimal fica: {hex(num)[2:]}')
    
else:
    print('Opção Inválida, tente novamente!')