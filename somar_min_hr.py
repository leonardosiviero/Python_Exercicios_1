hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
minutos = 0
total = mins + dura
sobra = total / 60 
sobra_int = int(sobra) #hora para ser somada
sobra_decimal = sobra - sobra_int
minutos = round(sobra_decimal * 60) #minutos a serem somados
hour = hour + sobra_int
hora = hour % 24
print(hora, ":", minutos)


