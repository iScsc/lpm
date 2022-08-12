# Settings.py - global variables
import json
import InteractFunc
import os

class Settings:
    def __init__(self,PathToJSON):
        self.PathToJSON = PathToJSON
    
    def GetSettings(self):
        "Loads json"
        with open(self.PathToJSON,"r") as ReadFile:
            SettingsDict = json.load(ReadFile)
        return SettingsDict
    
    def GetPathToSource(self):
        "Get path to TeX sources"
        return Settings.GetSettings(self)["PathToSource"]
    
    def GetClassList(self):
        "Get available classes"
        SettingsDict = Settings.GetSettings(self)
        return [SettingsDict["latex_class"][i]["name"] for i in range(len(SettingsDict["latex_class"]))]
    
    def GetClassDep(self,ClassName):
        "Get Class dependencies"
        SettingsDict = Settings.GetSettings(self)
        ClassList = [SettingsDict["latex_class"][i]["name"] for i in range(len(SettingsDict["latex_class"]))]
        return SettingsDict["latex_class"][ClassList.index(ClassName)]["dependencies"]
    
    def CheckDep(self,ClassName):
        "Check Class dependencies"
        SettingsDict = Settings.GetSettings(self)
        ClassList = [SettingsDict["latex_class"][i]["name"] for i in range(len(SettingsDict["latex_class"]))]
        DepList = SettingsDict["latex_class"][ClassList.index(ClassName)]["dependencies"]
        ClassFile = "".join([ClassName,".tex"])
        Path = os.path.join(Settings.GetPathToSource(self),ClassFile)
        for dep in DepList:
            if dep != ClassFile:
                FileName,FileExtension = dep.split('.')
                Result = InteractFunc.SearchTeX(FileName.removesuffix(FileExtension),Path)
                if not Result:
                    return False
        return True

SettingsLaunch = Settings(r"/home/nlesquoy/ghq/LaTeX-Project-Manager/settings/config.json")

# print(InteractFunc.SearchTeX("packages.tex".removesuffix(".tex"),r"/home/nlesquoy/ghq/LaTeX-Project-Manager/source_TeX/standard.tex"))
