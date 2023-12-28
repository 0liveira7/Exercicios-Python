from random import sample

n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))

lista = sample([n1, n2, n3, n4], k=4)


print(f"A ordem de apresentação será: {lista}")