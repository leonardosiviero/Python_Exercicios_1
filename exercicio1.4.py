#Cálculo da média anual a partir da nota dos bimetres

num1 = float(input("Insira nota primeiro bimestre: "))
num2 = float(input("Insira nota segundo bimestre: "))
num3 = float(input("Insira nota terceiro bimestre: "))
num4 = float(input("Insira nota quarto bimestre: "))

media = (num1 + num2 + num3 + num4) / 4

print("A média das notas foram: {:.2f}.".format(media))