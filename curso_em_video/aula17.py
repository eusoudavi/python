"""
LISTAS []
"""
lista = ['hamburgues', 'suco', 'pizza', 'pudim']
# LISTAS SÃO MUTÁVEIS
lista[3] = 'picolé'
# PODEMOS ACRESCENTAR NOVOS ITENS NAS LISTAS
lista.append('biscoito')
# PODMEOS INSERIR QUALQUER OBJETO NA LISTA EM QUALQUER POSIÇÃO
lista.insert(0, 'cachorro-quente')
print(lista)
# PODEMOS DELETAR ÍTENS DA LISTA
del lista[3]
print(lista)
lista.pop(3)  # ESSE COMANDO NORMALMENTE É UTILIZADO PARA APAGAR O ÚLTIMO ELEMENTO DA LISTA
print(lista)
lista.remove('suco')  # ESSE COMANDO É PARA INDICARMOS QUAL O OBJETO AO INVÉS DO ÍNDICE
print(lista)
#
# valores = list(range(4, 11, 2))
# print(valores)
valores = [8, 2, 4, 7, 1, 0, 9]
print(valores)
valores.sort(reverse=True)
print(valores)
print(len(valores))

a = [2, 3, 4, 7]
b = a  # O PYTHON LIGA UMA LISTA NA OUTRA
c = a[:]  # O PYTHON COPIOU A LISTA A EM C
b[2] = 3
print(a)
print(b)
print(c)
print(max(c))
print(a)
a.insert(1,50)
print(a)

num = [3, 6, 4, 1]
for n1, n2 in enumerate(num):
    print(n1 + n2)
val = list(range(1, 5))
print(val)
