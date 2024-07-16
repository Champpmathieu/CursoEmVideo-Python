from time import sleep
numero = int(input('Digite um numero: '))
print('Calculando (.)')
sleep(3)
print('Calculando (..)')
sleep(3)
print('Calculando (...)')
sleep(3)
print('Calculando (....)')
sleep(3)
c = numero
f = 1
print('Fatorando {}! = '.format(numero), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))
#print('O fatorial do numero {} é {}'.format(numero,fatorial))