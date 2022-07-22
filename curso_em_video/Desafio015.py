km = float(input("Quantos quilometros foram percorridos?  "))
dias = int(input("Quantos dias o carro ficou alugado?   "))
preco = 0.15 * km + 60 * dias
print("O valor que deverá ser pago é de R${:.2f}" .format(preco))
