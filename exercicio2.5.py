#Programar para verificar se aluno esta aprovado para passar de ano

nota1 = float(input("Nota 1° bimestre: "))
nota2 = float(input("Nota 2° bimestre: "))
nota3 = float(input("Nota 3° bimestre: "))
nota4 = float(input("Nota 4° bimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media == 10:
    print("Aprovado com distinção")
elif media >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")