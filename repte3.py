generacio=int(input("Generació de processadors: "))
memoraia=int(input("Memòria de la targeta gràfica: "))
memoria_lliure=int(input("Memòria d’emmagatzematge lliure: "))

if generacio<=5 and memoraia<=2 and memoria_lliure<=50:
  print("Podeu executar el joc.")
else:
  print("NO podeu executar el joc.")