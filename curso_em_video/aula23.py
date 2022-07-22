"""
Tratamento de Erros e Exceções
"""
try:
    a = int(input('NUMERADOR: '))
    b = int(input('DENOMINADOR: '))
    r = a / b
    # AQUI O PROGRAMA IRÁ TENTAR EXECUTAR UMA TAREFA
except ZeroDivisionError:
    # POSSO CRIAR SITUAÇÕES DIFERENTES CONFORME O ERRO APRESENTADO
    print('NÃO É POSSÍVEL DIVIDIR UM NÚMERO POR ZERO')
except Exception as erro:
    # COMANDO OBRIGATÓRIO PARA INFORMAR O QUE ELE DEVE RESPONDER CASO NÃO CONSIGA EXECUTAR A TAREFA
    print('Os números digitados não podem ser divididos!')
    print(f'Posso mostrar qual é o erro assim: {erro.__class__}')
else:
    # COMANDO OPCIONAL PARA INFORMAR O QUE ELE IRÁ RESPONDER CASO CONISGA EXECUTAR O COMANDO PRINCIPAL
    print(f'O resultado da divisão de {a} por {b} é {r:.2f}')
finally:
    # COMANDO OPCIONAL PARA INFORMAR O QUE ELE DEVE FAZER APÓS A TENTATIVA
    print('Obrigado, volte sempre!')
