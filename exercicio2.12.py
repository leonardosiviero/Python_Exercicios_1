#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá #pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#    Desconto do IR:
#    Salário Bruto até 900 (inclusive) - isento
#    Salário Bruto até 1500 (inclusive) - desconto de 5%
#    Salário Bruto até 2500 (inclusive) - desconto de 10%
#    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220. 

horas = float(input("Insira quantidade de horas trabalhadas: "))
valHr = float(input("Insira o valor da hora trabalhada: "))

salBruto = horas * valHr

if salBruto<= 900:
    ir = 0
elif salBruto <= 1500:
    ir = salBruto * 0.05
elif salBruto <= 2500:
    ir = salBruto * 0.10
else:
    ir = salBruto * 0.2

inss = salBruto * 0.1
fgts = salBruto * 0.11
descontos = ir + inss
salLiq = salBruto - descontos

print("Salário Bruto      : R${:.2f}".format(salBruto))
print("(-) IR (5%)        : R${:.2f}".format(ir))
print("(-) INSS (10%)     : R${:.2f}".format(inss))
print("FGTS (11%)         : R${:.2f}".format(fgts))
print("Total de descontos : R${:.2f}".format(descontos))
print("Salário Líquido    : R${:.2f}".format(salLiq))