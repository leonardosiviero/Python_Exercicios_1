#Cálculo salário bruto profissional CNPJ

valorHora = float(input("Insira o valor da hora trabalhada em R$: "))
horasTrabalhadas = int(input("Insira a quantidade de horas total trabalhadas: "))

salario = valorHora * horasTrabalhadas

print("Salário: R${:.2f}".format(salario))