@echo off

SET PYTHON_DISTRIBUTION=C:\Users\Dumi\AppData\Local\Programs\Python\Python39\python.exe

REM get this script's directory path
set SCRIPT_PATH=%~dp0
echo Script path: %SCRIPT_PATH%
cd %SCRIPT_PATH%

REM get project's root directory (2 levels above this script's path)
set ROOT_PATH=%cd%
echo Root path: %ROOT_PATH%

echo Deleting old venv...
REM rmdir: delete directory; /S: also delete directory's content; /Q: Quiet mode, do not ask if ok to remove directory
rmdir %ROOT_PATH%\venv /S /Q

echo Building new environment...
%PYTHON_DISTRIBUTION% -m venv venv


set PYTHON_EXE=%cd%\venv\Scripts\python.exe


REM It is a good practice to use latest version of setuptools
echo Updating setuptools...
%PYTHON_EXE% -m pip install -U setuptools

echo Installing project requirements...
%PYTHON_EXE% -m pip install -r %ROOT_PATH%\requirements.txt 
