#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

### Meu código:

# lista: list = ['M', 'F']

# while lista == lista:
#     pessoa = str(input('Digite seu sexo [M/F]: ')).strip().upper()
#     if pessoa == lista[0]:
#         print(f'Seu sexo é o Masculino')
#         break
#     elif pessoa == lista[1]:
#         print(f'Seu sexo é o Feminino')
#         break
#     else:
#         print('Ocorreu algum erro, digite novamente')
        

### Código do Guanabara:

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, Informe novamente seu sexo: ')).strip().upper()[0]
    
print(f'Sexo {sexo} digitado com sucesso!')


    
