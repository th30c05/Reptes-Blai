numero=int(input("Qualifica la pelicula del 0 al 100: "))

if numero==0:
    print("-")
elif numero>0 and numero<=100:
    print("*"*numero)
else:
    print("Numero incorrecte, recorda que ha de ser del 0 al 100 ambdos inclosos")