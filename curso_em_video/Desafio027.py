"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""
nome = str(input('Digite seu nome completo: ')).strip().split()
ultimo = list(reversed(nome))

print('O seu primeiro nome é {} \n'
      'Seu último nome é {}' .format(nome[0].capitalize(), ultimo[0].capitalize()))
# SEGUNDA OPÇÃO

print('O seu primeiro nome é {} e o seu último nome é {}'
      .format(nome[0].capitalize(), nome[len(nome) - 1].capitalize()))
