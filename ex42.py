print('-=-' * 20)
print('Analisador de triangulo!')
print('-=-' * 20)
reta1 = float(input('Digite a primeira reta: '))
reta2 = float(input('Digite a segunda reta: '))
reta3 = float(input('Digite a terceira reta: '))
if reta1+reta2 > reta3 and reta1+reta3 > reta2 and reta2+reta3 > reta1:
    print('É possivel construir um triangulo a partir desses valores!')
else:
    print('Não é possivel contruir um triangulo a partir desses')

if reta1 == reta2 == reta3:
    print('Esse é um triangulo EQUILÁTERO: todos os lados iguais')
elif (reta1 == reta2) != reta3 and (reta2 == reta3) != reta1 and (reta1 == reta3) != reta2:
    print('Este é um triangulo ISÓSCELES: dois lados iguais, um diferente')
elif reta1 != reta2 != reta3:
    print('Esse é um triangulo ESCALENO: todos os lados diferentes')