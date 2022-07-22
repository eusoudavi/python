"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
     A) Quantos números foram digitados.
                B) A lista de valores, ordenada de forma decrescente.
                            C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    lista.append(int(input('Digite um valor inteiro:')))
    print(f'Valor {lista[-1]} adicionado na lista.')
    fim = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if fim == 'N':
        break
print('=-' * 30)
lista.sort(reverse=True)
print(f'Foram coletados {len(lista)} números. Em ordem decrescente temos: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digita e está na posição {lista.index(5)}')
else:
    print('O valor 5 não foi digitado!')
