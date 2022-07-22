"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
cont = soma = 0
funcionando = True
while funcionando is True:
    n = int(input('Digite um número inteiro: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    continuar = str(input('Você deseja continuar [S/N]: ')).upper()
    # print(continuar)
    if continuar != 'S' and continuar != 'N':
        print('Você digitou um comando inválido!')
        while continuar not in 'SN':
            continuar = str(input('Você deseja continuar [S/N]: ')).strip().upper()
    if continuar == 'N':
        funcionando = False
med = soma/cont
print('=-=' *50)
print('Você digitou {} números e a soma deles é {}\n'
      'A média desses números é {:.2f}'. format(cont, soma, med))
print('O maior número digitado foi {} e o menor foi {}' .format(maior, menor))
