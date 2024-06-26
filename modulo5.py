# Exemplo de condições aninhadas em Python

idade = int(input("Digite sua idade: "))

if idade > 18:
    print("Você é maior de idade.")
    if idade >= 60:
        print("Você é idoso.")
    else:
        print("Você não é idoso.")
elif idade == 18:
    print("Você acabou de atingir a maioridade.")
else:
    print("Você é menor de idade.")
