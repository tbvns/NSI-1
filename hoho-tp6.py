def ex3():
    s = "&"
    false = False
    while false:
        for cha in s:
            if not cha.isalpha() and not cha.isdigit():
                s = input("saisie en minuscules, majuscules et chiffres seulement : ")
            else:
                false = True