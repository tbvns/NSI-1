import math

def ex(i):
    return math.pi*i**2

def ex2(i1, i2, i3):
    return i1*i2*i3

def ex3(i1, i2, i3):
    l = i1
    if i2 > l: l = i2
    if i3 > l: l = i3
    return l

def ex4(s, c):
    n = 0
    for i in range(len(s)):
        if s[i] == c: n+=1
    return n

def ex5(li):
    l = 0
    for i in range(len(li)):
        if li[i] > l: l = li[i]
    return l

def ex6(nb):
    liste = {1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril', 5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août', 9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'}
    return liste[nb]

def ex7(x1 = 10, x2 =10, x3 = 10):
    return x1 * x2 * x3

def ex8(x1 = None, x2 = None, x3 = None):
    if x2 is None:
        x2 = x1
    if x3 is None:
        x3 = x1
    if x1 is None:
        print(-1)
    else:
        return

