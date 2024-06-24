aluguel = float(input('Quantos dias alugados?'))
rodados = float(input('Quantos Km rodados?'))
alu = aluguel*60
rod = rodados*0.15
total = alu+rod
print('O total a pagar é R${}:'.format(total))