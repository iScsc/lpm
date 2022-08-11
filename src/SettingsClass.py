# Settings.py - global variables
import json

class SettingsClass:
    def __init__(self,PathToJSON):
        self.PathToJSON = PathToJSON
    
    def GetSettings(self):
        "Loads json"
        with open(self.PathToJSON,"r") as ReadFile:
            SettingsDict = json.load(ReadFile)
        return SettingsDict
    
    def GetClassList(self):
        "Get available classes"
        SettingsDict = SettingsClass.GetSettings(self)
        return [SettingsDict["latex_class"][i]["name"] for i in range(len(SettingsDict["latex_class"]))]

# test = SettingsClass(r"/home/nlesquoy/ghq/LaTeX-Project-Manager/settings/config.json")
# print(SettingsClass.GetClassList(test))
