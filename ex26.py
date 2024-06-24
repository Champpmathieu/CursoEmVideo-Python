frase = input('digite uma frase: ').strip().lower()
print('sua frase tem essa quantidade de letras A {}'.format(frase.count('a')))
print('a primeira letra A apareceu na posição {}'.format(frase.find('a')))
print('a ultima letra A apareceu na posição {}'.format(frase.rfind('a')))