CestQuandMes60 = lambda age : 60 - age

prenom = input("Quel est votre prénom ?")
nom = input("Quel est votre nom ?")

age = input("Quel âge avez vous ?")
age = int(age)

#print(type(prenom))
#print("Cette personne s'appelle : ", prenom, " ", nom, " et son âge est de : ", age, " ans")
#print("Cette personne s'appelle : {} {} et son âge est de {} ans".format(prenom, nom, age))

def verifier_age(prenom,nom,age):
    if age > 35:        
        delaiRestant = CestQuandMes60(age)
        donnees = [prenom, nom, delaiRestant]
        return donnees
    elif age == 35:        
        delaiRestant = CestQuandMes60(age)
        donnees = [prenom, nom, delaiRestant]
        return donnees
    else:        
        delaiRestant = CestQuandMes60(age)
        donnees = [prenom, nom, delaiRestant]
        return donnees
    
contenu = verifier_age(prenom,nom,age)

prenom_recupere = contenu[0]
nom_recupere = contenu[1]
delai_recupere = contenu[2]

print(f"Hello {prenom_recupere} {nom_recupere}, tu auras 60 ans dans {delai_recupere} ans")

