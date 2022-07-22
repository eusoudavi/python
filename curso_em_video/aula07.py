n1 = int(input('Digite um valor: '))
n2 = int(input("Digite um segundo valor: "))

s = n1 + n2
p = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2

# Podemos utilizar {:3.f} para definir que o resultado que será aplicado tenha uma limitação de 3 casas decimais float.

# A quebra de linha no mesmo print pode ser feita com \n >>> se houver espaço entre o \n, o programa aplicará esse
# espaço no resultado.

# Caso não se queira fazer a quebra de linha entre 2 print, pode-se utilizar no final do primeiro print o comando end=' '

print('A soma dos valores é {},\no produto é {},\na divisão é {:.3f},'
      '\na divisão inteira é {}, o resto da divisão é {} '
      '\n e a exponenciação entre do primeiro com o segundo é {}' .format(s, p, d, di, r, e), end=' ... ')
print('Obrigado pela participação.')