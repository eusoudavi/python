"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

price = float(input('Digite o valor da casa: R$'))
money = float(input('Qual o seu salário: R$'))
years = int(input('Em quantos anos você pretende parcelar a compra da casa? '))

m = price/(years * 12)

if m < 0.3 * money:
    print('O valor da prestação é R${:.2f}.' .format(m))
    print('Emprestimo \033[32mLIBERADO \033[m')
elif m >= 0.3 * money:
    print('O valor das parcelas será de R${:.2f} e será maior que 30% do seu salário de R${}.' .format(m, money))
    print('Empréstimo \033[31mNEGADO \033[m')

