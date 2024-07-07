sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos insira o seu sexo novamente: ')).upper().strip()[0]
print("Valor {} armazenado!".format(sexo))