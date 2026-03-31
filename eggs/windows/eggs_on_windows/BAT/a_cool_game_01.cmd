@echo off
color 7

:menu
cls
echo Hey! Welcome to the game!
echo 1) Start
echo 2) How to play
echo 3) Exit
set /p number=
if "%number%" == "1" goto level0
if "%number%" == "2" goto help
if "%number%" == "3" goto exit
goto menu

:help
cls
echo Press the number of the answer then hit enter.
echo go back? (y/n)
set /p menu=
if "%menu%" == "y" goto menu
if "%menu%" == "n" goto exit
goto help

:exit
echo Thanks for playing!
timeout 5
exit

:die
cls
echo Ya Die!
echo Ya Die!
echo Ya Die!
echo Ya Die!
echo Ya Die!
pause >nul
goto menu

:level0
cls
echo You're awake to find yourself in a dark room. What do you do?
echo 1) Why?
echo 2) Sleep
echo 3) Find Light Switch
echo 4) Go North
set /p answer0=
if "%answer0%" == "1" goto level1
if "%answer0%" == "2" goto level2
if "%answer0%" == "3" goto level3
if "%answer0%" == "4" goto level4
goto level0

:level1
cls
echo WHY? Because the script says so!
echo The darkness is offended by your questioning.
echo 1) Apologize
echo 2) Ask "Why?" again
set /p answer1=
if "%answer1%" == "1" goto level0
if "%answer1%" == "2" goto die
goto level1

:level2
cls
echo You sleep and when you wake up
echo You're awake to find yourself in a dark room. What do you do?
echo 1) Sleep More
echo 2) Check Pockets
echo 3) Czech Pockets
echo 4) Open Pokedex
set /p answer2=
if "%answer2%" == "1" goto level21
if "%answer2%" == "2" goto level22
if "%answer2%" == "3" goto level23
if "%answer2%" == "4" goto level24
goto level2

:level21
cls
echo You sleep for 100 years. 
echo You wake up and find you are now a skeleton. 
echo Skeletons don't have muscles to move with.
pause
goto die

:level22
cls
echo You find a lint ball and a single AAA battery.
echo 1) Eat the lint
echo 2) Put battery in mouth
echo 3) Throw battery into the darkness
set /p answer22=
if "%answer22%" == "1" goto die
if "%answer22%" == "2" goto level313
if "%answer22%" == "3" goto level223
goto level22

:level223
cls
echo You hear a "clink" followed by a very angry "OW!"
echo 1) Say sorry
echo 2) Run South
set /p answer223=
if "%answer223%" == "1" goto level0
if "%answer223%" == "2" goto level5
goto level223

:level23
cls
echo You reach into your pockets and find the entire city of Prague.
echo The geographic scale of a European capital inside your trousers
echo crushes your lower half instantly.
pause
goto die

:level24
cls
echo You open your Pokedex. It glows!
echo You see a Grimer in the corner looking hungry.
echo 1) Throw PokeBall
echo 2) Use Flash
echo 3) Run away
set /p answer24=
if "%answer24%" == "1" goto die
if "%answer24%" == "2" goto level3
if "%answer24%" == "3" goto level4
goto level24

:level3
cls
echo How will you find the light switch? You're in a dark room.
echo You need a light switch to see. Do you see?
echo 1) I see
echo 2) I don't see
set /p answer3=
if "%answer3%" == "1" goto level31
if "%answer3%" == "2" goto level32
goto level3

:level31
cls
echo No you don't see! You're in a dark room!
echo 1) Touch Wall
echo 2) Jump
echo 3) Lick Wall
echo 4) Ignore Wall
set /p answer31=
if "%answer31%" == "1" goto level311
if "%answer31%" == "2" goto level312
if "%answer31%" == "3" goto level313
if "%answer31%" == "4" goto level314
goto level31

:level311
cls
echo The wall is covered in wet moss. It whispers your home address.
echo 1) Whisper back
echo 2) Punch the wall
set /p answer311=
if "%answer311%" == "1" goto level6
if "%answer311%" == "2" goto die
goto level311

:level312
cls
echo You jump. The ceiling is much lower than you thought.
echo *CRACK*
pause
goto die

:level313
cls
echo You find the light switch! But you used your tongue.
echo 1000 volts of electricity flies up and fries your face off.
pause
goto die

:level314
cls
echo You ignore the wall. The wall feels neglected and falls on you.
pause
goto die

:level32
cls
echo We know. That is why you need to:
echo 1) Find Light Switch
set /p answer32=
if "%answer32%" == "1" goto level3
goto level32

:level4
cls
echo You head North. You walk into a giant industrial fan.
echo You are now confetti.
pause
goto die

:level5
cls
echo You run South and trip over a very small, very expensive vase.
echo The ghost of an interior decorator appears and screams.
echo 1) Apologize for the vase
echo 2) Ask if it has a light switch
set /p answer5=
if "%answer5%" == "1" goto level0
if "%answer5%" == "2" goto level6
goto level5

:level6
cls
echo "Fine!" the voice booms. A door opens, flooding the room with light.
echo You see a giant pile of plastic starfish and a single Exit door.
echo 1) Take a starfish
echo 2) Walk out the door
echo 3) Stay in the Dark Room
set /p answer6=
if "%answer6%" == "1" goto level_win
if "%answer6%" == "2" goto level_win
if "%answer6%" == "3" goto level0
goto level6

:level_win
cls
echo YOU ESCAPED THE DARK ROOM!
echo You win a plastic starfish and a feeling of mild confusion.
echo WELL DONE DARREN!
pause
goto menu
