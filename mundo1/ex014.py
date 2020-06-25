# escrevs um programa qe converta a temperatura digitada em c° para °f
c = float(input('Digite a temperatura: '))
f = (c * 9 / 5) + 32
print('A temperatuara de {:.1f}°C corresponde a {:.1f}°F'.format(c, f))
