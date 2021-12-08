#Conversor de temperatura

fahrenheit = float(input("Insira a temperatura em fahrenheit: "))
celsius = 5 * ((fahrenheit-32)/9)

print("A conversão da temperatura é {:.2f}°C.".format(celsius))