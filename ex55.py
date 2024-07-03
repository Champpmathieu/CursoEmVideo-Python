maior = 0
menor = 0
for c in range(1, 6):
    num = float(input('Digite o peso da pessoa {}: '.format(c)))
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))