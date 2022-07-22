print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(),
upper(), lower(), capitalize(), title(), strip(), junção com join().""")

# ACIMA TEMOS UM MÉTODO DE ESCREVER UM TEXTO GRANDE

frase = 'Curso em Video Python'

print('FATIAMENTO \n')

print(frase[9])         # ESTOU ESCREVENDO O NONO ELEMENTO DA STRING
print(frase[9:14])      # ESTOU ESCREVENDO DO NONO ELEMENTO AO 13
print(frase[9:21:2])    # ESCREVENDO AS LETRAS DE 9 A 20 PULANDO 1
print(frase[:5])        # É IGUAL A ESCREVER print(frase[0:5])
print(frase[15:])       # É O MESMO PROCESSO ANTERIOR, SÓ QUE ESCREVENDO ATÉ O ÚLTIMO ÍNTEM DA STRING
print(frase[9::3])      # ESCREVENDO AS LETRAS DE 9 ATÉ O FINAL PULANDO 2

print('---' * 10)
print('ANÁLISE\n')

print(len(frase))               # MOSTRA O COMPRIMENTO DA STRING
print(frase.count('o'))         # O PROGRAMA FARÁ UMA CONTAGEM DA LETRA o
print(frase.count('o', 0, 13))  # O PROGRAMA CONTARÁ A LETRA o A PARTIR DO PRIMEIRO CARCTERE ATÉ O 12
print(frase.find('deo'))        # O PROGRAMA INFORMARÁ QUAL A POSIÇÃO DA STRING COMEÇA A SEQUENCIA DE LETRAS deo
# SE NÃO HOUVER A PALAVRA PROCURADA, A RESPOSTA É -1
print('Curso' in frase)         # O PROGRAMA INFORMARÁ SE HÁ A PALAVRA DENTRO DA STRING

print('---' * 10)
print('TRASNFORMAÇÃO\n')

nova_frase = frase.replace("Python", "Android")
print(nova_frase)               # O PROGRAMA SUBSTITUIU UMA PALAVRA DA STRING frase E CRIOU UMA NOVA STRING
print(frase.upper())            # O PROGRAMA VAI DEIXAR TÚDO MAIÚSCULO
print(frase.lower())            # O PROGRAMA VAI DEIXAR TUDO MINÚSCULO
print(frase.capitalize())       # O PROGRAMA VAI DEIXAR APENAS A PRIMEIRA LETRA DA STRING EM MAIÚSCULA
print(frase.title())            # VAI DEIXAR A PRIMEIRA LETRA DE TODAS AS PALAVRAS EM MAIÚSCULA
print('\n')

frase = '   Aprenda Python  '
print(frase)
print(frase.strip())            # REMOVE OS ESPAÇOS DESNECESSÁRIOS NO COMEÇO E FINAL DA STRING
print(frase.rstrip())           # REMOVE OS CARACTERES APENAS NA DIREITA (RIGHT)
print(frase.lstrip())           # REMOVE OS CARACTERES APENAS NA ESQUERDA (LEFT)

print('---' * 10)
print('DIVISÃO\n')

frase = 'Curso em Video Python'
frase = frase.split()           # DIVIDE A STRING EM UMA LISTA
print(frase)
print(frase[0])
print(frase[0][0])

print('---' * 10)
print('JUNÇÃO\n')

frase = '-'.join(frase)         # REUNE UMA LISTA NUMA STRING USANDO - COMO SEPARADOR
print(frase)
