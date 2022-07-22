a = input('Digite algo: ')
print('O tipo primitivo do que você digitou é {}' .format(type(a)))
print('O que você escreveu é um número?', a.isnumeric())
print('O que você escreveu tem apenas letras?', a.isalpha())
print('O que foi escrito é tipo alfanumérico?', a.isalnum())
print('Essa palavra está toda maiúscula?', a.isupper())
print('Essa palavra está toda minúscula?', a.islower())
print('O que você digitou está capitalizado?', a.istitle())

