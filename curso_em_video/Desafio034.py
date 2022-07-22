"""
 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
sal = float(input('Qual o salário do funcionário? '))

if sal > 1250:
    aum = sal * 1.1
    print('O salário de R${} soferá um aumento de 10%, passando para R${:.2f}' .format(sal, aum))
else:
    aum = sal * 1.15
    print('O salário de R${} sofrerá um aumento de 15%, passando para R${:.2f}' .format(sal, aum))
