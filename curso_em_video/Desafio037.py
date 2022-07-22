"""
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:

1 para binário,
2 para octal
3 para hexadecimal.
"""

num = int(input('Digite o valor de um número inteiro: '))
print('Você deseja converter esse número para qual base: \n'
      ' [ 1 ] para \033[32mBINÁRIO \033[m \n'
      ' [ 2 ] para \033[34mOCATAL \033[m \n'
      ' [ 3 ] para \033[31mHEXADECIMAL \033[m')
conv = int(input(' '))

if conv == 1:
    print('O valor {} corresponde à {} em \033[32mbinário \033[m'.format(num, format(num, "b")))
elif conv == 2:
    print('O valor {} corresponde à {} em \033[34moctal \033[m'.format(num, format(num, "o")))
elif conv == 3:
    print('O valor {} corresponde à {} em \033[31mhexadecimal \033[m'.format(num, format(num, "X")))
#     SE UTILIZAR O "X" MINÚSCULO, O RESULTADO IMPRESSO SERÁ MINÚSCULO TAMBÉM
else:
    conv = int(input('Esse valor digitado não corresponde a nenhuma conversão'))
