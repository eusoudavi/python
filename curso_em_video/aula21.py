"""
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
escopo de variáveis e retorno de resultados.
* Interactive Help -> help()
* docstrings -> manual
* Argumentos opcionais
* Escopo de Variáveis
* Retorno de resultados
"""
# INTERACTIVE HELP
help(print())
print('=' * 30)
print(input.__doc__)
print('=' * 30)


# DOCSTRINGS
def contador(i, f, p):
    """
    AO COLOCAR 3X ASPAS DUPLAS, ABRIMOS UMA DOCSTRING DESSA FUNÇÃO QUE IRÁ EXPLICAR COMO ESSA FUNÇÃO TRABALHA:
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')


help(contador)


# PARÂMETROS OPCIONAIS
def somar(a, b, c=0):
    s = a + b + c
    print(f' A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)  # COMO FOI COLOCADO NA DEFINIÇÃO DA FUNÇÃO c = 0, SE NÃO COLOCARMOS UM VALOR PARA O C AO CHAMAR A
# FUNÇÃO, O PROJETO FUNCIONARÁ DE QUALQUER MANEIRA.


# ESCOPO DE VARIÁVEIS
def teste():
    global x   # ESSE COMANDO TORNAL A VARIÁVEL GLOBAL PARA QUE APAREÇA NO PROGRAMA PRINCIPAL
    x = 8  # AS VARIÁVEIS ATRIBUÍDAS NAS FUNÇÕES PRECISAM SER INDICADAS QUE VALEM NO PROGRAMA PRINCIPAL (VARIÁVEL LOCAL)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa principal
n = 2   # AS VARIÁVEIS ATRIBUÍDAS NO PROGRAMA PRINCIPAL, VALEM NAS FUNÇÕES (VARIÁVEL GLOBAL)
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa pricipal, x vale {x}')
print('=-' * 30)


# RETORNO DE RESULTADOS
def somar(a, b, c=0):
    s = a + b + c
    return s   # DEFINO ASSIM QUAL É O RESULTADO DA FUNÇÃO, QUANDO CHAMADO NO PROGRAMA PRINCIPAL


print(somar(3, 2, 5))
print(somar(8, 4) )
