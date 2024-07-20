escolha = ''
contador = 0
soma = 0
maior = 0
menor = 0
while escolha != 'N':
    numero = float(input('Digite um numero: '))
    escolha = str(input('Quer continuar?[S/N]: ')).strip().upper()
    contador += 1
    soma += numero
    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor =  numero
media = soma / contador
print('Você digitou {} números e a média foi {}'.format(contador,media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))