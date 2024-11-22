def ex3():
    found = True
    s = input("saisie en minuscules, majuscules et chiffres seulement : ")
    while found:
        for cha in s:
            if not cha.isalpha() and not cha.isdigit():
                s = input("saisie en minuscules, majuscules et chiffres seulement : ")
            else:
                found = False

def ex4():
    while True:
        chaine = input("Chaîne : ")
        if len(chaine) > 2 and chaine[2] == "$" and chaine.replace("$", "").isdigit(): break
