mais = 0
homens = 0
cont = 1
menor = 0
while True:
    print('~~'* 30)
    print('                      Casdastro de Pessoa')
    print('~~'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    escolha = str(input('Quer continuar[S/N]: ')).strip().upper()
    if sexo == 'M':
        homens += 1 
    if idade > 18:
        mais += 1
    if idade < 20 and sexo == 'F':
        menor += 1
    if escolha == 'N':
        print(' ')
        print('(FINALIZADO)')
        break
print(f'{mais} pessoas tem maiores de 18 anos, {homens} homens foram cadastrados e {menor} mulheres são menores')