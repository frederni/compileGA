import csv
import os
def getPreWrap():
    return """\documentclass{article}
\\usepackage[utf8]{inputenc}

\\title{Endringsforslag}
\\author{Linjeforeningen Nabla}
\date{}

\\usepackage{graphicx}
\\usepackage{tabularx,ragged2e,booktabs,caption}
\\newcolumntype{L}{>{\RaggedRight\\arraybackslash}X} % modified 'X' column type

\\begin{document}
\maketitle

"""

def generateTable(i, name, case, suggestionType, origTXT, newTXT, reasoning):
    mainStr = """\\begin{table}[ht!]
\captionsetup{font=bf,skip=0.5\\baselineskip}
\caption*{F""" + str(i) + """}
\\begin{tabularx}{\\textwidth}{@{}lL@{}}
\\toprule
Forslagsstiller & """ +str(name) + "\\\ \nSak & " + str(case) + " \\\ \nType forslag & " + str(suggestionType) + " \\\ \nOpprinnelig tekst & " + str(origTXT) + " \\\ \nNy tekst & " + str(newTXT) + "\\\ \nBegrunnelse & " + str(reasoning) + """ \\\ 
\\bottomrule
\end{tabularx}
\end{table}"""
    return mainStr
def getPostWrap():
    return "\n\end{document}"


def load_data(fn):
    """
    Only works with following question order
    * Email
    * Navn
    * Saksnummer
    * Forslagstype
    * Opprinnelig tekst
    * Ny tekst
    * Begrunnelse
    """
    with open(fn,newline = "\n", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        datalist = list(reader)
    
    N = len(datalist)
    timestamp_data = [datalist[i][0] for i in range(1,N)]
    email_data = [datalist[i][1] for i in range(1,N)]
    name_data = [datalist[i][2] for i in range(1,N)]
    case_data = [datalist[i][3] for i in range(1,N)]
    suggType_data = [datalist[i][4] for i in range(1,N)]
    orig_data = [datalist[i][5] for i in range(1,N)]
    new_data = [datalist[i][6] for i in range(1,N)]
    reason_data = [datalist[i][7] for i in range(1,N)]
    return {"t": timestamp_data, "eml": email_data, "name": name_data, "case": case_data, "sType": suggType_data, "orig": orig_data, "new": new_data, "reason": reason_data}

dta = load_data("test.csv")
allTables = """"""
for i in range(len(dta["t"])):
    allTables += generateTable(i+1, dta["name"][i], dta["case"][i], dta["sType"][i], dta["orig"][i], dta["new"][i], dta["reason"][i])
    allTables += "\n\n"


with open("endringsforslag.tex", "w", encoding="utf-8") as f:
    f.write(getPreWrap())
    f.write(allTables)
    f.write(getPostWrap())
usrAns = input("Har du pdflatex installert lokalt på din maskin? (Y/N) ")
if usrAns.upper() == "Y":
    print("Kompilerer...\nVær obs på dialogbokser hvis pdflatex må installere nødvendige pakker")
    os.system("pdflatex endringsforslag.tex")
    print("Endringsforslag er kompilert til \"endringsforslag.pdf\"")
else:
    print("Endringsforslag konvertert til LaTeX!\nÅpne endringsforslag.tex i notepad og lim inn i Overleaf.")
