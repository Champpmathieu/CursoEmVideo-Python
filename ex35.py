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