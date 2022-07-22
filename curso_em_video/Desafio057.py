"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = ''
while sexo != 'M' and sexo != 'F':
    print('Qual o seu sexo?\n'
          '[ M ] MASCULINO\n'
          '[ F ] FEMININO')
    sexo = str(input(' ')).upper().strip()[0]
                                        # POSSO DIGITAR MASCULNO QUE [0] PEGARÁ SOMENTE A PRIMERA LETRA DA PALAVRA
print('Obrigado!')
