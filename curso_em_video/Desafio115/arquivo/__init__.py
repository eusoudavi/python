from time import sleep
from Desafio115.interface import Op3


def TesteArq(nome):
    try:
        teste = open(nome, 'r')  # IRÁ LER UM ARQUIVO CONFORME O NOME DA FUNÇÃO
        teste.close()            # VAI FECHAR O ARQUIVO
    except (FileNotFoundError, FileExistsError):
        teste = open(nome, 'wt')
        teste.close()
        print(f'Criando o arquivo {nome}')
        sleep(1)
        print(f'Arquivo Criado!')


def EscreverArq(arq):
    try:
        cadastro = open(arq, 'a')
        cadastro.close()
    except FileNotFoundError:
        print('ARQUIVO NÃO ENCONTRADO')
        TesteArq(arq)
    else:
        cadastro = open(arq, 'a')
        cadastro.write(str(input('NOME: ')).strip().capitalize())
        cadastro.write(';')
        cadastro.write(str(input('IDADE: ')).strip())
        cadastro.write('\n')
        cadastro.close()


def LerArq(arq):
    try:
        leit = open(arq, 'rt')
        for linhas in leit:
            dado = linhas.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:.<30}{dado[1]:.>25} anos')
        # print(leit.read())
        leit.close()
        sleep(3)
    except FileNotFoundError:
        Op3('\033[31mERRO CRÍTICO\033[m')
        sleep(2)
