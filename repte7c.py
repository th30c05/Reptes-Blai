numero=int(input("Posa un numero positiu i jo et dire els numeors inparells que hi han entre el teu numero i el 1: "))
asterisc="*"

if numero>=1:
    for i in range(1,numero):
        if i%2!=0:
            print(i*asterisc)
else:
    print("Nomes es permeten numeros positius")