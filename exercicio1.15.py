#Cálculo salário bruto e pagamentos a serem feitos em cima do salario

valorHora = float(input("Insira o valor da hora trabalhada em R$: "))
horasTrabalhadas = int(input("Insira a quantidade de horas total trabalhadas: "))

salario = valorHora * horasTrabalhadas
ir = salario * 0.11
inss = salario * 0.08
sind = salario * 0.05
salarioLiquido = salario - ir - inss - sind

print("Salário Bruto: R${:.2f}".format(salario))
print("Pagamento de IR: R${:.2f}".format(ir))
print("Pagamento ao INSS: R${:.2f}".format(inss))
print("Pagamento para o Sindicato: R${:.2f}".format(sind))
print("Salário Líquido: R${:.2f}".format(salarioLiquido))