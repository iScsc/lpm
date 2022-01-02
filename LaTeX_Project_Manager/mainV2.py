# -*- coding: utf-8 -*-
# Packages :
import os # Pour la manipulation des dossiers
import shutil # Pour la manipulation des fichiers
from datetime import datetime # Pour la création de l'historique
import traceback # Pour la gestion des erreurs
from pptx import Presentation # Pour la création du .pptx 
# Code :
# Définitions des variables globales :
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S") # Recherche de la date lors de la création de l'historique
main_folder_path = "C:\\Users\\NIC\\Documents\\GitHub\\SUPAERO" # Dossier où sont stockés les projets et documents à créer --> USER INPUT
source_path = "C:\\Users\\Lorinfo\\Documents\\GitHub\\LaTeX-Project-Manager\\LaTeX_Project_Manager\\source_TeX" # Dossier où sont stockés les fichiers sources TeX --> USER INPUT
standard_classe = [
    "book",
    "article",
    "report",
    "letter",
    "scrartcl",
    "scrreprt",
    "scrbook",
    "scrlttr2",
] # Classes "standards" LaTeX utilisées dans mes documents
##########################################################
# Définitions des fonctions utiles :
# --------------------------------------------------------
# Creation d'un historique
def historique(folder):
    """
    Initialisation de l'historique
    """
    fname = folder + "\\historique.txt"
    with open(fname, "w") as file:
        file.write("CREATION HISTORIQUE - INITIALISATION A {date}\n".format(date=date_time))
        file.write("===========================================================\n")

def new_entry(project_name,folder):
    """
    Ajout d'un élément à l'historique
    """
    fname = folder + "\\historique.txt"
    with open(fname,"a") as file:
        file.write("Ajout d'un élément à l'historique à {date}\n".format(date=date_time))
        file.write("--> CREATION DE {pname}\n".format(pname=project_name))
        file.write("-------------------------------------------\n")
# Création du répertoire   
def make_folder(cd,fdname):
    """
    Fonction permettant de créer des dossiers dans un répertoire donné.
    cd --> str ; working directory utilisé pour stocker les fichiers
    fdname --> str ; nom du dossier à créer
    """
    folder_name = fdname
    folder_path = cd + "\\{name}".format(name=folder_name)
    try:
        os.makedirs(folder_path)    
        print("Directory ",folder_name," Created ")
    except FileExistsError:
        print("Directory ",folder_name," already exists")
# Récupération des fichiers sources 
def copytex(fname,fdname):
    """
    Fonction permettant de copier des fichiers d'un répertoire à un autre
    fname --> str ; nom du fichier à copier
    fdname --> str ; nom du dossier dans lequel envoyer le fichier
    NOTE : LE FICHIER PAR DEFAUT DANS LEQUEL SONT PRIS LES FICHIERS .TEX EST source_TeX
    """
    original = source_path + "\\{name}".format(name=fname)
    target = main_folder_path + "\\{fname}".format(fname=fdname) + "\\{name}".format(name=fname)
    shutil.copyfile(original, target)
# Fonction modèle = pas utilisée ici
def rename_file(fdname,cd,old_name,new_name):
    path_old_name = fdname + "\\{cdname}".format(cdname=cd) + "\\{name}".format(name=old_name)
    path_new_name = fdname + main_folder_path + "\\{cdname}".format(cdname=cd) + "\\{name}".format(name=new_name)
    os.rename(path_old_name,path_new_name)
# Création du .pptx
def make_pptx(project_name):
    """
    Fonction permettant de créer la présentation PowerPoint pour stockr
    les images du document
    project_name --> str ; nom du projet où on souhaite créer le fichier
    """
    prs = Presentation()
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = project_name
    subtitle.text = "Illustrations"
    prs.save(main_folder_path + "\\{0}".format(project_name) +"\\images" + "images.pptx")
    # On sauvegarde le document dans le folder 'images'.

# Routine de creation
def create_project(project_name,classe,images=True,pptx=False):
    """
    Routine de création de projet LaTeX.
    project_name --> str ; nom du projet à créer
    classe --> str ; classe du document à créer
    images --> bool, default = True ; indique s'il faut créer un dossier pour stocker des images
    pptx --> bool, default = False ; indique s'il faut créer dans 'images' un .pptx
    """
    cd = main_folder_path # working directory où il faut importer les dossiers
    path = cd + "\\{fdname}".format(fdname=project_name) # Path du nouveau projet à setup
    new_entry(project_name,main_folder_path) # Ajout d'un élément à l'historique correspondant au nouveau projet
    list_file = os.listdir(source_path) # Liste des fichiers se trouvant dans le dossier source
    if classe == "fiche":
        for file in list_file:
            if file.startswith("bristol") or file.startswith("mypackage"):
                copytex(file,project_name)
        if images:
            make_folder(path,"images")
            if pptx:
                make_pptx(project_name)
    elif classe == "standard": # C'est-à-dire 'article'
        make_folder(cd,project_name)
        for file in list_file:
            if file.startswith("glob") or file.startswith("standard"):
                copytex(file,project_name)
        if images: # S'il faut créer un dossier contenant les images du projet
            make_folder(path,"images")
            if pptx:
                make_pptx(project_name)
    elif classe == "book": # C'est-à-dire un projet plus complet
        make_folder(cd,project_name)
        for file in list_file:
            if file.startswith("glob") or file.startswith("standard"):
                    copytex(file,project_name)
    else: # Sinon je veux un beamer
        make_folder(cd,project_name)
        for file in list_file:
            if file.startswith("glob") or file.startswith("beam"):
                copytex(file,project_name)
        if images:
            make_folder(path,"images")
            # Pas besoin de créer un fichier .pptx ici
    try:
        os.chdir(path) # Changement de working directory
        # print("Current working directory: {0}".format(os.getcwd())) # Debug
    except FileNotFoundError:
        print("Le dossier {0} n'existe pas.".format(path))
    except NotADirectoryError:
        print("{0} n'est pas un dossier.".format(path))
    except PermissionError:
        print("Vous n'avez pas la permission de changer {0}".format(path))
    list_file = os.listdir(os.getcwd())
    # print(list_file) # Debug
    if classe in ["book","standard","fiche"]:
        # J'utilise ici mes conventions : elles sont prises en compte dans les fichiers .tex
        os.rename("glob_macros.tex","macros.tex")
        os.rename("glob_PackagesGlobStandard.tex","packages.tex")
        os.rename("standard_snippet_template.tex","main.tex")
    else: # Sinon c'est un beamer
        os.rename("glob_macros.tex","macros.tex")
        os.rename("glob_PackagesGlobStandard.tex","packages.tex")
        os.rename("beam_snippet_template_beamer.tex","main.tex")
    os.startfile(path) # Pour ouvrir quand il a été créé.



##################################################################
# INITIALISATION D'UN NOUVEAU PROJET
# historique(main_folder_path)

create_project("test","article",images=True,pptx=True)
#remove_project("test")

