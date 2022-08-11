# Settings.py - global variables
import json

with open("/home/nlesquoy/ghq/LaTeX-Project-Manager/settings/config.json","r") as ReadFile:
    SettingsDict = json.load(ReadFile)

PathToSource = SettingsDict["PathToSource"]
ClassList = ["fiche","standard","beamer"]