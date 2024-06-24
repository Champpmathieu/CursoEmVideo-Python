entrada = str(input('digite seu nome: ')).strip()
nome = entrada.split()
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[-1]))