import random
a = int(input('Digite um numero, tesoura = 1, papel = 2, pedra = 3: '))
r = random.randint(1, 3)
if r == 1 and a == 1:
    print('Nós empatamos!')
elif r == 2 and a == 2:
    print('Nós empatamos!')
elif  r == 3 and a == 3:
    print('Nós empatamos!')
elif r == 1 and a == 2:
    print('Eu ganhei escolhi tesoura') 
elif r == 1 and a == 3:
    print('Voce ganhou eu escolhi tesoura ')
elif r == 2 and a == 1:
    print('Voce ganhou eu escolhi papel')
elif r == 2 and a == 3:
    print('Eu ganhei escolhi papel')
elif r == 3 and a == 1:
    print('Eu ganhei escolhi pedra')
elif r == 3 and a == 2:
    print('Voce ganhou eu escolhi pedra')