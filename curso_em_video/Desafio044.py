"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""
print('{:-^50}' .format(' EXERCÍCIO 43 '))
normal = float(input('Qual o preço normal do produto? '))
print('TEMOS AS SEGUINTES CONDIÇÕES DE PAGAMENTO:\n'
      '[ 0 ] - À VISTA (DINHEIRO) COM 10% DE DESCONTO\n'
      '[ 1 ] - CARTÃO COM 5% DE DESCONTO\n'
      '[ 2 ] - CRÉDITO EM 2X\n'
      '[ 3 ] - CRÉDITO EM 3X OU MAIS - JUROS DE 20%\n')

cond = int(input('Qual a condição de pagamento? '))
print(' ')

if cond == 0:
    print('Você vai pagar R${:.2f}.' .format(0.9 * normal))
elif cond == 1:
    print('Você vai pagar R${:.2f}.'.format(0.95 * normal))
elif cond == 2:
    print('Você vai pagar R${:.2f}.'.format(normal))
    print('Cada parcela sairá por R${:.2f}' .format(normal/2))
elif cond == 3:
    parcelas = int(input('Em quantas parcelas você vai dividir? '))
    if parcelas < 3:
        print('A opção indicada é de no mínimo 3 parcelas. Assim, temos:')
        parcelas = 3
    print('Você vai pagar R${:.2f}.'.format(1.2 * normal))
    print('Dividindo em {} parcelas, o valor de cada parcela será de R${:.2f}'
          .format(parcelas, (1.2 * normal)/parcelas))
else:
    print('\033[31mO VALOR INSERIDO NÃO CORRESPONDE A NENHUMA ALTERNATIVA ACIMA! \033[m')
