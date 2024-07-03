soma = 0
for c in range(1, 5):
    print('------------ {} PESSOA ------------'.format(c))
    #nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    #sexo = str(input('SEXO [M\F]: '))
    soma += idade
media = soma/4
print(soma)
print(media)