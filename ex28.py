from random import randint
computador = randint(0, 5)
print('=+=' * 20)
print('vou pensar em um número entre 0 e 5 tente adivinhar o número...')
print('=+=' * 20)
player = int(input('Em que número pensei? '))
if player == computador:
    print('Você acertou o número!')
else:
    print('Você erro o número!')