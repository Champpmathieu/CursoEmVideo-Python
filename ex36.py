casa = float(input('Qual é o valor da casa: '))
dindin = float(input('Qual é o seu salário: '))
ano = int(input('Em quantos anos quer pagar: '))
prestação = casa / (ano * 12)
tolerancia = dindin*30/100
if prestação > tolerancia:
    print('Seu emprestimo foi NEGADO por não atender aos requisitos!')
else:
    print('Seu emprestimo foi APROVADO por atender aos requisitos!')