h = float(input('Digite o valor da altura de uma parede: '))
l = float(input('Digite o valor da largura da parede: '))
a = h * l
tinta = a/2
print('A área da parede é de {:.2f}m²' .format(a)) #, end=(' '))
print('Sabendo que 1 litro de tinta pinta 2m², você vai precisar de {:.1f} litros de tinta' .format(tinta) )