"""
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.

"""


nome = str(input('Digite o seu nome completo: ')).strip()
nome = nome.upper()

lista = nome.split()
s_esp = ''.join(lista)
letras = len(s_esp)
# OUTRA OPÇÃO É CONTAR O NOME NORMALMENTE E SUBTRATIR OS ESPAÇOS INTERNOS COM O COMANDO len(nome) - nome.count('')

prim = (lista[0]).lower().capitalize()

print('Obrigado {} por participar desse teste.'
      '\nSeu nome tem {} letras e o primeiro nome é {} e tem {} letras.' .format(nome, letras, prim, len(prim)))
