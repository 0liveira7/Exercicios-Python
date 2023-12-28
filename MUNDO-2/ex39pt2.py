#com biblioteca
from datetime import date

nasc = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

print('''
      
    Qual o seu Sexo?:
    [1.] Masculino
    [2.] Feminino
    
      ''')

opcao = int(input('Digite aqui: '))



if opcao == 1 and idade == 18:
    print('Tem que se alistar IMEDIATAMENTE!')


elif opcao == 1 and idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta(m) {saldo} ano(s) para o alistamento')
    
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')

elif opcao == 1 and idade > 18:
    saldo = idade - 18
    print(f'Você já everia ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
    

elif opcao == 2:
    print('Você não precisa se Alistar!')

else:
    print('Opção inválida, tente novamente!')