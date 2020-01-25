numero=int(input("Posa un numero positiu i jo et dire els numeors parells que hi han entre el teu numero i el 1: "))

if numero>=1:
    print( [i for i in range(1, numero) if i%2!=1] )
else:
     print("Nomes es permeten numeros positius")
