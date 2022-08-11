import os # Pour la manipulation des dossiers
import shutil # Pour la manipulation des fichiers
import SettingsClass
import mmap
# from pptx import Presentation # Pour la création du .pptx


def MakeFolder(WorkingDir,FolderName):
    """
    Fonction permettant de créer des dossiers dans un répertoire donné.
    WorkingDir --> str ; working directory utilisé pour stocker les fichiers
    FolderName --> str ; nom du dossier à créer
    """
    FolderPath = os.path.join(WorkingDir,FolderName)
    try:
        os.makedirs(FolderPath)    
        print("Directory ",FolderName," Created ")
    except FileExistsError:
        print("Directory ",FolderName," already exists")

def CopyTeX(WorkingDir,FileName,FolderName,PathToSource):
    """
    Fonction permettant de copier des fichiers d'un répertoire à un autre
    WorkingDir --> str ; dossier principal
    FileName --> str ; nom du fichier à copier
    FolderName --> str ; nom du dossier dans lequel envoyer le fichier
    """
    original = os.path.join(PathToSource,FileName)
    target = os.path.join(WorkingDir,FolderName,FileName)
    shutil.copyfile(original, target)

# def MakePPTX(WorkingDir,FolderName):
#     """
#     Fonction permettant de créer la présentation PowerPoint pour stockr
#     les images du document
#     WorkingDir --> Folder où est mis le projet
#     """
#     prs = Presentation()
#     title_slide_layout = prs.slide_layouts[0]
#     slide = prs.slides.add_slide(title_slide_layout)
#     title = slide.shapes.title
#     subtitle = slide.placeholders[1]

#     title.text = FolderName
#     subtitle.text = "Illustrations"
#     try:
#         MakeFolder(WorkingDir,"images")
#         prs.save(os.path.join(WorkingDir,FolderName,"images","images.pptx"))
#     except:
#         print("Something happened when creating the folder")
#     # On sauvegarde le document dans le folder 'images'.

def SearchTeX(SearchWord,FileName):
    with open(FileName, 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if s.find(bytes(SearchWord,encoding='utf-8')) != -1:
            file.close()
            return True
        else:
            file.close()
            return False

print(SearchTeX("truc","/home/nlesquoy/ghq/LaTeX-Project-Manager/test/test.txt"))