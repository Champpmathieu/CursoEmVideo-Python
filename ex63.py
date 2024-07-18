print("=="*20)
print('          Sequêcia Fibonacci'        )
print('=='*20)
n = int(input('Quanto termos voçê quer mostrar: '))
termo1 = 0
termo2 = 1
print('~'*30)
print('{} - {}'.format(termo1, termo2), end='')
contador = 3
while contador <= n:
    termo3 = termo1 + termo2
    print(' - {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1