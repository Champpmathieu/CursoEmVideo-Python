import time

while True:
    primeiroValor = float(input('Digite o primeiro valor: '))
    segundovalor = float(input("Digite o segundo valor: "))

    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] saber maior número')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    EscolhaDoUsuario = int(input('>>>>>> Qual a sua opção?: '))

    while EscolhaDoUsuario not in [1, 2, 3, 4, 5]:
        print('Valor invalido tente novamente!')
        EscolhaDoUsuario = int(input('>>>>>> Qual a sua opção?: '))

    if EscolhaDoUsuario == 1:
        soma = primeiroValor + segundovalor
        print('A soma do valor {} e do valor {} é {}!'.format(primeiroValor, segundovalor, soma))
    elif EscolhaDoUsuario == 2:
        multiplicacao = primeiroValor * segundovalor
        print('A multiplicação do valor {} e do valor {} é {}!'.format(primeiroValor, segundovalor, multiplicacao))
    elif EscolhaDoUsuario == 3:
        if primeiroValor > segundovalor:
            maior = primeiroValor
        else:
            maior = segundovalor
        print('O maior valor desses 2 números é {}'.format(maior))
    elif EscolhaDoUsuario == 4:
        continue  # Volta ao início do loop para novos números
    elif EscolhaDoUsuario == 5:
        print('Finalizando .')
        time.sleep(1)
        print('Finalizando ..')
        time.sleep(1)
        print('Finalizando ...')
        time.sleep(1)
        print('Programa finalizado com sucesso!')
        break  # Sai do loop e finaliza o programa
