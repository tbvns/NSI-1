from pyasn1_modules.rfc6664 import id_ecMQV


def ex1():
    while True:
        n = int(input("nb:"))
        if (n > 100) | (n < 0):
            break
        print(n)

def ex2():
    n = float(input("n:"))
    i = 0
    while True:
        r = n/2-3*i
        if r > 0:
            print("got", r, "with", i)
        i+=1

def ex3():
    x=int(input("x:"))
    y=int(input("y:"))
    s = ""
    for i in range(0, y):
        for j in range(0, x):
            s+="*"
        s+="\n"
    print(s)

def ex31():
    y=int(input("y:"))
    s = ""
    for i in range(0, y):
        for j in range(0, i):
            s+="*"
        s+="\n"
    print(s)

def ex4():
    nb = 0
    i = 0
    while True:
        nb+=1
        i+=1
        t = i * 7
        if t%3==0:
            print("*"+str(t))
            continue
        print(t)
        if nb >= 20:
            break

def ex5():
    s = input("text:")
    s2 = ""
    print("iteration:", len(s))
    for i in range(1, len(s) + 1):
        s2+=s[len(s)-i]
    print(s2)

a = "abcdefghijklmnopqrstuvwxyz1234567890°+&é'(-è_çà)='~#{[|`\\^@]}!:;,?./§%ù¨^£$µ¤² "
def ex6():
    s = input("text:")
    n = int(input("n:"))
    r = ""
    i=0
    while n > len(a):
        n-=len(a)
    while n < -len(a):
        n+=len(a)

    for st in s:
        for i in range(0, len(a)):
            q=n+i
            if q >= len(a):
                q=q-len(a)
            if q <= -len(a):
                q=q+len(a)
            if a[i] == st:
                r+=a[q]
    print(r)
