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


def ex3():
    a ="abcdefghijklmnopqrstuvwxyz"
    l = []
    for s in a:
        for s1 in a:
            l.append(s+s1)
    print(l)

