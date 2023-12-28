preço = float(input('Preço das compras: R$'))

print('==='*20)
print('                          Lojinha') 
print('==='*20)

print('''
      
FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
 
      ''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    valor = preço - (preço * 10 / 100)
    print(f'O preço de {preço}R$ com 10% de desconto pagando à vista com dinheiro/cheque vai ficar em {valor}R$ ')

elif opcao == 2:
    valor = preço - (preço * 5 / 100)
    print(f'O preço de {preço}R$ com 5% de desconto pagando à vista no cartão vai ficar em {valor}R$ ')

elif opcao == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra de R${preço:.2f} será parcelada em 2x de R${parcela:.2f} SEM JUROS')

elif opcao == 4:
    parcela = int(input('Quantas parcelas vão ser? '))
    taxa = 0.20
    valor = (preço / parcela) * (1 + taxa)
    preço_final = preço + (20 / 100 * preço)
    print(f'Sua compra será parcelada em {parcela}x de {valor:.2f} com JUROS')
    print(f'Sua compra de R${preço:.2f} vai custar {preço_final:.2f} no final. ')
    
else:
    print('\033[31;41mOpção de pagamento inválida, tente novamente\033[m')

