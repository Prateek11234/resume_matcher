from src.vectorizer import vec
from src.matcher import score, final_score
from src.skills import compare

def rank_all(resumes, jd_clean):
    out = []

    for name, txt in resumes:
        m = vec(txt, jd_clean)
        sim = score(m)

        match, miss, ratio = compare(txt, jd_clean)

        fs = final_score(sim, ratio)

        out.append({
            "name": name,
            "score": fs,
            "sim": round(sim*100,2),
            "skill": ratio,
            "match": match,
            "miss": miss
        })

    out = sorted(out, key=lambda x: x["score"], reverse=True)

    return out
