# Settings.py - global variables
import json
import InteractFunc
import os

class Settings:
    """A simple class to handle global and local settings.
    """
    def __init__(self,PathToJSON):
        """An object to group settings related files.

        :param PathToJSON: Path to the global `settings.json` file.
        :type PathToJSON: str
        """
        self.PathToJSON = PathToJSON
    
    def GetSettings(self)->dict:
        """Loads the global settings from :file:`settings.json`
        :return: _description_
        :rtype: _type_
        """
        with open(self.PathToJSON,"r") as ReadFile:
            SettingsDict = json.load(ReadFile)
        return SettingsDict
    
    def GetPathToSource(self):
        """Get the path to LaTeX source files from the
        "PathToSource" field in :file:`settings.json`.

        :return: Path to the folder containing LaTeX source files required to generate a new project.
        :rtype: str
        """
        return Settings.GetSettings(self)["PathToSource"]
    
    def GetClassList(self)->list:
        """Get the list of supported LaTeX document classes.

        :return: a list of all supported document classes specified in :file:`settings.json`
        :rtype: list
        """
        SettingsDict = Settings.GetSettings(self)
        return [SettingsDict["latex_class"][i]["name"] for i in range(len(SettingsDict["latex_class"]))]
    
    def GetClassDep(self,ClassName)->list:
        """Get all LaTeX dependencies for a specified supported LaTeX class.

        :param ClassName: name of the class. This parameter must be the same as those specified in :file:`settings.json`.
        :type ClassName: str
        :return: a list of dependencies (as file names with extensions stored as strings.)
        :rtype: list[str]
        """
        SettingsDict = Settings.GetSettings(self)
        ClassList = [SettingsDict["latex_class"][i]["name"] for i in range(len(SettingsDict["latex_class"]))]
        return SettingsDict["latex_class"][ClassList.index(ClassName)]["dependencies"]
    
    def CheckDep(self,ClassName):
        """Checks if all dependencies are correct, ie if the files specified in :file:`settings.json` are called 
        inside the main LaTeX document.

        :param ClassName: target LaTeX class. It must be a supported LaTeX Class
        :type ClassName: _type_
        :return: _description_
        :rtype: _type_
        """
        SettingsDict = Settings.GetSettings(self)
        ClassList = [SettingsDict["latex_class"][i]["name"] for i in range(len(SettingsDict["latex_class"]))]
        DepList = SettingsDict["latex_class"][ClassList.index(ClassName)]["dependencies"]
        ClassFile = "".join([ClassName,".tex"]) # main LaTeX file.
        Path = os.path.join(Settings.GetPathToSource(self),ClassFile)
        for dep in DepList:
            if dep != ClassFile:
                FileName,FileExtension = dep.split('.')
                Result = InteractFunc.SearchTeX(FileName.removesuffix(FileExtension),Path) # TODO: Change removesuffix for > 3.9 solution
                if not Result:
                    return False
        return True

SettingsLaunch = Settings(r"/home/nlesquoy/ghq/LaTeX-Project-Manager/settings/config.json") # Initialize settings -> TODO: move this to the project + create a function
