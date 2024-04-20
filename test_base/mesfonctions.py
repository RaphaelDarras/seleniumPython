CestQuandMes60 = lambda age : 60 - age

def direAurevoir(prenom,nom):
    print(f"Bon et bien au revoir {prenom} {nom}")

def verifierAge(prenom,nom,age):
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

def continuer(rep):
    while rep:
        saisie = input("Continuer ? (y/n)")
        if saisie == "y":
            continue
        elif saisie == "n":
            rep = False
        else :
            print("Je ne comprends pas. Continuer ? (y/n)")