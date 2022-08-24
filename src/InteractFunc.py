import os
import shutil
import subprocess
import mmap
import json
import art
import time

def MakeFolder(WorkingDir,FolderName):
    """Creates a folder in the specified directory.

    :param WorkingDir: The target directory where the new folder should be created
    :type WorkingDir: str
    :param FolderName: Name of the new folder
    :type FolderName: str
    """
    FolderPath = os.path.join(WorkingDir,FolderName)
    try:
        os.makedirs(FolderPath)    
        print("Directory ",FolderName," created.")
    except FileExistsError:
        print("Directory ",FolderName," already exists.")

def CopyTeX(WorkingDir,FileName,FolderName,PathToSource):
    """Copies a file.

    :param WorkingDir: Target directory
    :type WorkingDir: str
    :param FileName: the file name (with extension) that needs to be copied
    :type FileName: str
    :param FolderName: Target folder (inside :param:`WorkingDir`)
    :type FolderName: str
    :param PathToSource: Path to LaTeX source files
    :type PathToSource: str
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

def SearchTeX(SearchWord,FileName)->bool:
    """Checks if a word is inside a text file or not.

    :param SearchWord: The target word
    :type SearchWord: str
    :param FileName: Path to the file where the word should be.
    :type FileName: str
    :return: True if the word is in the file, false if not.
    :rtype: bool
    """
    with open(FileName, 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if s.find(bytes(SearchWord,encoding='utf-8')) != -1:
            file.close()
            return True
        else:
            file.close()
            return False

def WriteToJSON(PathToFile,elem):
    """Add a new element to a JSON file

    :param PathToFile: Path to the JSON file
    :type PathToFile: str
    :param elem: Complex element that needs to be added.
    :type elem: dict
    """
    if isinstance(elem,dict):
        with open(PathToFile,"r") as ReadFile:
            SettingsDict = json.load(ReadFile)
        SettingsDict.update(elem)
        with open(PathToFile,"w") as WriteFile:
            json.dump(SettingsDict,WriteFile,indent=4,separators=(',',':'))
            WriteFile.close()
    else:
        print("{0} is not of type <dict>".format(str(elem)))

def MakeChangeToJSON(PathToFile,TargetField,elem):
    """Makes changes to a simple field in a JSON file. The file
    must already exist.

    :param PathToFile: Path to the target file.
    :type PathToFile: str
    :param TargetField: The field that will be modified.
    :type TargetField: str
    :param elem: The element that will modify the `TargetField` JSON field.
    :type elem: str
    """
    with open(PathToFile,"r") as ReadFile:
        SettingsDict = json.load(ReadFile)
    if TargetField not in SettingsDict:
        print("{0} is not a valid field.".format(TargetField))
    else:
        SettingsDict[TargetField] = elem
        with open(PathToFile,"w") as WriteFile:
            json.dump(SettingsDict,WriteFile,indent=4,separators=(',',':'))

def CreateHistory(PathToWorkingDir)->bool:
    """Initializes the `history.txt` file in a new directory.

    :param PathToWorkingDir: Path to the target directory.
    :type PathToWorkingDir: str
    :return: True if the file was created, false if not.
    :rtype: bool
    """
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

def AddElementToHistory(PathToWorkingDir,ProjectName)->bool:
    """Add a line to the `history.txt` file when creating a new file.

    :param PathToWorkingDir: Path to the main directory where the history file is located.
    :type PathToWorkingDir: str
    :param ProjectName: Name of the project that will be created
    :type ProjectName: str
    :return: True if the line could be added, false if not.
    :rtype: bool
    """
    PathToHistory = os.path.join(PathToWorkingDir,"history.txt")
    if os.path.exists(PathToHistory):
        with open(PathToHistory,'a') as History:
            History.write(">>> Created {project} on {date}.\n".format(project=ProjectName,date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            History.close()
        return True
    else:
        return False

def RegisterDeletion(PathToWorkingDir,ProjectName)->bool:
    """Takes note of the deletion of a project in `history.txt`.

    :param PathToWorkingDir: Path to the main directory where the history file is located.
    :type PathToWorkingDir: str
    :param ProjectName: Name of the project that will be deleted
    :type ProjectName: str
    :return: True if the line could be added, false if not.
    :rtype: bool
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
    """Creates a `local_settings.json` file - This feature has no use for now.

    :param PathToWorkingDir: Path to the main directory
    :type PathToWorkingDir: str
    :param ProjectName: Name of the project where the file should be located
    :type ProjectName: str
    :return: True if the file could be created, false if not.
    :rtype: bool
    """
    PathToProjectDir = os.path.join(PathToWorkingDir,ProjectName)
    try:
        MakeFolder(PathToProjectDir,"settings")
        with open(os.path.join(PathToProjectDir,"settings","local_settings.json"),'w') as LocalSettings:
            LocalSettings.close()
        return True
    except:
        return False
    
def SaveProgress(Message):
    command = "git add . ; git commit -m {0} ; git push".format(Message)
    subprocess.run(command,shell=True)