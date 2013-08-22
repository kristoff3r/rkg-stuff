# -*- coding: utf8 -*-
stuff = ["Øl", "Light", "Sodavand", "Cider", "Rødvin"]
russer = ["Søren", "faggot", "Martin"]

def drinklist(items, names):
    with open("stregliste.tex", mode="w") as tex:
        tex.write(
'''\\documentclass[10pt,a4paper,danish]{article}
\\usepackage[danish]{babel}
\\usepackage[utf8]{inputenc}
\\usepackage[margin=1cm]{geometry}
\\usepackage{graphicx}
\\usepackage{array}
\\usepackage[table]{xcolor}


\\setlength\\parskip{0em}
\\setlength\\parindent{0em}

\\begin{document}
\\begin{center}
\\rowcolors{1}{white}{lightgray}
\\resizebox{\\textwidth}{!} {
\\begin{tabular}[h!]{'''+"|l"+"|p{0.50\\textwidth}"+("|c"*(len(items)-1) + "|")+"}\n")
        tex.write("\hline")
        tex.write("  " + "& ")
        tex.write(" & ".join(items))
        tex.write("\\\\\n")
        tex.write("\hline")

        for name in names:
            tex.write("  " + name + (" &"*(len(items))) + "\\\\\n")
            tex.write("\hline")

        tex.write('''
\\end{tabular}}
\\end{center}
\\end{document}
''')


drinklist(stuff, russer)


