#Altere o programa anterior permitindo ao usuário informar as populações e
# as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

def populacao():

    popA = int(input("Qual o tamanho da população A: "))
    popB = int(input("Qual o tamanho da população B: "))
    txA = float(input("Qual a taxa de cresimento (%): "))
    txB = float(input("Qual a taxa de cresimento (%): "))
    taxaA = (txA / 100) + 1
    taxaB = (txB / 100) + 1


    while popA < popB:
        popA = int(round(popA * taxaA, 0))
        popB = int(round(popB * taxaB, 0))

    print("População A possui {} habitantes, enquanto População B "
              "possui um número inferior com total de {} habitante."
              .format(popA, popB))

if (__name__ == "__main__"):
    populacao()