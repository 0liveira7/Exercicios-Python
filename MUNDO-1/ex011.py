largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area = largura * altura

print(f"Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.2f}m² ")
tinta = area / 2

print(f"Para pintar essa parede você vai precisar de {tinta:.1f}L de tinta. ")

