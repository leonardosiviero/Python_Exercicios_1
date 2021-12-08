#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#
#   Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento. 

sal1 = float(input('Insira salário atual: '))
sal2 = sal1
reaj1 = 0.20
reaj2 = 0.15
reaj3 = 0.10
reaj4 = 0.05

if sal2 <= 280:
    sal2 = sal2 + sal2 * reaj1
elif sal2 > 280 and sal2 <= 700:
    sal2 = sal2 + sal2 * reaj2
elif sal2 > 700 and sal2 <= 1500:
    sal2 = sal2 + sal2 * reaj3
else:
    sal2 = sal2 + sal2 * reaj4

reajuste = (sal2 / sal1 * 100) - 100
aumento = sal2 - sal1

print("Salário antes do reajuste: R${:.2f}".format(sal1))
print("Percentual de aumento aplicado: {:.2f}%".format(reajuste))
print("Valor do aumento: R${:.2f}".format(aumento))
print("Novo salário, após o aumento: R${:.2f}".format(sal2))