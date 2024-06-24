import math


gorda = float(input('Digite um número: '))
gordo = float(input('Digite outro número: '))
obeso = gordo + gorda


# A função math.ceil deve ser aplicada ao valor da soma
soma_arredondada = math.ceil(obeso)


# A string de formatação deve ser feita corretamente e a função format() deve ser aplicada diretamente na string
print('A soma arredondada entre o número {} e o número {} é igual a {}'.format(gorda, gordo, soma_arredondada))
