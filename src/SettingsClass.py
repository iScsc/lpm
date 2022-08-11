# Settings.py - global variables
import json

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

# test = Settings(r"/home/nlesquoy/ghq/LaTeX-Project-Manager/settings/config.json")
# print(Settings.GetClassDep(test,"standard"))
