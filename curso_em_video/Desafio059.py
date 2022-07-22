"""
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

a = int(input('Digite um valor inteiro: '))
b = int(input('Digite um segundo valor inteiro: '))

print('Selecione uma das seguintes opções a seguir para trabalhar com esses números:\n'
      '[ 1 ] SOMAR\n'
      '[ 2 ] MULTIPLICAR\n'
      '[ 3 ] MAIOR\n'
      '[ 4 ] NOVOS NÚMEROS\n'
      '[ 5 ] SAIR DO PROGRAMA')
opção_valida = False
while opção_valida == False:
    menu = int(input('Qual opção do MENU deseja: '))
    if menu == 1:
        print('\nA soma de {} com {} é {}' .format(a, b, a + b))
        # opção_valida = True
    elif menu == 2:
        print('\nO produto de {} com {} é {}' .format(a, b, a * b))
        # opção_valida = True
    elif menu == 3:
        if a > b:
            print('\nO valor {} é maior que {}' .format(a, b))
        elif a < b:
            print('\nO valor {} é maior que {}' .format(b, a))
        else:
            print('\nOs valores são iguais!')
        # opção_valida = True
    elif menu == 4:
        print('Digite novamente os valores:')
        a = int(input('Primeiro: '))
        b = int(input('Segundo: '))
    elif menu == 5:
        print('Obrigado')
        opção_valida = True
    else:
        print('\033[31mDigite uma opção válida do MENU.\033[m\n')

