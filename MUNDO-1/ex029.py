velo = int(input('Quantos km/h o carro estava? '))
limite = 80
valor_multa = 7

if velo > limite:
    excesso = velo - limite
    multa = excesso * valor_multa
    print('Você foi multado!!! ')
    print(f'Sua Multa é no valor de {multa:.2f}R$ ')
    
else:
    print('Você está dentro do limite de velocidade siga em frente! ')    