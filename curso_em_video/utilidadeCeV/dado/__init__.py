from utilidadeCeV import moeda

def leiaDinheiro(txt=''):
    entrada = str(input(txt)).strip().replace(',', '.')
    while True:
        if entrada.isalpha():
            try:
                num = float(entrada)
            except:
                print('O valor digitado não é válido!')
                entrada = str(input('Digite um valor válido!')).strip().replace(',', '.')
            else:
                break
        else:
            escrever = entrada.replace('.', ',')
            num = float(entrada)
            break

    print(f'Você digitou o valor R$ {escrever}')
    moeda.resumo(num)
