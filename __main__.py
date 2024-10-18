#EX 1
import math

def ex1():
    print("hello", input("Prénom:"))

def ex2():
    print("Price:", float(input("Amount of obj:")) * float(input("Price of 1 obj:")))

def ex3():
    s = input("type:")
    p = float(input("price:"))
    if s == "+":
        print("Added 20%")
        p = p + (p / 100) * 20
    elif s == "-":
        print("Removed 10%")
        p = p - (p / 100) * 10
    else:
        print("Nothing changed.")

    print("price:", p)

def ex4():
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))
    al=b**2+4*a*c
    if al > 0:
        print("2 solutions")
    elif al == 0:
        print("1 solutions")
    else:
        print("aucune solutions")

def ex5():
    c=input("code de sec' social:")
    if len(c) != 13:
        print("code invalide.")
        return
    c=int(c)

    cl=input("clef de controle:")
    if len(cl) != 2:
        print("code invalide.")
        return
    cl=int(cl)

    if (97 - (c%97)) == cl:
        print("code valide.")
    else:
        print("code invalide.")

def ex61():
    n=int(input("nb:"))
    if n > 0:
        print("La valeure en binaire naturel est", n)
    else:
        print("La valeure en binaire naturel est", 256 - n*-1)

def ex62():
    n=int(input("nb:"))
    print("La valeure en binaire naturel est", n - 256)

def ex7():
    n = float(input("nb:"))
    if n >= 0:
        print("sqrt:", math.sqrt(n))
    else:
        print("Invalid number!")

    s1 = input("String 1:")
    s2 = input("String 2:")
    if len(s1) > len(s2):
        print("s1 > s2")
    if len(s1) == len(s2):
        print("s1 = s2")
    else:
        print("s1 < s2")

def ex73():
    n = 0
    p = float(input("p:"))
    v = float(input("v:"))
    if p>2.3:
        n+=1
    if v>7.41:
        n+=1
    if n == 0:
        print("good")
    if (n == 1) & (p>2.3):
        print("increase size")
    else:
        print("reduce volume")
    if n == 2:
        print("shutting down...")

def ex9():
    t = float(input("temp eau:"))
    if t > 100:
        print("gazeu")
    elif t > 0:
        print("liquide")
    else:
        print("solide")

# tb: 16
# b: 14
# ab: 12
# passable: 10
def ex10():
    m = float(input("moyen:"))
    if m < 8:
        print("vs av pas le bac!")
    elif m < 10:
        print("go oral or by by")
    elif (m >= 10) & (m < 12):
        print("vs avez le bac")
    elif (m >= 12) & (m < 14):
        print("asser bien")
    elif (m >= 14) & (m < 16):
        print("bien")
    elif (m >= 16):
        print("tres bien")

