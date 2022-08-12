# -*- coding: utf-8 -*-
import ProjectClass
import pathlib

while True:
    try:
        action = input("Action ? [create, delete] ")
        if action == "create":
            PathToDir = str(input("Path to traget folder ? "))
            path = pathlib.Path(PathToDir)
            if isinstance(path,pathlib.PurePath):
                ProjectName = str(input("Project name ? "))
                LaTeXClass = str(input("Document class ? "))
                NewProject = ProjectClass.Project(ProjectName,PathToDir,LaTeXClass)
                ProjectClass.Project.CreateProject(NewProject)
            else:
                raise("This is not a path !")
        elif action == "delete":
            PathToDir = str(input("Path to target folder ?"))
            ProjectName = str(input("Project name ? "))
            try:
                ProjectClass.Project.RemoveProject(ProjectClass.Project(ProjectName,PathToDir,"standard"))
            except:
                raise("Something went wrong")
        else:
            break
    except:
        break
