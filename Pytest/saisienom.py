nom = input("quel est ton nom ?")

def verif_nom(n):
    if n == "John":
        return "ok"
    else:
        return "ko"
    

print(verif_nom(nom))