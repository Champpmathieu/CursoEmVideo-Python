p = float(input('Qual é o preço do produto:'))
j = int(input('De qual forma irá pagar, dinheiro/cheque: 1,cartão: 2, parcelado 2x: 3, parcelado 3x: 4 : '))
d1 = p - (p*10/100)
d2 = p - (p*5/100)
d3 = p + (p*20/100)
if j == 1:
    print('Voce pagara {:.2f} reais nesse produto'.format(d1))
elif j == 2:
    print('Voce pagara {:.2f} nesse produto'.format(d2))
elif j == 3:
    print('Voce pagara {} nesse produto'.format(p))
elif j == 4:
    print('Voce pagara {:.2f} nesse produto'.format(d3))