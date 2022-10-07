# Standard Python Libraries
import sys
import os
import pathlib
import shutil
import time
import traceback
import mmap
import json

# Special Libraries
import art
import rich

# 'rich' libraries
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.markdown import Markdown
from rich.console import Console

# Initialization
with open("src/app.cfg", "r") as config_file:
    config = config_file.readlines()
    config_file.close()

path_to_json = config[0].rstrip("\n")
default_dir = config[1]


class Interact:
    def make_folder(path_to_dir: pathlib.PosixPath, folder_name: str) -> None:
        """Creates a folder in the specified directory."""
        try:
            pathlib.PosixPath(path_to_dir, folder_name).mkdir(parents=True)
            print("Directory {0} created.".format(folder_name))
        except FileExistsError:
            print("Directory {0} already exists.".format(folder_name))

    def copy_file(
        working_dir: pathlib.PosixPath,
        path_to_source: pathlib.PosixPath,
        file_name: str,
        folder_name: str,
    ) -> None:
        """Copies a file."""
        original = pathlib.PosixPath(path_to_source) / file_name
        target = pathlib.PosixPath(working_dir)/ folder_name / file_name
        shutil.copyfile(original, target)

    def search_file(search_word: str, file_name: str) -> bool:
        """Checks if a word is inside a text file or not."""
        with open(file_name, "rb", 0) as file, mmap.mmap(
            file.fileno(), 0, access=mmap.ACCESS_READ
        ) as s:
            if s.find(bytes(search_word, encoding="utf-8")) != -1:
                file.close()
                return True
            else:
                file.close()
                return False

    def create_history(path_to_dir: pathlib.PosixPath) -> bool:
        """Initializes the `history.txt` file in a new directory."""
        path_to_history = pathlib.PosixPath(path_to_dir, "history.txt")
        if not path_to_history.exists():
            with open(path_to_history, "x") as history:
                history.write(art.text2art("history"))
                history.write(
                    ">>> Initializing 'history.txt' for this repository ...\n"
                )
                history.write(
                    ">>> Date of creation = {0}\n".format(
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    )
                )
                history.write(">>> Ready to go !\n")
                history.write(
                    "###########################################################\n"
                )
                history.close()
            return True
        else:
            return False

    def add_element_to_history(
        path_to_dir: pathlib.PosixPath, project_name: str
    ) -> bool:
        """Add a line to the `history.txt` file when creating a new file."""
        path_to_history = pathlib.PosixPath(path_to_dir, "history.txt")
        if os.path.exists(path_to_history):
            with open(path_to_history, "a") as history:
                history.write(
                    ">>> Created {project} on {date}.\n".format(
                        project=project_name,
                        date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    )
                )
                history.close()
            return True
        else:
            return False

    def register_deletion(path_to_working_dir, project_name) -> bool:
        """Takes note of the deletion of a project in `history.txt`."""
        path_to_history = pathlib.PosixPath(path_to_working_dir, "history.txt")
        if path_to_history.exists():
            with open(path_to_history, "a") as history:
                history.write(
                    ">>> Deleted {project} on {date}.\n".format(
                        project=project_name,
                        date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    )
                )
                history.close()
            return True
        else:
            return False


class Settings:
    """A simple class to handle global and local settings."""

    def get_settings(path_to_json: pathlib.PosixPath) -> dict:
        """Loads the global settings from :file:'settings.json'"""
        with open(path_to_json, "r") as ReadFile:
            settings_dict = json.load(ReadFile)
        return settings_dict

    def get_path_to_source(path_to_json: pathlib.PosixPath) -> pathlib.PosixPath:
        """Get the path to LaTeX source files from the
        'path_to_source' field in 'settings.json'.
        """
        return Settings.get_settings(path_to_json)["path_to_source"]

    def get_class_list(path_to_json: pathlib.PosixPath) -> list[str]:
        """Get the list of supported LaTeX document classes."""
        settings_dict = Settings.get_settings(path_to_json)
        return [
            settings_dict["latex_class"][i]["name"]
            for i in range(len(settings_dict["latex_class"]))
        ]

    def get_class_dep(path_to_json: pathlib.PosixPath, class_name: str) -> list[str]:
        """Get all LaTeX dependencies for a specified supported LaTeX class."""
        settings_dict = Settings.get_settings(path_to_json)
        class_list = Settings.get_class_list(path_to_json)
        return settings_dict["latex_class"][class_list.index(class_name)][
            "dependencies"
        ]

    def check_dep(path_to_json: pathlib.PosixPath, class_name: str) -> bool:
        """Checks if all dependencies are correct, ie if the files specified in 'settings.json' are called
        inside the main LaTeX document.
        """
        settings_dict = Settings.get_settings(path_to_json)
        class_list = Settings.get_class_list(path_to_json)
        dep_list = settings_dict["latex_class"][class_list.index(class_name)][
            "dependencies"
        ]
        class_file = "".join([class_name, ".tex"])  # main LaTeX file.
        path = pathlib.PosixPath(Settings.get_path_to_source(path_to_json), class_file)
        for dep in dep_list:
            if dep != class_file and not Interact.search_file(pathlib.PosixPath(dep).stem, path):
                return False
        return True


class Project:
    """This a class to define the properties of a LaTeX project."""

    class_list = Settings.get_class_list(path_to_json)
    path_to_source = Settings.get_path_to_source(path_to_json)

    def __init__(self, project_name, working_dir, latex_class):
        """Constructor method."""
        self.project_name = project_name
        self.working_dir = working_dir
        self.latex_class = latex_class

    def check_class(self) -> bool:
        """Check if 'latex_class' is a supported LaTeX document class."""
        if self.latex_class not in Project.class_list:
            return False
        else:
            return True

    def check_init(self) -> bool:
        """Check if the project can be initialized in the folder specified in
        the field 'working_dir' and if the LaTeX dependencies detailled in
        'settings.json' are correct by searching in the main TeX file for
        correct include statements.
        """
        Interact.make_folder(self.working_dir, self.project_name)
        return (
            os.access(Project.path_to_source, os.W_OK | os.X_OK)
            and Project.check_class(self)
            and Settings.check_dep(path_to_json, self.latex_class)
        )

    def create_project(self, images=True):
        """Create of project according to the information given in 'Project.Project'."""
        if Project.check_init(self):
            dep_list = Settings.get_class_dep(path_to_json, self.latex_class)
            for dep in dep_list:
                Interact.copy_file(self.working_dir,Project.path_to_source,dep,self.project_name) # Copy required TeX files
            if images:
                Interact.make_folder(
                    os.path.join(self.working_dir, self.project_name), "images"
                )  # Create `images` folder
            Path = pathlib.PosixPath(self.working_dir, self.project_name)
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
            if self.latex_class == "standard":
                os.rename("standard.tex", "main.tex")
            if self.latex_class == "beamer":
                os.rename("beamer.tex", "main.tex")
            # Initialize local history file
            # Interact.create_history(self.working_dir)
            # Add line corresponding to the newly created project in `history.txt`
            # Interact.add_element_to_history(self.working_dir, self.project_name)
        else:
            print("No project was generated. Please retry.")

    def remove_project(self):
        """Delete a specified Project."""
        Interact.register_deletion(self.working_dir, self.project_name)
        del_path = pathlib.Path(self.working_dir, self.project_name)
        try:
            shutil.rmtree(del_path)
        except:
            traceback.print_exc()

# Interface

rich.print("[bold magenta]{0}[/bold magenta]".format(art.text2art("> LPM <")))
action = Prompt.ask("What should I do ?", choices=["create","delete","inspect","configure","name","quit"], default="create")
if action == "create":
    PathToDir = Prompt.ask("Where should I create the new project ?",default=default_dir)
    path = pathlib.Path(PathToDir)
    if isinstance(path,pathlib.PurePath):
        ProjectName = Prompt.ask("How should I name it ?",default="test")
        LaTeXClass = Prompt.ask("Which LaTeX document class should be used ?",choices=Settings.get_class_list(path_to_json),default="standard")
        ImagesFolder = Confirm.ask("Do you want to create a folder for images ?",default=False)
        launch = Confirm.ask("Do you want to launch the generation of the new project ?",default=True)
        if launch:
            NewProject = Project(ProjectName,PathToDir,LaTeXClass)
            Project.create_project(NewProject,images=ImagesFolder)
        else:
            rich.print("[bold red]>>> Emergency stop - Nothing was generated ! <<<[/bold red]")
elif action == "delete":
    PathToDir = Prompt.ask("Where is the target ?",default=default_dir)
    ProjectName = Prompt.ask("What's its name ?",default="test")
    execute = Confirm.ask("Do you really want to delete this project ?",default=False)
    if execute:
        try:
            Project.remove_project(Project(ProjectName,PathToDir,"standard"))
        except:
            rich.print("[bold red]>>> Something went wrong <<<[/bold red]")
    else:
        rich.print("[bold red]>>> Emergency stop - Nothing was deleted ! <<<[/bold red]")
elif action == "inspect":
    seeGlobJSON = Confirm.ask("Do you want to see the global configuration file ?",default=True)
    if seeGlobJSON:
        config = Settings.get_settings(path_to_json)
        rich.print_json(data=config)
    else:
        pass
elif action == "configure":
    try:
        with open("app.cfg","r",newline='') as config:
            data = config.readlines()
            PathToConfig = data[0].rstrip("\n")
            default_dir = data[1]
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
else:
    rich.print("[italic blue]I have nothing to do ![/italic blue]")