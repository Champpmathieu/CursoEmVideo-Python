# Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
from time import sleep
soma = 0
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