# -*- coding: utf-8 -*-
# Packages used in this file :
import os
import subprocess
import shutil
import jinja2 # Template manager
##########################################
# CORE functions
##########################################
def writing_tex(filename):
    """
    Function uses for test purposes : write (and overwrite if the file exists)
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
    