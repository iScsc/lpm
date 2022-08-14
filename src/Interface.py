# -*- coding: utf-8 -*-
import os
import ProjectClass
import SettingsClass
import pathlib
from rich.prompt import Prompt
from rich.prompt import Confirm
import rich
import art

# TODO: use Console class from rich lib

# Parameters :
SettingsLaunch = SettingsClass.Settings(r"/home/nlesquoy/ghq/github.com/LaTeX-Project-Manager/settings/config.json") # Initialize settings -> TODO: create a function to find this file automatically
default_path = r"/home/nlesquoy/ghq/github.com/LaTeX-Project-Manager/test"

rich.print("[bold magenta]{0}[/bold magenta]".format(art.text2art("> LPM <")))
action = Prompt.ask("What should I do ?", choices=["create","delete"], default="create")
if action == "create":
    PathToDir = Prompt.ask("Where should I create the new project ?",default=default_path)
    path = pathlib.Path(PathToDir)
    if isinstance(path,pathlib.PurePath):
        ProjectName = Prompt.ask("How should I name it ?",default="test")
        LaTeXClass = Prompt.ask("Which LaTeX document class should be used ?",choices=SettingsClass.Settings.GetClassList(SettingsClass.SettingsLaunch),default="standard")
        launch = Confirm.ask("Do you want to launch the generation of the new project ?")
        if launch:
            NewProject = ProjectClass.Project(ProjectName,PathToDir,LaTeXClass)
            ProjectClass.Project.CreateProject(NewProject)
        else:
            rich.print("[bold red]>>> Emergency stop - Nothing was generated ! <<<[/bold red]")
elif action == "delete":
    PathToDir = Prompt.ask("Where is the target ?",default=default_path)
    ProjectName = Prompt.ask("What's its name ?",default="test")
    execute = Confirm.ask("Do you really want to delete this project ?",default="n")
    if execute:
        try:
            ProjectClass.Project.RemoveProject(ProjectClass.Project(ProjectName,PathToDir,"standard"))
        except:
            print("[bold red]>>> Something went wrong <<<[/bold red]")
    else:
        rich.print("[bold red]>>> Emergency stop - Nothing was deleted ! <<<[/bold red]")
else:
    rich.print("[italic blue]I have nothing to do ![/italic blue]")