#!/usr/bin/env python
# -*- coding: utf8 -*-


def header():
    return '''\\documentclass[10pt,a4paper,danish]{article}
\\usepackage[danish]{babel}
\\usepackage[utf8]{inputenc}
\\usepackage[margin=1cm]{geometry}
\\usepackage{graphicx}
\\usepackage{array}
\\usepackage[table]{xcolor}
\\setlength\\parskip{0em}
\\setlength\\parindent{0em}'''

# Indlæs navne
with open('russer.txt') as f:
    russer = f.read().strip().split('\n')

with open('vejledere.txt') as f:
    vejledere = f.read().strip().split('\n')


# Skabelon til streglister
drikkevarer = ['Øl', 'Light', 'Sodavand', 'Cider', 'Rødvin']
mad = ['Mad på fad']
def drinklist(items, names, filename):
    with open(filename + '.tex', mode="w") as tex:
        tex.write(header())

        tex.write('''
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

# Skabelon til afleverede ting
afleveret = ['Har afleveret']
def afleverede_ting(items, names, filename):
    with open(filename + '.tex', mode="w") as tex:
        tex.write(header())
        #tex.write('\\renewcommand\\arraystretch{2.4} \\setlength\\minrowclearance{2.4pt}')
        tex.write('''
\\begin{document}
\\begin{center}
\\rowcolors{1}{white}{lightgray}
\\resizebox{\\textwidth}{!} {
\\begin{tabular}[h!]{'''+"|l"+"|p{0.50\\textwidth}"+("|c"*(len(items)-1) + "|")+"}\n")
        tex.write("\hline")
        tex.write(" Navn " + "& ")
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


if __name__ == '__main__':
    drinklist(drikkevarer, russer, 'russer-stregliste')
    drinklist(drikkevarer, vejledere, 'vejleder-stregliste')
    drinklist(mad, russer, 'russer-stregliste-mad')
    drinklist(mad, vejledere, 'vejleder-stregliste-mad')
    afleverede_ting(afleveret, russer, 'russer-afleveret')
