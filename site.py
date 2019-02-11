"""
NAME : Papon Alexis
DESC : Converti un fichier au format Markdown en HTML
Date : 11/02/2019
"""

import os
import sys
import markdown2
import re


link_patterns=[(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]

html_start = "<!doctype html>\n\n<html>\n\n\t<head>\n\n\t\t<meta charset='utf-8'>\n\t\t<link rel='stylesheet' href='style.css'>\n\t\t<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet'>\n\t\t<title>Markdown</title>\n\n\t</head>\n\n\t\t<body>\n\n"
html_fin = "\n\n\t</body>\n\n</html>"

def convert(md_folder, html_folder):
    folder = os.listdir(md_folder)
    print("\n")
    for i in folder:
        f = open(f'{md_folder}/{i}', "r")
        html_content = markdown2.markdown(f.read(), extras=["link-patterns", "cuddled-lists"], link_patterns=link_patterns)
        file_name = os.path.splitext(i)[0]
        print(f'Le fichier "{file_name}" a été converti en "{file_name}.html".')
        html_file = open(f'{html_folder}/{file_name}.html', 'w')
        html_file.write(html_start)
        html_file.write(html_content)
        html_file.write(html_fin)
    print("\n")



if len(sys.argv) == 1:
    print("\nTaper python site.py -h ou site.py --help pour afficher les commandes.\n")

elif (sys.argv[1] == "-i" or sys.argv[1] == "--input_directory") and (sys.argv[3] == "-o" or sys.argv[3] == "--output_directory") and len(sys.argv) == 5:
    md_folder = sys.argv[2]
    html_folder = sys.argv[4]
    convert(md_folder, html_folder)

elif sys.argv[1] == "--help" or sys.argv[1] == "-h" and len(sys.argv) == 2:
    print("\nCe programme convertie un fichier markdown en html pour cela il faut 2 paramètres.\n")
    print("-i ./un_dossier : le chemin du dossier de fichiers .md (contenant les fichiers markdown)")
    print("-o ./un_autre_dossier : le chemin du dossier où seront mis les fichiers générés en .html\n")
    print("python main.py -i ./un_dossier -o ./un_autre_dossier\n")