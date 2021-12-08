#Cálculo da área de um quadro e mostrar o dobro da área pro usuario

lado = float(input("Insira a dimensão do lado do quadrado: "))

area = lado ** 2
areaDobro = area * 2

print("\n O dobro da área do quadrado é {:.2f}.\n".format(areaDobro))