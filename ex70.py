baratoPreco = float('inf')  # Inicializa com um valor alto para garantir que qualquer preço seja menor
baratoNome = ''
soma = 0
maior = 0

while True:
    nomeProduto = input('Produto: ').strip()
    precoProduto = float(input('Preço: '))
    continuar = input('Quer continuar? [S/N]: ').strip().upper()

    soma += precoProduto

    if precoProduto >= 1000:
        maior += 1

    # Atualiza a lógica para encontrar o produto mais barato
    if precoProduto < baratoPreco:
        baratoNome = nomeProduto
        baratoPreco = precoProduto

    if continuar == 'N':
        break

print(f'A soma dos produtos é {soma:.2f}!')
print(f'A quantidade de produtos maiores que R$ 1000 é {maior}!')
print(f'O produto mais barato é {baratoNome} (R$ {baratoPreco:.2f})')
