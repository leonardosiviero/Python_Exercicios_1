#Cálculo de multa por excesso de peso do pescado

pesoPeixe = float(input("Insira o peso do peixe em kg: "))

if pesoPeixe > 50.0:
    excesso = pesoPeixe - 50
    multa = excesso * 4
    print("A multa para o peso excedente a 50.0 kg é: R${:.2f}".format(multa))
else:
    print("O peixe não possui mais de 50.0 kg, portanto não há multa.")