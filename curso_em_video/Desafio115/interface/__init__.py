from time import sleep

def cab(txt):
    print('=' * 60)
    print(f'\033[7m {txt:^60}\033[m')
    print('=' * 60)



def iniciar(menu, txt=''):
    cab('MENU PRINCIPAL')
    for pos, itens in enumerate(menu):
        print(f'{pos + 1} - {itens}')
    print('=' * 60)
    while True:
        try:
            a = int(input(txt))
        except (ValueError, TypeError):
            print(f'\033[31mValor inválido\033[m')
            continue
        except KeyboardInterrupt:
            print('Programa encerrado de forma inesperada!')
        else:
            if a > len(menu):
                print('\033[33mDigite um número válido do menu!\033[m')
            else:
                return a



def Op1(txt='OP_01'):
    cab(txt)
    sleep(.4)
    return True


def Op2(txt='OP_02'):
    cab(txt)
    sleep(.4)
    return True


def Op3(txt='OP_03'):
    cab(txt)
    sleep(.1)
    print(f'\033[35m {"ENCERRANDO O SISTEMA!":^60}\033[m')
    sleep(1.2)
    print(f'\033[35m {"ATÉ MAIS":^60}\033[m')
    return False
