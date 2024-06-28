i = int(input('Qual é a sua idade: '))
if i <=9:
    print('Você está na categoria MIRIM')
elif i > 9 and i <= 14:
    print('Você está na categoria INFANTIL')
elif i > 14 and i <= 19:
    print('Você está na categoria JUNIOR')
elif i > 19 and i <= 25:
    print('Você está na categoria SÊNIOR')
elif i > 25:
    print('Você está na categoria MASTER')