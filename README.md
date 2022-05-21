
# About

![image](https://user-images.githubusercontent.com/26779639/169642932-67bd9843-6e79-4894-b3d6-773e6d608c1d.png)
<br>
SimpleBreak is a python script that sets a break reminder at a time interval specifically for Windows 10 by using [win10toast](https://pypi.org/project/win10toast/) to call a Windows notification. It also uses the [win32api](https://pypi.org/project/pywin32/) package to detect if the computer is in an idle state.

It can be automated to run on startup. This script was originally created to be used as part of a tutorial teaching beginner scripting but is being released early prior to the tutorial's completion. 

The documentation on this project is hence written with beginners in mind and can act as a lightweight tutorial of sorts.



# Installation & Usage

Firstly, Python should either be installed through [the official website](https://www.python.org/) or through [PyCharm](https://www.jetbrains.com/pycharm/), which is a popular and industry standard [IDE (Integrated Development Environment)](https://en.wikipedia.org/wiki/Integrated_development_environment).

The dependency modules can be installed either through [`pip install`](https://docs.python.org/3/installing/index.html) or (highly recommended) through [PyCharm](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html). Consider running the project in a [virtual environment](https://docs.python.org/3/library/venv.html).

The python script `simpleBreak.py` can be run in the following ways.
The user could run the script [traditionally through command line](https://docs.python.org/3/faq/windows.html#id3). 

```
# Run in the directory that contains breakScript.py
py simpleBreak.py
```
What this does is that the `simpleBreak.py` file is being 'fed' to the Python interpreter program that was installed and so the Python program will execute code using the instructions (the `.py` script) that was written. 
 
Currently, `simpleBreak.py` looks for a file with the exact name of `settings.txt` in order to set simple settings.  The second iteration of this script may allow different configuration files to be fed at command line. 

The script uses Windows 10 dependent libraries and so will only run on Windows 10 and possibly Windows 11.

# Startup Automation

There are a few methods to automate the starting of this file that one can consider.
1. [Windows Batch File in Startup Folder](https://superuser.com/questions/954950/run-a-script-on-start-up-on-windows-10)
2. [Windows Task Scheduler](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10)

[The `.idea` folder](https://rider-support.jetbrains.com/hc/en-us/articles/207097529-What-is-the-idea-folder-)
# Dependencies 
|Package| Purpose |
|--|--|
| [Windows 10 Toast Notifications](https://github.com/jithurjacob/Windows-10-Toast-Notifications) | Calls the Windows notification toast when the break conditions are met |
| [pywin32](https://github.com/mhammond/pywin32) | Check if the Windows computer is idle |


# Further Learning
The script is quite minimalistic and so here are some ideas that can be considered to improve it in a fork for learning purposes.
1. Allow the text and icon to be read from the `settings.txt` file
2. [Allow the passing of different `settings.txt` files on startup](https://realpython.com/python-command-line-arguments/) which can allow different configuration profiles for different days, timings and moods.
3. Consider recreating the script functionality in [AutoHotKey](https://www.autohotkey.com/) using [TrayTip](https://www.autohotkey.com/docs/commands/TrayTip.htm) instead of Python 
4. Turn the script into an executable using [pyinstaller](https://datatofish.com/executable-pyinstaller/)
5. Allow a cross-platform implementation by replacing `win32api` and `Windows 10 Toast Notification` dependencies to use a different gui, like for example [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)
