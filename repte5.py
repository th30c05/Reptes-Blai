def redondea(a, b):
  return int((a / 5 + 0.5)) * b

def reglade3(a, b, c):
    return int((c*b)/a)

personas=int(input("Numero de convidats: "))

if personas>=0:
    
    personasredondeadas=redondea((personas+3), 5)
    recetapara=5
    iogurt=reglade3(recetapara, 1, personasredondeadas)
    ous=reglade3(recetapara, 3, personasredondeadas)
    farina=reglade3(recetapara, 250, personasredondeadas)
    cacao=reglade3(recetapara, 125, personasredondeadas)
    sucre=reglade3(recetapara, 250, personasredondeadas)
    oli=reglade3(recetapara, 125, personasredondeadas)
    paquetllevat=reglade3(recetapara, 1, personasredondeadas)

    print("Nesesitarem:")
    if iogurt==1:#iogurt
        print("- "+str(iogurt)+" iogurt natural.")
    else:
        print("- "+str(iogurt)+" iogurts naturals.")

    print("- "+str(ous)+" ous.")#ous
    if farina ==1000:#farina
        print("- "+str(int(farina/1000))+"Kg de farina.")
    elif farina>1000:
        print("- "+str(farina/1000)+"Kg de farina.")
    else:
        print("- "+str(farina)+"gr de farina.")

    if cacao ==1000:#cacao
        print("- "+str(int(cacao/1000))+"Kg de cacao.")
    elif cacao>1000:
        print("- "+str(cacao/1000)+"Kg de cacao.")
    else:
        print("- "+str(cacao)+"gr de cacao.")

    if  sucre==1000:#sucre
        print("- "+str(int(sucre/1000))+"Kg de sucre.")
    elif sucre>1000:
        print("- "+str(sucre/1000)+"Kg de sucre.")
    else:
        print("- "+str(sucre)+"gr de sucre.")

    if oli ==1000:#oli
        print("- "+str(int(oli/1000))+"L d'oli.")
    elif oli>1000:
        print("- "+str(oli/1000)+"L d'oli.")
    else:
        print("- "+str(oli)+"ml d'oli.")

    if paquetllevat==1:#Paquet/s de llevat
        print("- "+str(paquetllevat)+" paquet de llevat.")
    else:
        print("- "+str(paquetllevat)+" paquets de llevat.")
    print(" ")
    print("Per a "+str(personasredondeadas)+" personas")  
else:  
    print("Numero incorrecte; No es imposible tenir convidats negatius.")


