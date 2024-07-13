# Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
import time
soma = 0
maior = 0
multiplicacao = 0
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
    primeiroValor = float(input('Digite o primeiro valor: '))
    segundovalor = float(input("Digite o segundo valor: "))
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] saber maior número')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    EscolhaDoUsuario = int(input('>>>>>> Qual a sua opção?: '))
if EscolhaDoUsuario == 1:
    soma = primeiroValor + segundovalor
    print('A soma do valor {} e do valor {} é {}!'.format(primeiroValor, segundovalor, soma))
elif EscolhaDoUsuario == 2:
    multiplicacao = primeiroValor * segundovalor
    print('A multiplicação do valor {} e do valor {} é {}!')

if EscolhaDoUsuario == 3:
    #saber o maior valor das variaveis
    if primeiroValor > segundovalor:
        maior = primeiroValor
    else:
        maior = segundovalor
print('O maior valor desses 2 numeros é {}'.format(maior))
if EscolhaDoUsuario == 4:
    primeiroValor = float(input('Digite o primeiro valor NOVO: '))
    segundovalor = float(input("Digite o segundo valor NOVO: "))
if EscolhaDoUsuario == 5:
    print('Finalizando  .')
    time.sleep(1)
    print('Finalizando  ..')
    time.sleep(1)
    print('Finalizando ...')
    time.sleep(1)
    print('Programa finalizado com sucesso!')