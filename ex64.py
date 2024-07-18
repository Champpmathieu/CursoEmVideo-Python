numero = 0
soma = 0
contador = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    soma += numero
    contador += 1
soma -= 999
contador -= 1
print('A quantida de valores digitados é {} e soma de todos os valores é {}!'.format(contador, soma))