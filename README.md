# python-link-script

A python script to scan library peer dependencies and link them to parent project.

## Setup

1. Clone repository
2.
3. Open your favorite text editor and paste the following text inside of it, replacing "your_login_name" with your login name:

```
@echo off
color b

:main
cls
D:\Users\your_login_name\ubuntu\ubuntu2004.exe run python3 link.py
echo.
echo ---------------------------------------------------------------------------------
echo Python script has exited. Press any button to restart or just close this window.
pause >nul
goto main
```

4.  Save the file as run.bat (.bat file extension is important here. You may need to select 'any' for the file type dropdown.
5.  Open an instance of WSL and ensure both **python3** and **yarn** are installed. You can do this by typing `python3 -V` and `yarn -V`. If a version is not listed, follow the installation instructions here: [python](https://docs.python-guide.org/starting/install3/linux/) and [yarn](https://yarnpkg.com/getting-started/install).

6.  If you prefer, you can place the `link.py` and `run.bat` files in your directory holding all your repositories, and create a shortcut to `run.bat`.

## Additional Information

- When running the script for the first time, a config file will be created. There, you can enter the _WSL_ directory where your repositories are stored and the script can run from another location.
