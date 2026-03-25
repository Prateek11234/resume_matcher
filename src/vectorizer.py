from sklearn.feature_extraction.text import TfidfVectorizer

def vec(a,b):
    v = TfidfVectorizer()
    m = v.fit_transform([a,b])
    return m