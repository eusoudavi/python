"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
mercado = ('Arroz', 9.85, 'Feijão', 5.47, 'Farinha', 3.50, 'Macarrão', 2.75, 'Batata', 4.37, 'Tomate', 8.12)
print('No nosso mercado temos os seguintes produtos:')
for posição, produto in enumerate(mercado):
    if posição % 2 == 0:
        print(f'O {produto:.<15}custa ', end='')
    else:
        print(f'R$ {produto:>5.2f}')
