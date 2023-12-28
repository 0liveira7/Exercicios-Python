#Calculando Descontos

produto = float(input("Qual o valor do produto? R$"))
desconto = float(input("Qual o desconto? "))

porcent = produto - (produto * desconto / 100)   # preço antigo, menos (-) a porcentagem de desconto... 

print(f"O produto de valor {produto} com o desconto de {desconto:.0f}% vai passar a custar R${porcent} ")