# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileReader
# Définition des variables globales :
path_folder = "C:\\Users\\NIC\\Documents\\GitHub\\latex_and_project\\LaTeX_Project_Manager"
pdf_path = "C:\\Users\\NIC\\Documents\\GitHub\\latex_and_project\\LaTeX_Project_Manager\\test.pdf"
# Routine de création du document LaTeX

def creation_tab_impair(page_number):
    if page_number%2==0:
        nbr_group = page_number//2 - 1
    else:
        nbr_group = page_number//2
    liste_tab = []
    compteur = 1
    while compteur < 2*nbr_group:
        liste_int = [compteur,compteur + 2]
        liste_tab.append(liste_int)
        compteur = compteur + 4
    return liste_tab

def creation_tab_full(page_number):
    liste_tab_impair = creation_tab_impair(page_number)
    print(liste_tab_impair)
    if page_number%2==0:
            nbr_group = page_number//2 - 1
    else:
        nbr_group = page_number//2
    liste_tab_pair = []
    compteur = 2
    while compteur <= 2*nbr_group:
        liste_int = [compteur+2,compteur]
        liste_tab_pair.append(liste_int)
        compteur = compteur + 4
    print(liste_tab_pair)
    liste_tab_full = liste_tab_impair
    spacer = 1
    for i in range(len(liste_tab_pair)):
        liste_tab_full.insert(i+spacer,liste_tab_pair[i])
        spacer = spacer + 1
    return liste_tab_full

def process_creation(path_file,path_folder_target,file_name):
    # Récupération du nombre de page.
    document = PdfFileReader(open(path_file, 'rb')) # Ouverture du document cible
    page_number = document.getNumPages() # Récupération du nombre de page total
    print(page_number)
    liste_tab = creation_tab_full(page_number) # Tableau de correspondance pour créer le .tex
    # création du fichier 'process.tex':
    with open(path_folder_target + "\\{0}".format("process.tex"), "w") as fichier:
        fichier.write("\\documentclass[twoside,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage[french]{babel}\n\\usepackage{pdfpages}\n") # Préambule standard pour le fichier
        fichier.write("\\begin{document}")
        # Boucle de création :
        for elem in liste_tab:
            fichier.write("\\includepdf[landscape,nup=1x2,noautoscale,frame,pages={0}".format("{" + str(elem[0]) + "," + str(elem[1]) + "}]{" + file_name  + "}\n"))
        if page_number%2==0:
            fichier.write("\\includepdf[landscape,nup=1x2,noautoscale,frame,pages={0}".format("{" + str(page_number-1) + "," + "{}" + "}]{" + file_name  + "}\n"))
            fichier.write("\\includepdf[landscape,nup=1x2,noautoscale,frame,pages={0}".format("{" + "{}" + "," + str(page_number) + "}]{" + file_name + "}\n"))
        else:
            fichier.write("\\includepdf[landscape,nup=1x2,noautoscale,frame,pages={0}".format("{" + str(page_number) + "," + "{}" + "}]{" + file_name  + "}\n"))
        fichier.write("\\end{document}")
        fichier.close()


process_creation(pdf_path,path_folder,"test.pdf")


