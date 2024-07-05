somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhernova = 0
for c in range(1, 5):
    print('------------ {} PESSOA ------------'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    somaidade += idade
    if idade < 20 and sexo in 'Ff':
        mulhernova += 1
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    else:
        if idade > maioridadehomem and sexo in 'Mm':
            maioridadehomem = idade
            nomevelho = nome
mediaidade = somaidade/4
print('A média de idade dessas pessoas é {}.'.format(mediaidade))
print('A idade do homem mais velho é {} e seu nome é {}'.format(maioridadehomem, nomevelho))
print("A quantidade de pessoas menores de 20 anos é {}".format(mulhernova))