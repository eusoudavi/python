nome = str(input('Qual o seu nome? ')).strip().lower()
if nome == "davi":
    print('Seu nome é muito bonito!')
elif nome == 'karina':
    print('Seu nome fica muito bonito com o sobrenome \033[0;34m Visintainer \033[m')
else:
    print('Seu nome é normal!')

print('Bom dia, {}!' .format(nome.capitalize()))
