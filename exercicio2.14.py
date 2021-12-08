#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 

nota1 = float(input("Inserir nota da primeira prova: "))
nota2 = float(input("Inserir nota da segunda prova: "))
media = (nota1 + nota2) / 2

if media >= 0 and media < 4.0:
    conceito = "E"
    sitAluno = "REPROVADO"
elif media >= 4.0 and media < 6.0:
    conceito = "D"
    sitAluno = "REPROVADO"
elif media >= 6.0 and media < 7.5:
    conceito = "C"
    sitAluno = "APROVADO"
elif media >= 7.5 and media < 9.0:
    conceito = "B"    
    sitAluno = "APROVADO"
else:
    conceito = "A"    
    sitAluno = "APROVADO"

print("Média do aluno nas duas avaliações: {:.1f}\n".format(media))
print("Média de Aproveitamento  Conceito")
print("Entre 9.0 e 10.0            A    ")
print("Entre 7.5 e 9.0             B    ")
print("Entre 6.0 e 7.5             C    ")
print("Entre 4.0 e 6.0             D    ")
print("Entre 4.0 e zero            E    \n")
print("Conceito final   : {}".format(conceito))
print("Situação do aluno: {}".format(sitAluno))