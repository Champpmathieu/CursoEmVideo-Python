print("=="*20)
print('          10 TERMOS DE UMA PA'        )
print('=='*20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 1
while contador <= 10:
    print('{} '.format(termo), end=" ")
    termo += razao
    contador += 1
print('Fim')