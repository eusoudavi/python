"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

import random
vit = 0
print(f'{" JOGO DE PAR OU ÍMPAR ":-^50}')
while True:
    comp = random.randint(0, 5)
    jogador = int(input('Escolha um número inteiro: '))
    escolha = str(input('Escolha entre PAR [P] ou IMPAR [I]: ')).strip().upper()
    soma = comp + jogador
    while escolha not in 'PI':
        print('OPÇÃO INVÁLIDA!')
        escolha = str(input('Escolha entre PAR [P] ou IMPAR [I]: ')).strip().upper()[0]
    if soma % 2 == 0:
        if escolha == 'P':
            print(f'Você jogou {jogador} e o computador jogou {comp}. A soma é {soma} PAR!\n'
                  f'O jogador ganhou!')
            vit += 1
        else:
            print(f'Você jogou {jogador} e o computador jogou {comp}. A soma é {soma} IMPAR!\n'
                  f'O computador ganhou!')
            break
    else:
        if escolha == 'I':
            print(f'Você jogou {jogador} e o computador jogou {comp}. A soma é {soma} IMPAR!\n'
                  f'O jogador ganhou!')
            vit += 1
        else:
            print(f'Você jogou {jogador} e o computador jogou {comp}. A soma é {soma} PAR!\n'
                  f'O computador ganhou!')
            break
print(f'{" GAME OVER ":=^50}')
print(f'Você venceu {vit} vezes')
