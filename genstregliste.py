#!/usr/bin/env python
# -*- coding: utf8 -*-

def header():
        return '''\\documentclass[10pt,a4paper,danish]{article}
        \\usepackage[danish]{babel}
        \\usepackage[utf8]{inputenc}
        \\usepackage[margin=1cm]{geometry}
        \\usepackage{graphicx}
        \\usepackage{array}
        \\usepackage{amssymb}
        \\usepackage[table]{xcolor}
        \\setlength\\parskip{0em}
        \\setlength\\parindent{0em}
        \\begin{document}
        '''

def footer():
    return '''\\end{document}
'''

def table(items, names, rowsize=None, per_page=None):
    table_header = ''
    if rowsize is not None:
        table_header += '\\renewcommand\\arraystretch{%f} \\setlength\\minrowclearance{%fpt}' % (rowsize, rowsize)
    table_header += '''\\rowcolors{1}{white}{lightgray}
\\resizebox{\\textwidth}{!} {
\\begin{tabular}[h!]{'''+"|l"+"|p{0.50\\textwidth}"+("|c"*(len(items)-1) + "|")+"}\n"
    table_header += "\hline"
    table_header += " Navn " + "& "
    table_header += " & ".join(items)
    table_header += "\\\\\n"
    table_header += "\hline"
    res = table_header
    for i in range(len(names)):
        if per_page is not None and i % per_page == 0 and i > 0:
                res += "\\end{tabular}}" + table_header
        res += "  " + names[i] + (" &"*(len(items))) + "\\\\\n"
        res += "\hline"
    res += '\\end{tabular}}'
    return res


# Indlæs navne
with open('russer.txt') as f:
    russer = f.read().strip().split('\n')

with open('vejledere.txt') as f:
    vejledere = f.read().strip().split('\n')

with open('vejledere-alle.txt') as f:
    vejlederealle = f.read().strip().split('\n')


def liste(items, names, filename, rowsize=None, per_page=None):
    with open(filename + '.tex', mode="w") as tex:
        tex.write(header())
        tex.write(table(items, names, rowsize, per_page))
        tex.write(footer())

def checkliste(names, filename):
    with open(filename + '.tex', mode="w") as tex:
        tex.write(header())
        for name in names:
            table_header = ''
        table_header += '''\\rowcolors{1}{white}{lightgray}
    \\resizebox{\\textwidth}{!} {
    \\begin{tabular}{l'''+"p{0.50\\textwidth}"+("l"*4 + "")+"}\n"
        res = table_header
        for i in range(0,len(names),2):
            res += names[i] + " & $\square$ "
            try:
                res += "&" + names[i+1] + "& $\square$ "
            except IndexError:
                pass
            res += "\\\\\n"
        res += "\\end{tabular}}"
        tex.write(res)
        tex.write(footer())



if __name__ == '__main__':
    # Skabelon til streglister
    drikkevarer = ['Øl', 'Light', 'Sodavand', 'Cider', 'Rødvin']
    campusdrikkevarer = ['Øl', 'Light', 'Alle andre ting']
    mad = ['Mad på fad']
    afleveret = ['Har afleveret']
    liste(drikkevarer, russer, 'russer-stregliste', 1.3)
    liste(drikkevarer, vejledere, 'vejleder-stregliste')
    liste(campusdrikkevarer, vejlederealle, 'vejleder-alle-stregliste')
    liste(mad, russer, 'russer-stregliste-mad')
    liste(mad, vejledere, 'vejleder-stregliste-mad')
    liste(afleveret, russer, 'russer-afleveret', 2.4, 14)
    checkliste(russer, 'russer-checkliste')
