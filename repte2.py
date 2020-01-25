paquets=int(input("Nombre de paquets de llimona: "))

if paquets<=0:
  resultat="Numero incorrecte."
else: 
  gerres=paquets/6
  resultat=("Podras fer "+str(gerres)+" gerres amb "+str(paquets)+" paquets de llimona.")
  
print(resultat)
