import os
import shutil
import mmap
import json
import art
import time

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

def WriteToJSON(PathToFile,elem):
    """
    Append a new element to JSON file
    """
    if isinstance(elem,dict):
        with open(PathToFile,"r") as ReadFile:
            SettingsDict = json.load(ReadFile)
        SettingsDict.update(elem)
        with open(PathToFile,"w") as WriteFile:
            json.dump(SettingsDict,WriteFile,indent=4,separators=(',',':'))
            WriteFile.close()
    else:
        raise("{0} is not of type <dict>".format(str(elem)))

def MakeChangeToJSON(PathToFile,TargetField,elem):
    """
    Changes already existing field - for simple input with no dict as value
    """
    with open(PathToFile,"r") as ReadFile:
        SettingsDict = json.load(ReadFile)
    if TargetField not in SettingsDict:
        raise("{0} is not a valid field.".format(TargetField))
    else:
        SettingsDict[TargetField] = elem
        with open(PathToFile,"w") as WriteFile:
            json.dump(SettingsDict,WriteFile,indent=4,separators=(',',':'))

def CreateHistory(PathToWorkingDir):
    """Create in main repo"""
    PathToHistory = os.path.join(PathToWorkingDir,"history.txt")
    if not os.path.exists(PathToHistory):
        with open(PathToHistory,'w') as History:
            History.write(art.text2art("History"))
            History.write(">>> Initializing history for this repository ...\n")
            History.write(">>> Date of creation = {0}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            History.write(">>> Ready to go !\n")
            History.write("###########################################################\n")
            History.close()
        return True
    else:
        return False

def AddElementToHistory(PathToWorkingDir,ProjectName):
    """Add line to history"""
    PathToHistory = os.path.join(PathToWorkingDir,"history.txt")
    if os.path.exists(PathToHistory):
        with open(PathToHistory,'a') as History:
            History.write(">>> Created {project} on {date}.\n".format(project=ProjectName,date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            History.close()
        return True
    else:
        return False

def RegisterDeletion(PathToWorkingDir,ProjectName):
    """
    Register deletion of project in history
    """
    PathToHistory = os.path.join(PathToWorkingDir,"history.txt")
    if os.path.exists(PathToHistory):    
        with open(PathToHistory,'a') as History:
            History.write(">>> Deleted {project} on {date}.\n".format(project=ProjectName,date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            History.close()
        return True
    else:
        return False
        

def CreateLocalSettings(PathToWorkingDir,ProjectName):
    """
    create local settings file
    """
    PathToProjectDir = os.path.join(PathToWorkingDir,ProjectName)
    try:
        MakeFolder(PathToProjectDir,"settings")
        with open(os.path.join(PathToProjectDir,"settings","local_settings.json"),'w') as LocalSettings:
            LocalSettings.close()
        return True
    except:
        return False
    


# CreateHistory(r"/home/nlesquoy/ghq/LaTeX-Project-Manager/test")
# AddElementToHistory(r"/home/nlesquoy/ghq/LaTeX-Project-Manager/test","Test")
