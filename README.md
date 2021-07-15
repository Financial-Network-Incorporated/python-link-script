# python-link-script

A python script to scan library peer dependencies and link them to parent project.

## Setup

1. Clone repository
2. Open your favorite text editor and paste the following text inside of it, replacing the path with the path to your ubuntu executable (usually located in "D:\Users\your_login_name\ubuntu\"):

```
@echo off
color b

:main
cls
D:\<PATH_TO_YOUR_UBUNTU_EXECUTABLE>.exe run python3 link.py
echo.
echo ---------------------------------------------------------------------------------
echo Python script has exited. Press any button to restart or just close this window.
pause >nul
goto main
```

3.  Save the file to the same directory as the python file and save as run.bat (.bat file extension is important here. You may need to select 'any' for the file type dropdown.)
    - If you prefer, you can place the `link.py` and `run.bat` files in your directory holding all your repositories, and create a shortcut to `run.bat`.
    - When running the script for the first time, a config file will be created. There, you can enter the path directory plainly where your repositories are stored and the script can run from another location.
4.  Open an instance of WSL and ensure both **python3** and **yarn** are installed. You can do this by typing `python3 -V` and `yarn -V`. If a version is not listed, follow the installation instructions here: [python](https://docs.python-guide.org/starting/install3/linux/) and [yarn](https://yarnpkg.com/getting-started/install).
