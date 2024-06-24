velocidade = int(input('Digite a velocidade do veiculo: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você está corrento muito rapido!')
    print('Multa de R${} para você!'.format(multa))
else:
    print('tenha uma boa viajem !')