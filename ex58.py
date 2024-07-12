from random import randint
computador = randint(0, 1)
tentativas = 0
print('=+=' * 20)
print('vou pensar em um número entre 0 e 1 tente adivinhar o número...')
print('=+=' * 20)
player = int(input('Em que número pensei? '))
while player != computador:
    tentativas += 1
    player = int(input('Você errou o número! Tente novamente outro numero: '))
print('Parabéns você acertou o número! Foram precisos {} tentativas para a resposta correta!'.format(tentativas))