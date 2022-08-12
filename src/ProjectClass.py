# -*- coding: utf-8 -*-
import os # Pour la manipulation des dossiers
import shutil # Pour la manipulation des fichiers
import traceback # Pour la gestion des erreurs
import SettingsClass
import InteractFunc

class Project:
    SettingsInit = SettingsClass.SettingsLaunch
    ClassList = SettingsClass.Settings.GetClassList(SettingsInit)
    PathToSource = SettingsClass.Settings.GetPathToSource(SettingsInit)

    def __init__(self,ProjectName,WorkingDir,LaTeXClass):
        self.ProjectName = ProjectName
        self.WorkingDir = WorkingDir
        self.LaTeXClass = LaTeXClass
    
    def CheckClass(self):
        if self.LaTeXClass not in Project.ClassList:
            return False
        else:
            return True
    
    def CheckInit(self):
        """Check if the project can be initialized + make folder"""
        InteractFunc.MakeFolder(self.WorkingDir,self.ProjectName)
        return os.access(Project.PathToSource,os.W_OK | os.X_OK) and Project.CheckClass(self) and \
        SettingsClass.Settings.CheckDep(Project.SettingsInit,self.LaTeXClass)

    def CreateProject(self,images=True,pptx=False):
        if Project.CheckInit(self):
        # utiliser la fonction pour checker si packages.sty ou bristol sont utilisés,
            DepList = SettingsClass.Settings.GetClassDep(Project.SettingsInit,self.LaTeXClass)
            for dep in DepList:
                InteractFunc.CopyTeX(self.WorkingDir,dep,self.ProjectName,Project.PathToSource)
            if images:
                InteractFunc.MakeFolder(os.path.join(self.WorkingDir,self.ProjectName),"images")
            Path = os.path.join(self.WorkingDir,self.ProjectName)
            try:
                os.chdir(Path)
            except FileNotFoundError:
                print("Le dossier {0} n'existe pas.".format(Path))
            except NotADirectoryError:
                print("{0} n'est pas un dossier.".format(Path))
            except PermissionError:
                print("Vous n'avez pas la permission de changer {0}".format(Path))
            except:
                print("Something went wrong")
            if self.CheckClass == "standard":
                os.rename("standard.tex","main.tex")
            if self.CheckClass == "beamer":
                os.rename("beamer.tex","main.tex")
            InteractFunc.CreateHistory(self.WorkingDir)
            InteractFunc.AddElementToHistory(self.WorkingDir,self.ProjectName)
            InteractFunc.CreateLocalSettings(self.WorkingDir,self.ProjectName)
        else:
            raise("No project was generated.")
        
    def RemoveProject(self):
        """
        Delete project from folder
        """
        InteractFunc.RegisterDeletion(self.WorkingDir,self.ProjectName)
        DelPath = os.path.join(self.WorkingDir,self.ProjectName)
        try:
            shutil.rmtree(DelPath)
        except:
            traceback.print_exc()
    

# NewProject = Project("Test 1","/home/nlesquoy/ghq/LaTeX-Project-Manager/test","standard")
# # Project.RemoveProject(NewProject)
# # print(Project.CheckInit(NewProject))
# Project.CreateProject(NewProject,True,False)