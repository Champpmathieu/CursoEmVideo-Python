s = int(input('Digite o salário de um funcionário: '))
clt = (s*15/100) + s
rico = (s*10/100) + s
if s > 1250:
    print('Agora o salario do funcionario pj passa a ser R${}'.format(rico))
else:
    print('Agora o salario do funcionario clt passa a ser R${}'.format(clt))
