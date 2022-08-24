# LaTeX Project-Manager
*A project-manager tool to speed up creation process for note-taking*
---
## **Description**
LPM (LaTeX Project Manager) is a simple project manager to generate a new LaTeX project from a template.

## Requirements
- Python 3.9 at least
- `art` library (`python3 -m pip install art`)

Tested on *Ubuntu 22.04 LTS*. 
  
## Installation
```
git clone https://github.com/iScsc/LaTeX-Project-Manager.git
cd ./LaTeX-Project-Manager/settings
```
- Change the "PathToSource" with the *absolute* path to the `source_TeX` folder in the `/settings/config.json` file.
```
cd ../src
```
- Change the path with the *absolute* path to the `config.json` file. 
```python
SettingsLaunch = Settings(r"/home/nlesquoy/ghq/LaTeX-Project-Manager/settings/config.json")
```
- Open your terminal and launch the `Interface.py` script.
```python
>>> python3 Interface.py
```
The prompt should be displayed in your terminal.
