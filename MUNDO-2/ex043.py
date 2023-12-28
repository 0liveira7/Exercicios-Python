peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do Peso ')

elif 18.5 <= imc <= 25:
    print('Você está no peso ideal ')

elif 25 <= imc <= 30:
    print('SOBREPESO ')

elif 30 <= imc <= 40:
    print('Obesidade! ')

else:
    print('Você ta com OBESIDADE MÓRBIDA! NIVEL THAIS CARLA!')

