from time import sleep

print('{:=^50}' .format('LAÇOS DE REPETIÇÃO - ITERAÇÕES'))

for c in range(1, 6):
    # VAI REPETIR 5 VEZES POIS ELE NÃO CONSIDERA O ÚLTIMO NÚMERO
    print('Oi')

print('CONTAGEM REGRESSIVA')
for c in range(6, 0, -1):
    # O ÚLTIMO NÚMERO DO RANGE É A FORMA QUE ELE FARÁ A ITERAÇÃO
    print(c)

print('')
print('CONTAGEM DIRETA PULANDO 1')
for d in range(0, 6, 2):
    # O ÚLTIMO NÚMERO DO RANGE É A FORMA QUE ELE FARÁ A ITERAÇÃO
    print(d)

print(' ')
n = int(input('Digite um núemro: '))
for c in range(0, n+1):
    sleep(.5)
    print(c)


print('FIM')
