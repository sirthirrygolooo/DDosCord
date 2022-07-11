@echo off

REM nomme la fenêtre 
title DDoSCord Lancher 
cls

:MAIN
cls
echo. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo. + Press S to start, V for checking python version (3.9 is good) and avoid some compatibilities            +
echo. + problems, I to install requirements and E to exit...                                                    +
echo. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


choice /c SVIE /m ">>>"
IF ERRORLEVEL 4 GOTO END
IF ERRORLEVEL 3 GOTO INS
IF ERRORLEVEL 2 GOTO VER
IF ERRORLEVEL 1 GOTO START 


:START
python main.py
exit


:VER
cls
python --version
pause
GOTO MAIN 

:INS 
pip install -r requirements.txt
pause
GOTO MAIN

:END
CHOICE /c YN /m "Voulez vous vraiment quitter ? "

REM confirmation du choix
IF ERRORLEVEL 2 GOTO MAIN
IF ERRORLEVEL 1 exit
exit
