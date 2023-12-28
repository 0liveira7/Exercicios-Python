#Reajuste Salárial

sal = float(input("Qual o salário do Funcionário? R$"))
novo = sal + (sal * 15 / 100)

print(f"Um funcionário que ganhava R${sal}, com 15% de aumento, passa a receber R${novo:.2f}")