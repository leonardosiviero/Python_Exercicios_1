keyword = "chupacabra"
sortword = str(input("Enter any word and try to scape the loop: "))

while sortword != keyword:
    print("You´re in the loop!")
    sortword = str(input("Enter any word and try to scape the loop: "))
    if sortword == keyword:
        break
    
print("You've successfully left the loop.")
    