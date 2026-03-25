import streamlit as st

from src.parser import read_pdf
from src.preprocess import clean
from src.ranker import rank_all


st.title("ai resume matcher")

files = st.file_uploader("upload resumes", accept_multiple_files=True)
jd = st.text_area("job description")

if st.button("run"):
    if files and jd:

        jd_clean = clean(jd)

        all_resumes = []

        for f in files:
            name = f.name
            open("tmp.pdf","wb").write(f.read())

            txt = read_pdf("tmp.pdf")
            txt = clean(txt)

            all_resumes.append((name, txt))

        res = rank_all(all_resumes, jd_clean)

        st.subheader("ranking")

        for i,r in enumerate(res):
            st.write(f"{i+1}. {r['name']} - {r['score']}%")

            st.progress(int(r["score"]))

            st.write("sim:", r["sim"],"% | skill:", r["skill"],"%")

            if r["match"]:
                st.write("match:", r["match"])

            if r["miss"]:
                st.write("missing:", r["miss"])

            st.write("---")

    else:
        st.write("upload files + jd")