# -*- coding: utf-8 -*-
import os
import shutil
import traceback
import Settings
import Interact

class Project:
    """This a class to define the properties of a LaTeX project.
    It relies on functions defined in :class:`SettingsClass.Settings`
    and :file:`InteractFunc.py`.

    :param ProjectName: Name of the project that will be treated.
    :type ProjectName: str
    :param WorkingDir: Path to the folder where the project is located or where
    it will be created
    :type WorkingDir: str
    :param LaTeXClass: Class associated with the `main` file of the project. It must be
    a supported class (ie detailled in `settings.json`), checks are done to verify that.
    :type LaTeXClass: str
    """
    with open("app.cfg","r") as config:
        data = config.readlines()
        config.close()
    
    SettingsInit = Settings.Settings(data[0].rstrip("\n"))
    ClassList = Settings.Settings.GetClassList(SettingsInit)
    PathToSource = Settings.Settings.GetPathToSource(SettingsInit)

    def __init__(self,ProjectName,WorkingDir,LaTeXClass):
        """Constructor method.
        """
        self.ProjectName = ProjectName
        self.WorkingDir = WorkingDir
        self.LaTeXClass = LaTeXClass
    
    def CheckClass(self)->bool:
        """Check if `LaTeXClass` is a supported LaTeX document class.

        :return: True if it is a supported class, false if not.
        :rtype: bool
        """
        if self.LaTeXClass not in Project.ClassList:
            return False
        else:
            return True
    
    def CheckInit(self)->bool:
        """Check if the project can be initialized in the folder specified in
        :class:`Project.WorkingDir` and if the LaTeX dependencies detailled in
        `settings.json` are correct by searching in the main TeX file for
        correct include statements.

        :return: True if the project can be safely initialized, False if not.
        :rtype: bool
        """
        Interact.MakeFolder(self.WorkingDir,self.ProjectName)
        return os.access(Project.PathToSource,os.W_OK | os.X_OK) and Project.CheckClass(self) and \
        Settings.Settings.CheckDep(Project.SettingsInit,self.LaTeXClass)

    def CreateProject(self,images=True,pptx=False):
        """Create of project according to the information given in
        :class:`ProjectClass.Project`.

        :param images: Create an `images` folder, defaults to True
        :type images: bool, optional
        :param pptx: Create a `.pptx` file inside the `images` folder to create figures
        - currently not implemented, defaults to False
        :type pptx: bool, optional
        """
        if Project.CheckInit(self):
        # utiliser la fonction pour checker si packages.sty ou bristol sont utilisés,
            DepList = Settings.Settings.GetClassDep(Project.SettingsInit,self.LaTeXClass)
            for dep in DepList:
                Interact.CopyTeX(self.WorkingDir,dep,self.ProjectName,Project.PathToSource) # Copy required TeX files
            if images:
                Interact.MakeFolder(os.path.join(self.WorkingDir,self.ProjectName),"images") # Create `images` folder
            Path = os.path.join(self.WorkingDir,self.ProjectName)
            try:
                os.chdir(Path)
            except FileNotFoundError:
                print("The folder {0} does not exist.".format(Path))
            except NotADirectoryError:
                print("{0} is not a folder.".format(Path))
            except PermissionError:
                print("You do not have permission to modify {0}".format(Path))
            except:
                print("Something went wrong.")
                traceback.print_exc()
            if self.LaTeXClass == "standard":
                os.rename("standard.tex","main.tex")
            if self.LaTeXClass == "beamer":
                os.rename("beamer.tex","main.tex")
            # Initialize local history file
            Interact.CreateHistory(self.WorkingDir)
            # Add line corresponding to the newly created project in `history.txt`
            Interact.AddElementToHistory(self.WorkingDir,self.ProjectName)
            # Create a `local_settings.json` file. This feature is not used for now.
            Interact.CreateLocalSettings(self.WorkingDir,self.ProjectName)
        else:
            print("No project was generated. Please retry.")
        
    def RemoveProject(self):
        """Delete a specified Project. This function is likely to be moved to :file:`InteractFunc.py`
        """
        Interact.RegisterDeletion(self.WorkingDir,self.ProjectName)
        DelPath = os.path.join(self.WorkingDir,self.ProjectName)
        try:
            shutil.rmtree(DelPath)
        except:
            traceback.print_exc()