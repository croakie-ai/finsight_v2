import pymupdf
import os

for company in ["TCS","Infosys","Wipro"]:
    folder="data/raw/"+company
    for name in os.listdir(folder):
        doc=pymupdf.open(folder+"/"+name)
        toc=doc.get_toc()
        print(company, name, "pages:",len(doc), "bookmarks:",len(toc))