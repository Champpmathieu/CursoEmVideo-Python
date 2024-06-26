n = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'))
if escolha == 1:
    print(bin(n))
elif escolha == 2:
    print(oct(n))
elif escolha == 3:
    print(hex(n))
print('Fim')