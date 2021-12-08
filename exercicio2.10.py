#Código para obter o turno em que estuda

turno = input("Qual o turno em que estuda (M/V/N): ")
turno = turno.upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")