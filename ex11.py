larg = float(input('Digite a largura:'))
altu = float(input('Digite a altura:'))
area = larg*altu
tinta = area/2
print('A seu této tem as dimençôes de {:.0f}x{:.0f} é {:.0f} Metros Quadrados.'
      'E para pintar o seu teto você irá precisar de {} L de tinta!   '
      .format(larg, altu, area, tinta))
