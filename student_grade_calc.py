nom_etudiant = str(input("enter votre nom : "))
prenom_etudiant = str(input("enter votre prenom : "))
note_tp = float(input("entrer votre note du tp : "))
note_devoir = float(input("entrer votre note du devoir : "))
note_exam = float(input("entrer votre note du exam : "))
moyen = (note_tp * 0.20) + (note_devoir * 0.30) + (note_exam * 0.50)
print(moyen)
if moyen >= 12 :
    print("etudiant admis")
elif 5 <= moyen < 12 :
     print("etudiant ajourne")
else :
     print("etudiant exclus")
