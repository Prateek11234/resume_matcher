import pdfplumber

def read_pdf(path):
    txt = ""
    try:
        pdf = pdfplumber.open(path)
        for p in pdf.pages:
            t = p.extract_text()
            if t:
                txt += t + "\n"
        pdf.close()
    except:
        print("pdf read issue")
    return txt.strip()