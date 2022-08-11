# -*- coding: utf-8 -*-
import os # Pour la manipulation des dossiers
import shutil # Pour la manipulation des fichiers
import traceback # Pour la gestion des erreurs
import SettingsClass
import InteractClass

class Project:
    SettingsInit = SettingsClass.Settings(r"/home/nlesquoy/ghq/LaTeX-Project-Manager/settings/config.json")
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
    
    def CreateProject(self,images=True,pptx=False):
        if Project.CheckClass(self):
        # utiliser la fonction pour checker si packages.sty ou bristol sont utilisés,
            InteractClass.MakeFolder(self.WorkingDir,self.ProjectName)
            DepList = SettingsClass.Settings.GetClassDep(Project.SettingsInit,self.LaTeXClass)
            for dep in DepList:
                InteractClass.CopyTeX(self.WorkingDir,dep,self.ProjectName,Project.PathToSource)
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
        else:
            raise("No project was generated.")
        
    def RemoveProject(self):
        """
        Delete project from folder
        """
        DelPath = os.path.join(self.WorkingDir,self.ProjectName)
        try:
            shutil.rmtree(DelPath)
        except:
            traceback.print_exc()
    

NewProject = Project("Test 1","/home/nlesquoy/ghq/LaTeX-Project-Manager/test","standard")
Project.CreateProject(NewProject,True,False)