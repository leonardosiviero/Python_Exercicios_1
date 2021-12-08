#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
#taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
#com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
#número de anos necessários para que a população do país A ultrapasse ou iguale
#a população do país B, mantidas as taxas de crescimento. 

def populacao():

    popA = 80000
    popB = 200000
    txA = 1.03
    txB = 1.015

    while popA < popB:
        popA *= txA
        popB *= txB

    print("PopA = {}".format(popA))
    print("PopB = {}".format(popB))

if (__name__ == "__main__"):
    populacao()
