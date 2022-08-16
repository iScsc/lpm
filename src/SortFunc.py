import os
import shutil
import json
from typing import Any
import InteractFunc

def InitFolder(PathToFolder:str,ListOfFolders:list)->Any:
    for folder in ListOfFolders:
        if not os.path.exists(os.path.join(PathToFolder,folder)):
            InteractFunc.MakeFolder(PathToFolder,folder)


def GetAllFiles(PathToFolder:str)->list:
    os.chdir(PathToFolder)
    return [file for file in os.listdir(PathToFolder) if os.path.isfile(os.path.join(PathToFolder,file))]

def GetAllFolders(PathToJSON:str)->list:
    with open(PathToJSON,"r") as ReadFile:
        SettingsDict = json.load(ReadFile)
        ReadFile.close()
    return SettingsDict["ListOfFolders"]


def GetExclude(PathToJSON:str)->list:
    with open(PathToJSON,"r") as ReadFile:
        SettingsDict = json.load(ReadFile)
        ReadFile.close()
    return SettingsDict["Exclude"]

def CheckConvention(PathToFolder:str,PathToJSON:str)->bool:
    FileList = GetAllFiles(PathToFolder)
    FlagList = [True for i in range(len(FileList))]
    ExcludeList = GetExclude(PathToJSON)
    Convention = GetAllFolders(PathToJSON)
    for file in FileList:
        for folder in Convention:
            if file.startswith(folder) and file not in ExcludeList:
                FlagList[FileList.index(file)] = False
                break
    return False in FlagList

def SortFiles(PathToFolder:str,PathToJSON:str)->Any:
    if CheckConvention(PathToFolder,PathToJSON):
        FileList = GetAllFiles(PathToFolder)
        TargetFolder = GetAllFolders(PathToJSON)
        ExcludeList = GetExclude(PathToJSON)
        for file in FileList:
            for folder in TargetFolder:
                if file.startswith(folder) and file not in ExcludeList:
                    shutil.move(os.path.join(PathToFolder,file),os.path.join(PathToFolder,folder,file))
                    break
    else:
        print("Something went wrong when sorting the files.")
        