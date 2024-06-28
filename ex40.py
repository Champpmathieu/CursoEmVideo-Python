k = float(input('Digite a sua nota: '))
m = float(input('Digite sua segunda nota: '))
media = (k + m) / 2
if media < 5:
    print('Você está REPROVADO')
elif media >= 5 and media < 7:
    print('Você está de Recuperação')
elif media >= 7:
    print('Você está APROVADO')