#Tempo para download

download = float(input("Tamanho do arquivo em MB: "))
velLink = float(input("Velocidade do site em Mbps: "))
tempo = download / velLink

print("Tempo para efetuar o download: {} segundos.".format(tempo))