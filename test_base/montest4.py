import mesfonctions

prenom = input("Quel est votre prénom ?")
nom = input("Quel est votre nom ?")

age = input("Quel âge avez vous ?")
age = int(age)

rep = True

contenu = mesfonctions.verifierAge(prenom, nom, age)

prenom_recupere = contenu[0]
nom_recupere = contenu[1]
delai_recupere = contenu[2]

print(f"Hello {prenom_recupere} {nom_recupere}, tu auras 60 ans dans {delai_recupere} ans")

#mesfonctions.continuer(rep)
mesfonctions.direAurevoir(prenom,nom)
