n = s = 0
while True:
    n = int(input('DIGITE: '))
    if n == 999:
        break
    s += n
print(f'Soma = {s}')