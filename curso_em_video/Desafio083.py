"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
ex = list()
inicio = fim = ok = 0
ex = str(input('Digite uma expresão que contenha parênteses: '))
print(ex)
if '(' or ')' in ex:
    for pos, letras in enumerate(ex):
        if '(' in letras:
            # print(f'Primeiro parênteses na posição {pos}')
            inicio = pos
            ok += 1
        if ')' in letras:
            # print(f'O fechamento está na posição {pos}')
            fim = pos
            ok -= 1
    if inicio < fim and ok == 0:
        print('Os parênteses foram colocados de maneira certa!')
    else:
        print('Houve algum erro de digitação!')
else:
    print('A frase que você digitou não contêm parênteses!')
