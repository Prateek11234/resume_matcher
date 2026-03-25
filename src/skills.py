def base_skills():
    return [
        "python","machine learning","deep learning","nlp","sql",
        "flask","django","docker","aws","pandas","numpy","api",
        "data analysis","tensorflow","pytorch","excel","git"
    ]

def find(txt, pool):
    f = []
    for s in pool:
        if s in txt:
            f.append(s)
    return list(set(f))

def compare(r,j):
    sk = base_skills()
    r1 = find(r,sk)
    j1 = find(j,sk)

    m = list(set(r1) & set(j1))
    miss = list(set(j1) - set(r1))

    ratio = 0
    if len(j1) > 0:
        ratio = round((len(m)/len(j1))*100,2)

    return m, miss, ratio