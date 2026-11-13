import pymupdf

doc=pymupdf.open("data/raw/TCS/FY2026.pdf")
print("pages: ",len(doc))

def top_lines(page,n=6):
    lines=[]
    for l in page.get_text("text",sort=True).splitlines():
        if l.strip():           
            lines.append(l.strip())
    return " ".join(lines[:n]).lower().replace("’","'")        

phrase="management discussion and analysis"


hits=[]
for i,page in enumerate(doc):
    if phrase in top_lines(page):
        hits.append(i+1)

if len(hits)!=0:
    print(phrase, " -> ",hits)
else:
    print("Not found in top 6 lines of any page")