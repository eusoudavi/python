n = int(input('Escreva um númeor inteiro: '))
# ant = n - 1
# su = n + 1

# print('O número que você digitou foi {}.'
#      '\nO antecessor desse número é o {}.'
#      '\nO sucessor desse número é {}' .format(n, ant, su))

# CÓDIGO OTIMIZADO COM MENOS VARIÁVEIS:

print("O número que você digitou foi {}."
      "\nO antecessor desse número é: {}"
      "\nO sucessor desse número é: {}" .format(n, (n-1), (n+1)))
