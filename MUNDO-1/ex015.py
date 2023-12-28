#Aluguel de carros

dias = int(input("Quantos dias alugados? "))
km = int(input("Quantos km rodados? "))

preço_km = (km*0.15)
preço = (dias*60) + preço_km

print(f"O total a pagar é de R${preço}")