@echo off

REM nomme la fenêtre 
title DDoSCord Lancher 
cls

REM definition de la fonction principale  

:MAIN
cls
echo. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo. + Veuillez presser S pour lancer, V pour verifier votre version de python (3.9 idealement) et             +
echo. + eviter des problemes de compatibilite, I pour installer les bibliotheques requises et E pour quitter... +
echo. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

REM choix de l'utilisateur avec redirection vers la fonction qui correspond a l'action voulue

choice /c SVIE /m ">>>"
IF ERRORLEVEL 4 GOTO END
IF ERRORLEVEL 3 GOTO INS
IF ERRORLEVEL 2 GOTO VER
IF ERRORLEVEL 1 GOTO START 

REM fonction qui lance juste le programme
:START
python main.py
exit

REM montre à l'utilisateur sa version de python
:VER
cls
python --version
pause
GOTO MAIN 

REM Installe les bibliothèques requises contenues dans le fichier requirements.txt avec pip
:INS 
pip install -r requirements.txt
pause
GOTO MAIN

REM Fonction qui permet de quitter le programme
:END
CHOICE /c YN /m "Voulez vous vraiment quitter ? "

REM confirmation du choix
IF ERRORLEVEL 2 GOTO MAIN
IF ERRORLEVEL 1 exit
exit
