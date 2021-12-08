#Loja de tintas 1

import math

area = float(input("Insira a área que será aplicada a tinta: "))
litros = (area / 6 * 1.1)
litroPcima = math.ceil(litros)
print("Deverá comprar {} litros de tinta".format(litroPcima))
qtdLatas = math.ceil(litroPcima/18)
print("Comprar {} latas de 18 litros.".format(qtdLatas), "Total: R$", float(qtdLatas * 80))
qtdGaloes = math.ceil(litros/3.6)
print("Comprar {} galões de 3.6 litros.".format(qtdGaloes), "Total: R$", float(qtdGaloes * 25))
latas = math.floor(litros / 18)
galoes = math.ceil((((litros/18) - (math.floor(litros/18))) * 18 ) /3.6)
print("Comprar", latas, "latas de 18 litros e", galoes, "galões de 3.6 litros.", "Total: R$", float(qtdGaloes * 25 + qtdLatas * 80))