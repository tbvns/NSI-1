def ex1():
    text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    d = {}
    l = []
    for s in text:
        if s in d.keys():
            d[s]+=1
            continue
        d[s]=1
        l.append([s, d[s]])

def ex2():
    result = []
    for i in range(1000):
        somme = 0
        for x in str(i):
            somme += int(x)**3
        if int(i) == somme:
            result.append(i)
    return result

def ex3():
    a ="abcdefghijklmnopqrstuvwxyz"
    l = []
    for s in a:
        for s1 in a:
            l.append(s1+s)
    print(l)

def ex5():
    d = {"test":"test5", "test1":"tes2", "test8":"test0", "test87":"tes5641"}
    nd = {}
    for k in range(0, len(d.values())):
        nd[list(d.values())[k]] = list(d.keys())[k]
    return nd

def count_car(ch, c):
    return ch.count(c)

def ordre_frequence(chaine):
    frequence = {}
    for char in chaine:
        if char != ' ':  # On ignore les espaces
            frequence[char] = frequence.get(char, 0) + 1
    return sorted(frequence.items(), key=lambda x: x[1], reverse=True)

# Fonction pour afficher la liste triée par ordre décroissant de fréquences
def ex6(chaine):
    frequence_triee = ordre_frequence(chaine)
    for char, count in frequence_triee:
        print(f"{char} est apparue {count} fois.")
