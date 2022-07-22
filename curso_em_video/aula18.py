"""
LISTA DENTRO DE LISTAS
"""
d1 = ['Pedro', 25]
d2 = ['Maria', 19]
d3 = ['João', 32]
pessoas = list()
pessoas.append(d1[:])  # OS : SERVEM PARA COPIARMOS A LISTA, CASO CONTRÁRIO, VAI ESTÁ VINCULADO
pessoas.append(d2[:])
pessoas.append(d3[:])
print(pessoas)
print('==' * 30)

# SE NÃO COLOCAR OS :, FICA ASSIM:
teste = list()
galera = list()
teste = ['Pedro', 25]
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 10
galera.append(teste)
print(galera)
print('==' * 30)

# DECLARAÇÃO TODA DE UMA VEZ
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32], ['Ana', 10]]
print(pessoas)
print(pessoas[0][0])  # O PRIMEIRO ÍNDICE É REFERENTE A MAIOR LISTA
print(pessoas[1])
print(pessoas[2][1])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')
