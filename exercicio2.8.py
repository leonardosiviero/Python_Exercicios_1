#Escolher qual produto comprar escolhendo o mais barato.

preco1 = float(input("Preço produto 1: "))
preco2 = float(input("Preço produto 2: "))
preco3 = float(input("Preço produto 3: "))

if preco1 < preco2 and preco1 < preco3:
    menor = "primeiro produto"
elif preco2 < preco1 and preco2 < preco3:
    menor = "segundo produto"
else:
    menor = "terceiro produto"

print("Comprar o {}.".format(menor))