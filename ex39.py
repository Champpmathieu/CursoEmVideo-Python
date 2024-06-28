n = int(input('Qual é a sua idade: '))
v = 18 - n
if n == 18:
    print('esse é o ano exato para voce se alistar')
elif n > 18:
    print('voce ja passou da hora de se alistar, ira pagar multa')
elif n < 18:
    print('ainda falta {} anos para voce se alistar'.format(v))