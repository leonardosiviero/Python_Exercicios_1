int1 = int(input("Insira um número inteiro: "))
int2 = int(input("Insira outro número inteiro: "))
real1= int(input("Insira um número real: "))


respA = (2 * int1) * (int2 / 2)
respB = (int1 * 3) + real1
respC = real1 ** 3

print("O produto do dobro do primeiro com metade do segundo: {}.".format(respA))
print("A soma do triplo do primeiro com o terceiro: {}.".format(respB))
print("O terceiro elevado ao cubo: {}.".format(respC))