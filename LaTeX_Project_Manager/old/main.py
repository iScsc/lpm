# -*- coding: utf-8 -*-
# Packages :
import os
import shutil
from datetime import datetime
# ======================================
# Code :
# ======================================
# Définitions des variables globales :
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S") # Recherche de la date lors de la création de l'historique
main_folder_path = "C:\\Users\\Lorinfo\\Documents\\GitHub\\SUPAERO" # Dossier où sont stockés les projets et documents à créer --> USER INPUT
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
    original = "C:\\Users\\Lorinfo\\Documents\\GitHub\\latex_and_project\\LaTeX_Project_Manager\\source_TeX\\{name}".format(name=fname)
    target = main_folder_path + "\\{fname}".format(fname=fdname) + "\\{name}".format(name=fname)
    shutil.copyfile(original, target)
# Fonction modèle = pas utilisée ici
def rename_file(fdname,cd,old_name,new_name):
    path_old_name = fdname + "\\{cdname}".format(cdname=cd) + "\\{name}".format(name=old_name)
    path_new_name = fdname + main_folder_path + "\\{cdname}".format(cdname=cd) + "\\{name}".format(name=new_name)
    os.rename(path_old_name,path_new_name)
# Routine de creation
def create_project(project_name,classe,images=True):
    """
    Routine de création de projet LaTeX.
    project_name --> str ; nom du projet à créer
    classe --> str ; classe du document à créer
    images --> bool, default = True ; indique s'il faut créer un dossier pour stocker des images
    """
    cd = main_folder_path # working directory où il faut importer les dossiers
    path = cd + "\\{fdname}".format(fdname=project_name)
    new_entry(project_name,main_folder_path)
    list_file = os.listdir("C:\\Users\\Lorinfo\\Documents\\GitHub\\latex_and_project\\LaTeX_Project_Manager\\source_TeX")
    if classe in standard_classe:
        make_folder(cd,project_name)
        for file in list_file:
            if file.startswith("glob") or file.startswith("standard"):
                copytex(file,project_name)
        if images: # S'il faut créer un dossier contenant les images du projet
            make_folder(path,"images")
    else:
        make_folder(cd,project_name)
        for file in list_file:
            if file.startswith("glob") or file.startswith("beam"):
                copytex(file,project_name)
        if images:
            make_folder(path,"images")
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
    if classe in standard_classe:
        # J'utilise ici mes conventions : elles sont prises en compte dans les fichiers .tex
        os.rename("glob_macros.tex","macros.tex")
        os.rename("glob_PackagesGlobStandard.tex","packages.tex")
        os.rename("standard_snippet_template.tex","main.tex")
    else:
        os.rename("glob_macros.tex","macros.tex")
        os.rename("glob_PackagesGlobStandard.tex","packages.tex")
        os.rename("beam_snippet_template_beamer.tex","main.tex")
    os.startfile(path) # Pour ouvrir quand il a été créé.


##################################################################
# INITIALISATION D'UN NOUVEAU PROJET
# historique(main_folder_path)
create_project("Crrect","article",images=False)

