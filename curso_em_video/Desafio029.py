"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
from time import sleep

vel = float(input('Qual a velocidade do carro? '))
multa = (vel - 80) * 7

print(' ')
sleep(1)

if vel > 80:
    print('\033[0;30;41mA velocidade de {}Km/h é maior que 80Km/h.\033[m \n'
          'VOCÊ FOI MULTADO EM \033[1;31m R${:.2f}' .format(vel, multa))
else:
    print('\033[0;42m Parabéns, continue abaixo de 80Km/h. \033[m')
