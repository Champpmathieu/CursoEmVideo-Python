salario = float(input('Qual o salário de um funcionário'))
aumento = salario*15/100
aument = salario+aumento
print('Um funcionario que ganhava R${} com o aumento de 15% agora passa a'
      'ganhar R${} '.format(salario, aument))