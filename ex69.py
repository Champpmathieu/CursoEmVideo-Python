while True:
    print('~~'* 30)
    print('                      Casdastro de Pessoa')
    print('~~'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    escolha = str(input('Quer continuar[S/N]: ')).strip().upper()
    if escolha == 'N':
        print(' ')
        print('(FINALIZADO)')
        break