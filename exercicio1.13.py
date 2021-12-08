#Cálculo do peso ideal

altura = float(input("Insira a altura da pessoa em metros: "))

homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7

print("Peso ideal para homem com esta altura: {:.1f}kg.".format(homem))
print("Peso ideal para mulher com esta altura: {:.1f}kg.".format(mulher))