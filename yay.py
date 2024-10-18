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

#flemme
#def ex6():

#ex8 aussi
def ex7(i1 = None, i2 = 10, i3 = 10):

    return i1*i2*i3

print(ex7(5.2, 3))