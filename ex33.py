a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

menor = a 
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c

maior = b
if a>b and a>c:
    maior = a
if c>b and c>a:
    maior = c

print('O menor valor digitado foi {} '.format(menor))
print('O maior valor digitado foi {}'.format(maior))