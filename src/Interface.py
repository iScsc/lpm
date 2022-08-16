# -*- coding: utf-8 -*-
import sys
import os
import ProjectClass
import SettingsClass
import SortFunc
import InteractFunc
import pathlib
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.markdown import Markdown
import rich
import art

# TODO: use Console class from rich lib

def SettingsInit(PathToJSON):
    return SettingsClass.Settings(PathToJSON)

# Parameters :
# DefaultPath = r"/home/nlesquoy/ghq/github.com/LaTeX-Project-Manager/test"
with open("app.cfg","r",newline='') as config:
    data = config.readlines()
    PathToConfig = data[0].rstrip("\n")
    DefaultPath = data[1]
    config.close()

SettingsLaunch = SettingsClass.Settings(PathToConfig) # Initialize settings -> TODO: create a function to find this file automatically

rich.print("[bold magenta]{0}[/bold magenta]".format(art.text2art("> LPM <")))
action = Prompt.ask("What should I do ?", choices=["create","delete","inspect","configure","sort","save","name","quit"], default="create")
if action == "create":
    PathToDir = Prompt.ask("Where should I create the new project ?",default=DefaultPath)
    path = pathlib.Path(PathToDir)
    if isinstance(path,pathlib.PurePath):
        ProjectName = Prompt.ask("How should I name it ?",default="test")
        LaTeXClass = Prompt.ask("Which LaTeX document class should be used ?",choices=SettingsClass.Settings.GetClassList(SettingsLaunch),default="standard")
        ImagesFolder = Confirm.ask("Do you want to create a folder for images ?",default=False)
        launch = Confirm.ask("Do you want to launch the generation of the new project ?",default=True)
        if launch:
            NewProject = ProjectClass.Project(ProjectName,PathToDir,LaTeXClass)
            ProjectClass.Project.CreateProject(NewProject,images=ImagesFolder)
        else:
            rich.print("[bold red]>>> Emergency stop - Nothing was generated ! <<<[/bold red]")
elif action == "delete":
    PathToDir = Prompt.ask("Where is the target ?",default=DefaultPath)
    ProjectName = Prompt.ask("What's its name ?",default="test")
    execute = Confirm.ask("Do you really want to delete this project ?",default=False)
    if execute:
        try:
            ProjectClass.Project.RemoveProject(ProjectClass.Project(ProjectName,PathToDir,"standard"))
        except:
            rich.print("[bold red]>>> Something went wrong <<<[/bold red]")
    else:
        rich.print("[bold red]>>> Emergency stop - Nothing was deleted ! <<<[/bold red]")
elif action == "inspect":
    seeGlobJSON = Confirm.ask("Do you want to see the global configuration file ?",default=True)
    if seeGlobJSON:
        config = SettingsClass.Settings.GetSettings(SettingsLaunch)
        rich.print_json(data=config)
    else:
        pass
elif action == "configure":
    try:
        with open("app.cfg","r",newline='') as config:
            data = config.readlines()
            PathToConfig = data[0].rstrip("\n")
            DefaultPath = data[1]
            config.close()
        configure = Prompt.ask("What do you want to do ?",choices=["path/to/settings","path/to/default/folder"])
        if configure == "path/to/settings":
            new = Prompt.ask("Where are the settings ?")
            data[0] = new + "\n"
            with open("app.cfg","w") as config:
                config.writelines(data)
                config.close()
        elif configure == "path/to/default/folder":
            new = Prompt.ask("Where should I create a new project by default ?")
            data[1] = new + "\n"
            with open("app.cfg","w") as config:
                config.writelines(data)
                config.close()
        else:
            rich.print("[italic blue]I have nothing to do ![/italic blue]")
    except:
        rich.print("[bold red]>>> Something went wrong <<<[/bold red]")
elif action == "name":
    MarkDown = Prompt.ask("Which file do you want to see ?",choices=["commit.md","convention.md","../README.md"])
    with open(MarkDown,"r+") as file:
        rich.print(Markdown(file.read()))
    sys.exit(0)
elif action == "sort":
    SortTarget = Prompt.ask("Which directory do you want to clean up ?",default=DefaultPath)
    SortFunc.SortFiles(SortTarget,PathToConfig)
elif action == "save":
    dir = Prompt.ask("Where is the folder that you want to save ?",default=DefaultPath)
    os.chdir(dir)
    message = Prompt.ask("What is the message that should be used for the commit ?")
    InteractFunc.SaveProgress(message)
elif action == "quit":
    rich.print("[bold blue]Bye Bye !")
else:
    rich.print("[italic blue]I have nothing to do ![/italic blue]")