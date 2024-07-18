print("=="*20)
print('          10 TERMOS DE UMA PA'        )
print('=='*20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} '.format(termo), end=" ")
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar: '))
print('Progreção finalizada com {} termos mostrados!'.format(total))