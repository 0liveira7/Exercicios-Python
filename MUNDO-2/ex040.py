nt1 = float(input('Digite sua primeira nota: '))
nt2 = float(input('Digite sua seguna nota: '))

media = (nt1 + nt2) / 2

if media < 5.0:
    print(f'Tirando {nt1} e {nt2}, a média do aluno é {media}')
    print('REPROVADO')

elif media <= 6.9:
    print(f'Tirando {nt1} e {nt2}, a média do aluno é {media}')
    print('RECUPERAÇÃO')
    
else:
    print(f'Tirando {nt1} e {nt2}, a média do aluno é {media}')
    print('APROVADO')
    
