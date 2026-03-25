from sklearn.metrics.pairwise import cosine_similarity

def score(m):
    s = cosine_similarity(m[0:1], m[1:2])
    return float(s[0][0])

def final_score(sim, skill_ratio):
    sim_part = sim * 70
    skill_part = (skill_ratio/100) * 30
    return round(sim_part + skill_part,2)