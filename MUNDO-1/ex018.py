#Seno, Cosseno e Tangente

import math

ang = int(input('Ângulo: '))
rad = math.radians(ang)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f"Calculando o valor do angulo de {ang}, podemos afirmar que o seno é {seno:.2f}, seu cosseno é {cosseno:.2f} e sua tangente é {tangente:.2f}")

