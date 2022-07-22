import requests
# https://docs.python-requests.org/en/latest/

site = 'http://httpbin.org/basic-auth/user/passwd'
# 'http://httpbin.org/basic-auth/user/passwd'
# USUÁRIO - user
# SENHA - passwd

try:
    resposta = requests.get(site)
    # O COMANDO request VAI RESPONDER CONFORME OS COD DE RETORNO HTTP DA API
except:
    print('Não é possível acessar a página Web.')
else:
    if resposta.status_code == 200:  # CÓDIGO PARA INFORMAR QUE O SITE ESTÁ DISPONÍVEL
        print('O site está disponível')
    elif resposta.status_code == 404:  # CÓDIGO INFORMANDO QUE O SITE NÃO FOI ENCONTRADO NO SERVIDOR
        print('Erro 404 - O site está fora do ar')
    elif resposta.status_code == 401:  # CÓDIGO INFORMANDO QUE O SITE TEM UMA INTERFACE PARA ACESSO DE USUÁRIO
        print('É necessário fazer autenficação para entrar no site')
        acesso = str(input('Deseja informar usuário e senha manualmente [M]'
                           ' ou usar o método automático [A]: ')).strip().upper()[0]
        if acesso == "A":
            login = requests.get(site, auth=('user', 'passwd'))
            if login.status_code == 200:
                print('O site está disponível')
            else:
                print('Erro ao acesar o site!')
        elif acesso == "M":
            U = str(input('USUÁRIO: '))
            S = str(input('SENHA: '))
            login = requests.get(site, auth=(U, S))
            if login.status_code == 200:
                print('O site está disponível')
            else:
                print('Erro ao acesar o site!')
