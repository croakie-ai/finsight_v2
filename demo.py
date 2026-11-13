import pymupdf

doc=pymupdf.open("data/raw/TCS/FY2026.pdf")
page=doc[170]

print(doc.get_toc()[0:30])