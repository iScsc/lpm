import os # Pour la manipulation des dossiers
import shutil # Pour la manipulation des fichiers
import traceback # Pour la gestion des erreurs
## CONVENTIONS :
# Convention --> %ID:type : {thm:théorème,def:définition,prp:proposition,lem:lemme,cor:corollaire,exe:exemple,exr:exercice,prv:preuve}-chapter-section-subsection-num
# Convention --> pour les preuves,ID du texte associé à la fin
# %TITLE:titre
# %BEGIN text %END --> balise de répérage du corps du texte.
## TEST :
# with open(path,'r',encoding='UTF-8') as file: # Il est important de préciser l'encodage !
#     content = file.readlines() # On récupère le contenu sous forme de liste.
# liste_ID = [] # liste des ID
# chapters_num = [] # liste de sauvegarde des numéros de chapitres
# section_num = [] # idem pour les sections
# subsection_num = [] # idem pour les sous-sections
# contenu_raw = [] # liste de listes de listes avec le contenu du document final
# for i in range(len(content)):
#     if content[i].startwith('%ID'):
#         liste_ID.append(i) # Position des ID, donne aussi le début de chaque nouvel élément
# for j in range(liste_ID):
#     ID = content[liste_ID[j]]
#     tri_int = ID.split('-')

# with open(path,'a',encoding='UTF-8') as file:
#     file.write("\\begin{theorem}[Un magnifique theorem]\nun truc\n\\end{theorem}")
#     file.close()
# ID_int = "ID:thm-1-2-1"
# ID_int = ID_int.split(":") # On récupérer l'ID et on le casse --> c'est une liste.
# ID_int.pop(0) # On supprime l'en-tête
# ID_int = ID_int[0].split("-")
# print(ID_int)
#print(content)

## CODE :
# Variables globales :
content = []
path = r"C:\Users\NIC\Documents\GitHub\latex_and_project\LaTeX_Project_Manager\TEST_TeX\test_templates.tex"
with open(path,'r',encoding='UTF-8') as file: # Il est important de préciser l'encodage !
    content = file.readlines()
liste_ID = []
for i in range(len(content)):
    if content[i].startswith('%ID'):
        liste_ID.append(i) # Position des ID, donne aussi le début de chaque nouvel élément
#print([content,len(content)])
#print([liste_ID,len(liste_ID)])
table_comp = {
    "thm":"theorem",
    "prp":"proposition",
    "prv":"proof"
} # Table de liaison entre les ID et les environnements correspondants
balises = ["%BEGIN\n","%END\n"] # Balises indiquant le début et la fin du corps du texte
contenu_raw = [] # Liste de listes de listes contenant le contenu trié
# Structure = i:%ID,i+1:%title:text,i+2:%BEGIN,...,i+N:%END
# Creation de la grille :
nbr_chap,nbr_sec=2,[2,2]
for i in range(nbr_chap):
    contenu_raw.append([])
for i in range(len(contenu_raw)):
    for j in range(nbr_sec[i]):
        contenu_raw[i].append([])
#print(contenu_raw)
# Boucle principale:
for i in range(len(liste_ID)):
    ID_int = content[liste_ID[i]].split(":") # On récupérer l'ID et on le casse --> c'est une liste.
    ID_int.pop(0) # On supprime l'en-tête
    ID_int = ID_int[0].split("-")
    title_int = content[liste_ID[i]+1].split(":")
    print(title_int)
    title_int.pop(0)
    print(title_int)
    title_int = title_int[0] # Récupération du titre
    print(title_int)
    compteur_int = 4 # On initialise au début du corps du texte
    corps_int = "" # Variable de stockage du corps
    while content[liste_ID[i] + compteur_int] not in balises and liste_ID[i] + compteur_int < len(content)-1:
        corps_int = corps_int + content[liste_ID[i] + compteur_int]
        #print(corps_int)
        compteur_int = compteur_int + 1
        #print(compteur_int)
    # On a fini de récupérer tous les éléments. Il faut maintenant trier :
    env_name = table_comp[ID_int[0]]
    chapters_num,sections_num = int(ID_int[1])-1,int(ID_int[2])-1
    # Assemblage du bloc de texte avec la syntaxe LaTeX
    corps = "\\begin{" + env_name + "}[" + title_int + "]\n" + corps_int + "\n" + "\\end{" + env_name + "}\n"
    # Installation dans la grille
    contenu_raw[chapters_num][sections_num].append(corps)
print(contenu_raw)
#print(content)




