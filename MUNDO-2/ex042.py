r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and r1 > r2 - r3 and r2 > r1 - r3 and r3 > r2 - r1:
    if (r1 == r2 and r1 == r3 and r2 == r3):
         print('É um triângulo EQUILÁTERO.')

    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('É um triângulo ESCALENO. ')

    else:
     print('É um triângulo ISÓCELES')

else:
    print('Não é possivel formar um triângulo, tente novamente')