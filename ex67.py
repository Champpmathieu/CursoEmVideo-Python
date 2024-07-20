multiplicação = 0 
while True:
    if n < 0:
        break
    n = int(input('Quer ver a tabuada de que valor?'))
    print('^~'*30)
    for c in range(1, 11):
        multiplicação = c * n
        print(f'{n} x {c} = {multiplicação}')
    print('^~'*30)