print(' ')
n = int(input('Digite um numero: '))
print(' ')
print('A tabuada do numero {} é:'.format(n))
print(' ')
for c in range(1, 11):
    print('{} X {} = {}'.format(n, c, c*n))
print(' ')