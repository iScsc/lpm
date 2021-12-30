# -*- coding: utf-8 -*-
# Packages used in this file :
import os
import subprocess
import shutil
import jinja2 # Template manager
##########################################
# CORE functions
##########################################

# ========================================
# Test section
# ========================================
"""
'open' built-in function options :
'r'- open for reading (default);
'w'- open for writing, truncating the file first = Can be used for creation of file;
'x'- open for exclusive creation, failing if the file already exists;
'a'- open for writing, appending to the end of file if it exists = Can be used for file modifications;
'b'- binary mode;
't'- text mode (default);
'+'- open for updating (reading and writing);
"""
def writing_tex(filename):
    """
    Function used for test purposes : write (and overwrite if the file exists)
    latex-code given in a triple quote string = no need to use '\n' since it is
    already taken in account inside the triple quote string.
    """
    with open(filename,'w') as file:
        file.write(
"""\\documentclass[a4paper,12pt]{article}
\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage[french]{babel}
\\usepackage{lmodern}
\\begin{document}
Hello World
\\end{document}"""
        )
        file.close()
writing_tex("test.tex")

def modifying_tex(filename):
    """
    Function used for test purposes :
    """
    with open(filename,'a') as file:
        file.write(
"""\n\\begin{equation*}
\\bar{\\mathbb{R}} = \\mathbb{R}\\cup\\lbrace \\pm\\infty\\rbrace
\\end{equation*}
"""
        )
        file.close()
# modifying_tex("test.tex")

def search_index_tex(filename):
    """
    Function used for test purposes
    Some informations :
    >>> filin = open("zoo.txt", "r")
    >>> filin
    <_io.TextIOWrapper name='zoo.txt' mode='r' encoding='UTF-8'>
    >>> filin.readlines()
    ['girafe\n', 'tigre\n', 'singe\n', 'souris\n']
    >>> filin.close()
    """
    def find_bdoc(content):
        """
        content = list of strings (content of a .tex file) as output of f.readlines()
        """
        list_index = []
        for i in range(len(content)):
            if content[i] == "\\begin{document}\n" or "\\end{document}\n":
                list_index.append(i)
        return list_index
    with open(filename,'r') as file:
        content = file.readlines()
        index_doc = search_index_tex(content)
    return index_doc
# search_index_tex("test.tex")
def make_dummy(fname,text):
    with open(fname,'w') as file:
        file.write(text)

def make_folder(fdname):
    folder_name = fdname
    folder_path = "C:\\Users\\Lorinfo\\Documents\\GitHub\\LaTeX-Project-Manager\\{name}".format(name=folder_name)
    try:
        os.makedirs(folder_path)    
        print("Directory ",folder_name," Created ")
    except FileExistsError:
        print("Directory ",folder_name," already exists")

print(os.listdir("C:\\Users\\Lorinfo\\Documents\\GitHub\\LaTeX-Project-Manager"))