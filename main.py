import os

from src.parser import read_pdf
from src.preprocess import clean
from src.ranker import rank_all


def run():
    path = input("folder path: ")
    jd_path = input("jd file: ")

    f = open(jd_path,"r",encoding="utf-8")
    jd = clean(f.read())
    f.close()

    res = []

    for file in os.listdir(path):
        if file.endswith(".pdf"):
            p = os.path.join(path,file)
            txt = read_pdf(p)
            txt = clean(txt)
            res.append((file,txt))

    out = rank_all(res,jd)

    for i,r in enumerate(out):
        print(i+1, r["name"], r["score"],"%")


if __name__ == "__main__":
    run()