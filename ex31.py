km = float(input('Digite a distancia da viagem: '))
preco = km * 0.50
desconto = km * 0.45
print(preco)
if km >= 200:
    print('O preço da sua passagem vai ser R${} com os desconto da temporada!'.format(desconto))
else:
    print('O preço da sua passagem vai ser R${}'.format(preco))
    