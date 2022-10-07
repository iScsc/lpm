# LaTeX Project-Manager
*A project-manager tool to speed up creation process for note-taking*
---
## **Description**
LPM (LaTeX Project Manager) is a simple project manager to generate a new LaTeX project from a template.

## Installation

*Requirements - see `requirements.txt` for more information*

How to install LPM ?
1) clone the project on your system with `git clone https://github.com/iScsc/lpm.git`
2) `cd` into the project directory and modify the `path_to_source` field in the `settings/config.json` file with the absolute path to your LaTeX sources.
3) in the same file, describe the dependencies of your custom classes and documents according to this nomenclature :
```json
"latex_class":[
    {
    "name":"classname",
    "dependencies":[
        "mypackage.sty",
        "packages.tex",
        "main.tex",
        "classname.cls"
        ]
    }
]
```

*Remarks - Note that LPM will create by default a new project in the same directory as the git repository. You can change this behavior by editing the second line of the `src/app.cfg` config file with the absolute (or relative) path to the directory of your choice.*

## How to use LPM ?

To use LPM, simply run the `src/main.py` file in your terminal. A text interface will be created. You juste have to follow the instructions !

## Contribute

If you find a bug, or if you want to request a new feature, feel free to open a new issue at https://github.com/iScsc/lpm/issues. You can also open a pull request at https://github.com/iScsc/lpm/pull.
