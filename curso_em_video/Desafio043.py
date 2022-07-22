"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""
peso = float(input('Qual o seu peso? [Kg] '))
altura = float(input('Qual a sua altura? [m] '))

imc = peso / altura ** 2

if imc < 18.5:
    print('Seu IMC é de {:.2f}. Você está abaixo do peso!' .format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.2f}. Você está no peso ideal!' .format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.2f}. Você está com sobrepeso, cuidado!' .format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.2f}. Você está com sobrepeso! FAÇA UMA DIETA E EXERCÍCIOS LOGO!' .format(imc))
else:
    print('Seu IMC é de {:.2f}. Você está com Obesidade Mórbida. PROCURE UM MÉDICO!' .format(imc))
