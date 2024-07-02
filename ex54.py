from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Digite o ano que a pessoa {} nasceu:'.format(pessoa)))
    idade = atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print('A quantidade pessoas menores de idade são {}, e as maiores de idade são {}'.format(totalmenor, totalmaior))