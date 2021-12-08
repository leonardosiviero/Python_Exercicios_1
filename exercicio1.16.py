#Loja de tintas 1

import math

area = float(input("Insira a área que será aplicada a tinta: "))
litros = (area / 3)
litroPcima = math.ceil(litros)
print("Deverá comprar {} litros de tinta".format(litroPcima))
qtdLatas = math.ceil(litroPcima/18)
print("Comprar {} latas de 18 litros.".format(qtdLatas), "Total: R$", float(qtdLatas * 80))
