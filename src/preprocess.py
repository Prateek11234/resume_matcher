import re

sw = ["the","is","in","and","to","of","a","for","on","with","as","by"]

def clean(x):
    x = x.lower()
    x = re.sub(r"[^a-z0-9\s]", " ", x)
    parts = x.split()
    out = []
    for w in parts:
        if w not in sw:
            out.append(w)
    return " ".join(out)