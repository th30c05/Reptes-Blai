stop=False
errors=0

while stop==False:
    
    passw="contrasenya"
    pasw=input("Introdueix la contrasenya per continuar: ")
    
    if passw==pasw:
        print("Contrasenya correcte. Benvingut")
        stop=True
    else:
        errors=errors+1
        if errors>1 and errors<15:
            print("Contrasenya incorrecte torna-ho a provar. (Portes "+str(errors)+" errors)")
        elif errors>=15:
            print("Maxim d errors permesos prova-ho mes tard. (Errors: "+str(errors)+")")
            stop=True
        else:
            print("Contrasenya incorrecte torna-ho a provar. (Portes "+str(errors)+" error)")