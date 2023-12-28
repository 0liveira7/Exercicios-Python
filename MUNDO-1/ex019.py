
from random import choice

nome1 = input("Primeiro aluno: ")
nome2 = input("Segundo aluno: ")
nome3 = input("Terceiro aluno: ")
nome4 = input("Quarto aluno: ")

sorteio = choice([nome1, nome2, nome3, nome4])


print(f"O aluno sorteado foi o(a) {sorteio}")