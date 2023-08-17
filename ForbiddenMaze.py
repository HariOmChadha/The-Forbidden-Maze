# Author: Hari Om Chadha
# This is a maze game where the player has to solve a few riddles to get the key to the exit and then solve the maze in the given time
import time
import sys
import os
from datetime import datetime, timedelta

# these are the four different maze layouts.
# 1s are walls and 0s are the path the player can walk on
easy = [[1,1,1,1,1,1,1,1,1],
        [1,1,1,1,0,1,1,1,1],
        [1,1,0,0,0,1,0,1,1],
        [1,1,0,1,1,1,0,1,1],
        [1,1,0,0,0,0,0,1,1],
        [1,1,0,1,0,1,1,1,1],
        [1,1,0,1,0,0,0,1,1],
        [1,1,1,1,0,1,1,1,1],
        [1,1,1,1,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,1]]

medium = [[1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,0,1,1,1,1,1,1],
          [1,1,0,0,0,1,0,1,0,0,0,1,1],
          [1,1,0,1,0,1,0,1,1,1,0,1,1],
          [1,1,0,1,0,1,0,0,0,0,0,1,1],
          [1,1,0,1,1,1,1,1,1,1,0,1,1],
          [1,1,0,1,0,0,0,0,0,0,0,1,1],
          [1,1,0,1,0,1,1,1,1,1,1,1,1],
          [1,1,0,1,0,0,0,1,0,0,0,1,1],
          [1,1,0,1,1,1,0,1,1,1,0,1,1],
          [1,1,0,0,0,0,0,0,0,0,0,1,1],
          [1,1,1,1,1,1,0,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1]]

hard = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1],
        [1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1],
        [1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,1],
        [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,1,1],
        [1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,1],
        [1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,1,1],
        [1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1],
        [1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,1],
        [1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1],
        [1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
        [1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,1],
        [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1],
        [1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1],
        [1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1],
        [1,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1],
        [1,1,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1],
        [1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1],
        [1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
        [1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

veryHard = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1],
            [1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1],
            [1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1],
            [1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1],
            [1,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1],
            [1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1],
            [1,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1],
            [1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1],
            [1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1],
            [1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1],
            [1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1],
            [1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1],
            [1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1],
            [1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1],
            [1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1],
            [1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
            [1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1],
            [1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1],
            [1,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1],
            [1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1],
            [1,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
            [1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
            [1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1],
            [1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1],
            [1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1],
            [1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1],
            [1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1],
            [1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1],
            [1,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1],
            [1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1],
            [1,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1],
            [1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
            [1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1],
            [1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1],
            [1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1],
            [1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
            [1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1],
            [1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1],
            [1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

mazeDesign = easy

y = 0
x = 0
winX = 0
winY = 0
currentDirection = 0
secondsGame = 0

attempts = 0
riddle1 = False
riddle2 = False
riddle3 = False
win = False
new = True
cheats = False

up = False
left = False
down = False
right = False

userUp = up
userLeft = left
userDown = down
userRight = right

choices = "forward(w)"
directionPrint = ""
endTime = ""
name = ""

#asks the user to choose a difficulty. Recurssive if the input is invalid
#assigns the global variables their values based on the choice
def difficulty():
    global mazeDesign
    global y
    global x
    global winX
    global winY
    global currentDirection
    global secondsGame
    global attempts
    a = input("""Please pick your difficulty:
(1)Easy (recommended for beginners)
(2)Medium 
(3)Hard
(4)Very Hard (ONLY PICK IF YOU ARE A MAZE GENIUS)
""").lower()
    a.replace(" ","")
    if a == "1" or a == "easy":
        mazeDesign = easy
        y = 8
        x = 4
        winY = 1
        winX = 4
        currentDirection = 0
        secondsGame = 500
        attempts = 10
    elif a == "2" or a == "medium":
        mazeDesign = medium
        y = 11
        x = 6
        winY = 1
        winX = 6
        currentDirection = 0
        secondsGame = 600
        attempts = 8
    elif a == "3" or a == "hard":
        mazeDesign = hard
        y = 22
        x = 11
        winY = 1
        winX = 10
        currentDirection = 0
        secondsGame = 700
        attempts = 6
    elif a == "4" or a == "veryhard":
        mazeDesign = veryHard
        y = 41
        x = 22
        winY = 1
        winX = 20
        currentDirection = 0
        secondsGame = 800
        attempts = 5
    else:
        print("That's an invalid input.")
        difficulty()
    return

#prints out the entire storyline before the riddles
def start():
    global name
    name = input("Please enter your name: ").upper()
    if name == "":
        start()
        return
    difficulty()
    for i in range (50):
        print("\n")
    print(f"""
This story starts with a person named {name}. {name} is a regular human who is absolutely mediocre in every way.
{name} has no charisma, fortitude, strength, intelligence, wisdom or rizz. Like I said: MEDIOCRE
They spend their entire day doing exactly what a human with mediorce stats would do.""")
    b = input("You will have to press ENTER to continue to the next prompt everytime. Press ENTER now.\n")
    print("BUT")
    b = input()
    print(f"""
One night {name} gets a chance to change all of this and be the person they has always wanted to be.
It all starts when {name} goes to bed on the fateful night in April 2006...\n""")
    b = input
    a = [f"{name} wakes up in the middle of the night to a wisper in their ear. They see a small glimpse of someone who disappears right after",
         """
                                               ...
                                            ;::::;
                                        ;::::; :;
                                        ;:::::'   :;
                                        ;:::::;     ;.
                                    ,:::::'       ;           OOO
                                    ::::::;       ;          OOOOO
                                    ;:::::;       ;         OOOOOOOO
                                    ,;::::::;     ;'         / OOOOOOO
                                    ;:::::::::`. ,,,;.        /  / DOOOOOO
                                .';:::::::::::::::::;,     /  /     DOOOO
                                ,::::::;::::::;;;;::::;,   /  /        DOOO
                                ;`::::::`'::::::;;;::::: ,#/  /          DOOO
                                :`:::::::`;::::::;;::: ;::#  /            DOOO
                                ::`:::::::`;:::::::: ;::::# /              DOO
                                `:`:::::::`;:::::: ;::::::#/               DOO
                                :::`:::::::`;; ;:::::::::##                OO
                                ::::`:::::::`;::::::::;:::#                OO
                                `:::::`::::::::::::;'`:;::#                O
                                `:::::`::::::::;' /  / `:#
                                ::::::`:::::;'  /  /   `#
                                Internet""",
         f"{name}: Why am I in an empty field? Where am I?",
         f"Mysterious voice: AH! Looks like we have a new creature to do our tests on.",
         f"{name}: Who...What are you? Why am I here?",
         f"Mysterious voice: Will you shut up already? You know what? If you shut up I might let you leave.",
         f"{name}: WHO ARE YOU?? WHY AM I HERE?",
         f"Mysterious voice: Alright, that's it. In you go for testing you puny creature."]
    for i in a:
        print(i)
        b = input()
    for i in range(50):
        print("\n")
    print("""
                                         WELCOME TO THE

  █████▒▒█████   ██▀███   ▄▄▄▄    ██▓▓█████▄ ▓█████▄ ▓█████  ███▄    █     ███▄ ▄███▓ ▄▄▄      ▒███████▒▓█████ 
▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▓█████▄ ▓██▒▒██▀ ██▌▒██▀ ██▌▓█   ▀  ██ ▀█   █    ▓██▒▀█▀ ██▒▒████▄    ▒ ▒ ▒ ▄▀░▓█   ▀ 
▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒██▒ ▄██▒██▒░██   █▌░██   █▌▒███   ▓██  ▀█ ██▒   ▓██    ▓██░▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒███   
░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒██░█▀  ░██░░▓█▄   ▌░▓█▄   ▌▒▓█  ▄ ▓██▒  ▐▌██▒   ▒██    ▒██ ░██▄▄▄▄██   ▄▀▒   ░▒▓█  ▄ 
░▒█░   ░ ████▓▒░░██▓ ▒██▒░▓█  ▀█▓░██░░▒████▓ ░▒████▓ ░▒████▒▒██░   ▓██░   ▒██▒   ░██▒ ▓█   ▓██▒▒███████▒░▒████▒
 ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▒▓███▀▒░▓   ▒▒▓  ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ▒ ▒    ░ ▒░   ░  ░ ▒▒   ▓▒█░░▒▒ ▓░▒░▒░░ ▒░ ░
 ░       ░ ▒ ▒░   ░▒ ░ ▒░▒░▒   ░  ▒ ░ ░ ▒  ▒  ░ ▒  ▒  ░ ░  ░░ ░░   ░ ▒░   ░  ░      ░  ▒   ▒▒ ░░░▒ ▒ ░ ▒ ░ ░  ░
 ░ ░   ░ ░ ░ ▒    ░░   ░  ░    ░  ▒ ░ ░ ░  ░  ░ ░  ░    ░      ░   ░ ░    ░      ░     ░   ▒   ░ ░ ░ ░ ░   ░   
           ░ ░     ░      ░       ░     ░       ░       ░  ░         ░           ░         ░  ░  ░ ░       ░  ░
                               ░      ░       ░                                                ░               
                                     BY HARI OM CHADHA""")
    
    b = input()
    print(f"""\n\n
This is a game of intelligence which is divided in 2 parts:""")
    b = input()
    print(f"""

PART 1: RIDDLES
The door at the end of the maze is locked so you must solve 3 riddles to get the key to the door
Faliure to solve the riddles in {attempts} attempts will lead to IMMINENT DEATH.
""")
    b = input()
    print(f"""
PART 2: THE MAZE
You will have exactly {secondsGame} seconds to solve the entire maze.
Failure to reach the exit will lead to IMMINENT DEATH

Completing the maze will prove that you are worthy of living and will be granted everything you desire.\n""")
    b = input("Press ENTER to begin the riddles.")
    riddles()
    return

#prompts the user to answer the three riddles
def riddles():
    global riddle1
    global riddle2
    global riddle3
    if not riddle1:
        for i in range(40):
            print("\n")
        print("""
RIDDLE 1:
What does man love more than life,
fear more than death or mortal strife, 
What the poor have, the rich require, 
and what contented men desire, 
What the miser spends and the spendthrift saves 
And all men carry to their graves?
""")
        answer = input("Answer: ").lower()
        if answer == "nothing":
            print("That is correct!")
            b = input("press ENTER to continue")
            riddle1 = True
        elif answer == "":   #attempts are not reduced if the player accidentally presses enter
            riddles()
            return
        else:
            riddleIncorrect()
            return

    if not riddle2:
        for i in range(40):
            print("\n")
        print("""
RIDDLE 2:
You can't see me. 
You can't touch me. 
You can't hear me. 
You can't taste me.
You can use me or create me. 
You can find me. 
I can be interrupted/broken easily. 
Some enjoy me and others fear me. What am I?\n
""")
        answer = input("Answer: ").lower()
        if answer == "silence":
            print("That is correct!")
            b = input("Press ENTER to continue")
            riddle2 = True
        elif answer == "":          #attempts are not reduced if the player accidentally presses enter
            riddles()
            return
        else:
            riddleIncorrect()
            return
    
    if not riddle3:
        for i in range(40):
            print("\n")
        print("""
RIDDLE 3:
I have a bed but never sleep,
I have a mouth but never speak.
I can run but never flee,
I'm full of pages, can you see?\n
""")
        answer = input("Answer: ").lower()
        if answer == "book":
            print("That is correct!")
            b = input("Press ENTER to continue")
            riddle3 = True
        elif answer == "":          #attempts are not reduced if the player accidentally presses enter
            riddles()
            return
        else:
            riddleIncorrect()
            return
    print("\n"*50)
    print("""
You are smarter than I thought. Here's the key to the exit:


     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
                                8o___oP' HC


I hope you are ready to die in the maze!
""")
    b = input()
    updateDirections()
    chooseDirection()
    return

#used to reduce the number of attemtpts and calls the death function if attempts == 0
def riddleIncorrect():
    global attempts
    print("That is incorrect.\n")
    attempts -= 1
    if attempts == 0:
        b = input(f"Looks like you ran out of tries. Bye bye {name}")
        death()
    else:
        print(f"You have {attempts} attempts left.")
        b = input("press ENTER to continue")
        riddles()
        return
    return

#checks to see what directoins are open from the players persepective
def openDirections():
    global choices
    choices = ""
    if userUp:
        choices += "forward(w)"
    if userLeft:
        if choices != "":
            choices += "/"
        choices += " left(a)"
    if userDown:
        if choices != "":
            choices += "/"
        choices += " backward(s)"
    if userRight:
        if choices != "":
            choices += "/"
        choices += " right(d)"
    return

#asks the user to pick a direction
def chooseDirection():
    global currentDirection
    global new
    global cheats
    openDirections()
    if new:
        art()
        print("Use the compass at the top to a keep track of the direction you are facing.")
        b = input(f"You have exactly {secondsGame:.2f} seconds to complete the maze. Press ENTER to move forward.\n").lower()
        direction = "w"
        timeCheck()
        new = False
    elif cheats:
        timeCheck()
        if secondsGame <= 0:
            print("You RAN OUT OF TIME even after having the map of the maze. HOW??")
            print("Mysterious Voice: You are actually the most disappointing person I have ever seen.")
            death()
            return
        print(f"Time left: {secondsGame:.2f} seconds")
        direction = input(f"You have either reached an intersection or a dead end. Please choose a path: {choices} OR type 'map' to see the map.\n").lower()
    else:
        timeCheck()
        if secondsGame <= 0:
            print("You RAN OUT OF TIME")
            death()
            return
        print(f"Time left: {secondsGame:.2f} seconds")
        direction = input(f"You have either reached an intersection or a dead end. Please choose a path: {choices}\n").lower()
    if direction == "w":
        if userUp:
            check()
        else:
            print("There's a wall in this direction. Try a different one")
            chooseDirection()
    #the currentDirection variable is used to track which way the player is facing
    #0 == north, 1 == east, -1 == west, -2/2 == south
    elif direction == "a":                          
        if userLeft:
            currentDirection -= 1
            check()
        else:
            print("There's a wall in this direction. Try a different one")
            chooseDirection()
    elif direction == "d":
        if userRight:
            currentDirection += 1
            check()
        else:
            print("There's a wall in this direction. Try a different one")
            chooseDirection()
    elif direction == "s":
        if userDown:
            currentDirection += 2
            check()
        else:
            print("There's a wall in this direction. Try a different one")
            chooseDirection()\
    #checks if a cheat code has been used
    elif direction == "cheats":
        if not cheats:
            print("\n"*50)
            art()
            print("Mysterious voice: OH NO! I am cursed to give the map to the player when that is said.")
            print("You can now access the map whenever you want BUT you still need to escape before the time runs out!")
            cheats = True
            chooseDirection()
        else:
            print("Cheats have already been activated.")
            chooseDirection()
    elif direction == "map" and cheats:
        map()
        art()
        chooseDirection()
    else:
        print("That's not a direction. Please try again")
        chooseDirection()
    return

#changes the value of currentDirection if it is not 0,1,-1,-2,2
def check():
    global currentDirection
    if currentDirection == -3:
        currentDirection = 1
    elif currentDirection == 3:
        currentDirection = -1
    elif currentDirection == 4:
        currentDirection = 0
    move(currentDirection)
    return

#used to find the closed intersection/turn/dead end in the maze.
#moves the player to that location and updates the x and y variables
def move(a):
    global x
    global y
    tempEnd = -99
    #facing north
    if a == 0:
        #finds the location of the wall right in front of the player
        for i in range (y - 1, -1, -1):
            if mazeDesign[i][x] == 1:
                tempEnd = i + 1
                break
        #finds the nearest intersection
        for i in range (y - 1, tempEnd - 1, -1):
            if mazeDesign[i][x-1] == 0:
                closestIntersection = i
                break
            if mazeDesign[i][x+1] == 0:
                closestIntersection = i
                break
        #updates the location
        try:
            if closestIntersection >= tempEnd:
                y = closestIntersection
            else: 
                y = tempEnd
        except:
            y = tempEnd
    #facing west
    elif a == -1:
        #finds the location of the wall right in front of the player
        for i in range (x - 1, -1, -1):
            if mazeDesign[y][i] == 1:
                tempEnd = i + 1
                break
        #finds the nearest intersection
        for i in range (x - 1, tempEnd - 1, -1):
            if mazeDesign[y-1][i] == 0:
                closestIntersection = i
                break
            if mazeDesign[y+1][i] == 0:
                closestIntersection = i
                break
        #updates the location
        try:
            if closestIntersection >= tempEnd:
                x = closestIntersection
            else: 
                x = tempEnd
        except:
            x = tempEnd
    #facing east
    elif a == 1:
        #finds the location of the wall right in front of the player
        for i in range (x + 1, len(mazeDesign[y]), 1):
            if mazeDesign[y][i] == 1:
                tempEnd = i - 1
                break
        #finds the nearest intersection
        for i in range (x + 1, tempEnd + 1, 1):
            if mazeDesign[y-1][i] == 0:
                closestIntersection = i
                break
            if mazeDesign[y+1][i] == 0:
                closestIntersection = i
                break
        #updates the location
        try:
            if closestIntersection <= tempEnd:
                x = closestIntersection
            else: 
                x = tempEnd
        except:
            x = tempEnd
    #facing south
    elif a == 2 or a == -2:
        #finds the location of the wall right in front of the player
        for i in range (y + 1, len(mazeDesign), 1):
            if mazeDesign[i][x] == 1:
                tempEnd = i - 1
                break
        #finds the nearest intersection
        for i in range (y + 1, tempEnd + 1, 1):
            if mazeDesign[i][x-1] == 0:
                closestIntersection = i
                break
            if mazeDesign[i][x+1] == 0:
                closestIntersection = i
                break
        #updates the location
        try:
            if closestIntersection <= tempEnd:
                y = closestIntersection
            else: 
                y = tempEnd
        except:
            y = tempEnd
    animation()
    updateDirections()
    if not win:
        art()
        chooseDirection()
    return
 
#maze doesn't turn so the player directions are tracked as booleans based on which way they are facing
#this functions updates the directions the player can move in
def updateDirections():
    global up
    global left
    global down
    global right
    global userUp
    global userLeft
    global userDown
    global userRight
    global win
    if mazeDesign[y - 1][x] == 0:
        up = True
    else:
        up = False
    if mazeDesign[y][x - 1] == 0:
        left = True
    else:
        left = False
    if mazeDesign[y + 1][x] == 0:
        down = True
    else:
        down = False
    if mazeDesign[y][x + 1] == 0:
        right = True
    else:
        right = False
    if currentDirection == 0:
        userUp = up
        userRight = right
        userLeft = left
        userDown = down
    elif currentDirection == -1:
        userUp = left
        userRight = up
        userLeft = down
        userDown = right
    elif currentDirection == 1:
        userUp = right
        userRight = down
        userLeft = up
        userDown = left
    elif currentDirection == 2 or currentDirection == -2:
        userUp = down
        userRight = left
        userLeft = right
        userDown = up
    if x == winX and y == winY:
        winGame()
    return

#this function prints the intercetion based on the open paths
#all intersections are made by conncatinating three different parts (right, front, and left)
def art():
    os.system('cls||clear')   #use for VScode
    #print("\n"*50)             #use for idle

    leftOpenArt = ['█████               ', 
                   '████████            ', 
                   '████████            ', 
                   '████████            ', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓██████', 
                   '████████▓▓▓▓▓▓████▓▓', 
                   '████████▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '████████▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '████████▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '████████▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '██████▓▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒']

    upOpenArt = ['                    ', 
                 '                    ', 
                 '                    ', 
                 '                    ', 
                 '                    ', 
                 '█                  █', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '██                ██', 
                 '▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓', 
                 '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                 '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                 '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                 '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                 '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                 '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                 '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                 '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒']

    rightOpenArt = ['               █████\n', 
                    '            ████████\n', 
                    '            ████████\n', 
                    '            ████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '██████▓▓▓▓▓▓████████\n', 
                    '▓▓████▓▓▓▓▓▓████████\n', 
                    '▒▒▒▒▒▒▒▒▒▒▒▒████████\n', 
                    '▒▒▒▒▒▒▒▒▒▒▒▒████████\n', 
                    '▒▒▒▒▒▒▒▒▒▒▒▒████████\n', 
                    '▒▒▒▒▒▒▒▒▒▒▒▒████████\n', 
                    '▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████\n', 
                    '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████\n', 
                    '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ HC\n']
    
    leftClosedArt = ['█████               ', 
                     '█████████           ', 
                     '███████████         ', 
                     '████████████████    ', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '████████████████████', 
                     '██████████████████▓▓', 
                     '████████████████▓▒▒▒', 
                     '██████████████▒▒▒▒▒▒', 
                     '████████████▓▒▒▒▓▒▒▒', 
                     '██████████▒▒▒▒▒▒▒▒▒▒', 
                     '████████▒▒▒▒▒▒▒▒▒▒▒▒', 
                     '██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                     '██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒']

    upClosedArt = ['                    ', 
                   '                    ', 
                   '                    ', 
                   '                    ', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '████████████████████', 
                   '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                   '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒']
    
    deadEndArt = ['                    ', 
                  '                    ', 
                  '                    ', 
                  '                    ', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓ DEAD ▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓ END! ▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█', 
                  '▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓', 
                  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', 
                  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒'] 
    
    rightClosedArt = ['               █████\n', 
                      '            ████████\n', 
                      '        ████████████\n', 
                      '  ██████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '████████████████████\n', 
                      '▓▓██████████████████\n', 
                      '▒▒▒▓▓███████████████\n', 
                      '▒▒▒▒▒▒▒▒████████████\n', 
                      '▒▒▒▒▒▒▒▒▓▒██████████\n', 
                      '▒▒▒▒▒▒▒▒▒▒▒▒████████\n', 
                      '▒▒▒▒▒▒▓▒▒▒▒▒▒▒██████\n', 
                      '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████\n', 
                      '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ HC\n']

    if new:
        directionArt()
        print(directionPrint)
        print("""
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |____ ENTER_____||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!| |MMMMMMMMMMM| |.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMMMMMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!| |MMMMMMMMMMM| |,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMMMMMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i| |MMMMMMMMMMM| | |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|MMMMMMMMMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;| |MMMMMMMMMMM| |`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMMMMMMMMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| | |MMMMMMMMMMM| ||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMMMMMMMM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[ ]MMMMMMMMMMM[ ] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._-   |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88888888888888888888888888888888888888888888888888888888888888 Internet
""")
    else:
        if userLeft:    
            printLeft = leftOpenArt
        else:
            printLeft = leftClosedArt
        if userUp:
            printUp = upOpenArt
        elif not userLeft and not userRight:
            printUp = deadEndArt
        else:
            printUp = upClosedArt
        if userRight:
            printRight = rightOpenArt
        else:
            printRight = rightClosedArt
        
        directionArt()
        print(directionPrint)
        for i in range (len(printLeft)):
            print(printLeft[i]+printUp[i]+printRight[i], end = "")
    return

#prints the animation that makes it look like the player is going forward
#uses 6 images with very small differeneces to make the animation
def animation():
    a = """
█████                                                  █████
█████████                                           ████████
███████████                                     ████████████
████████████████                            ████████████████
████████████████████                     ███████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
████████████████  ███                  █  ██████████████████
█████████████████████                  █████████████████████
██████████   ████████                  ███████   ███████████
█████████████████████                  █████████████████████
███   ███████████████                  ██████████████   ████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████████████
██████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████
████████████████▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███████████████
██████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████
████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████
██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████████
████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ HC"""

    b = """
█████                                                  █████
█████████                                           ████████
███████████                                     ████████████
████████████████                            ████████████████
████████████████████                     ███████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
████████████████████                   █████████████████████
███████████████  ████                  ██  █████████████████
█████████████████████                  █████████████████████
█████████   █████████                  ████████   ██████████
█████████████████████                  █████████████████████
██   ████████████████                  ███████████████   ███
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████████████████████
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████
██████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████
████████████▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████████
██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████
████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ HC"""

    c = """
█████                                                  █████
█████████                                           ████████
███████████                                     ████████████
████████████████                            ████████████████
████████████████████                     ███████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
███████████████████                     ████████████████████
██████████████  █████                  ████  ███████████████
█████████████████████                  █████████████████████
████████   ██████████                  ██████████   ████████
█████████████████████                  █████████████████████
   ██████████████████                  █████████████████   █
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████████████
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███████████████
██████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████
████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████
██████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████
████████▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ HC"""

    d = """
█████                                                  █████
█████████                                           ████████
███████████                                     ████████████
████████████████                            ████████████████
████████████████████                     ███████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
██████████████████  █                    ███████████████████
█████████████  ██████                  █████  ██████████████
█████████████████████                  █████████████████████
███████   ███████████                  ███████████   ███████
█████████████████████                  █████████████████████
  ███████████████████                  ██████████████████
█████████████████████                  █████████████████████
████████████████████▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████████████████████
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████
██████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████
████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████████
██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████
████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
██████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████
██▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓ HC"""

    e = """
█████                                                  █████
█████████                                           ████████
███████████                                     ████████████
████████████████                            ████████████████
████████████████████                     ███████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████████                  █████████████████████
█████████████████  ██                  █  ██████████████████
█████████████████████                  █████████████████████
████████████  ███████                  ██████  █████████████
█████████████████████                  █████████████████████
██████   ████████████                  ████████████   ██████
█████████████████████                  █████████████████████
 ████████████████████                  ████████████████████
████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████████████
██████████████████▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████████████████
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████
██████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████
████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████
██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████████
████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████
██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ HC"""

    list = [a,b,c,d,e]
    directionArt()
    #prints out the images after a small delay to makes it look like an animation
    for x in range (2):
        for i in list:
            #frame = "\n"*50 + directionPrint + i + "\n\n"             #use for idle
            time.sleep(0.12)                                        
            os.system('cls||clear')                                  #use for vs code
            frame = directionPrint + i                               #use for vs code
            print(frame, end = "")
    time.sleep(0.1)
    return

#prints the compass at the top based on the direction the player is facing
def directionArt():
    global directionPrint
    if currentDirection == 0:
        directionPrint = """
                             N
                             |     
                             |
                   W --------|-------- E     
                             |     
                             |     
                             S
                                        """
    elif currentDirection == 1:
        directionPrint = """
                             E
                             |     
                             |
                   N --------|-------- S     
                             |     
                             |     
                             W
                                        """
    elif currentDirection == -1:
        directionPrint = """
                             W
                             |     
                             |
                   S --------|-------- N     
                             |     
                             |     
                             E
                                        """
    else: 
        directionPrint = """
                             S
                             |     
                             |
                   E --------|-------- W     
                             |     
                             |     
                             N
                                        """
    return

#saves the time for when the game will end at the start of the maze
#subtracts the current time from the end time when the player moves
def timeCheck():
    global secondsGame
    global endTime
    if new:
        endTime = datetime.now() + timedelta(seconds = secondsGame)
    else: 
        a = endTime - datetime.now()
        secondsGame = a.total_seconds()
    return

#prints out the map of the maze with the exit and the player's current location if the cheats are activated
def map():
    print("                              ",end="")
    for row in range (1, len(mazeDesign)-1):
        for col in range (1, len(mazeDesign[0])-1):
            if row == y and col == x:
                if currentDirection == 0:
                    print("↑ ",end="")
                elif currentDirection == -1:
                    print(" ←",end="")
                elif currentDirection == 1:
                    print("→ ",end="")
                else:
                    print("↓ ",end="")
            elif row == winY and col ==winX:
                print("o ",end="")
            elif mazeDesign[row][col] == 1:
                print("██",end="")
            else:
                print("  ",end="")
        print()
        print("                              ",end="")
    print("\n'↑'is your location and direction.")
    print("'o' is the EXIT\n\n")
    print("Hurry up before you run out of time.")
    b = input("Press ENTER to continue")
    return

#Starts the death sequence of the lore
def death():
    b = input("Press ENTER to continue")
    print("\n"*50)
    a = ["Mysterious Voice: Looks like I was right once again! Humans are too weak and slow for this.",
         f"{name}: LET ME GO! WHY AM I HERE?",
         "Mysterious Voice: You wanna be free?",
         f"{name}: Yes, I wanna get out of here!",
         "Mysterious Voice: Ok then! I will free you from your pathetic life... BY KILLING YOU!! HAHAHA",
         f"{name}: NO THAT'S NOT WHAT I...",
         "The floor starts to break beneath you and there is no where to run. You start to fall into what looks like an empty void",
         f"{name}: AHHHHHH!! I DON'T WANNA DIE",
         "You see a bright light coming from the bottom of the hole you are falling in.",
         "It almost seems like there is something shiny at the bottom.",
         "You get closer and closer and see huge spikes full of blood pointed straight towards you.",
         """
                                                    ⢀⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣄⠀
                                        ⠀⠀⠀⣾⣿⣷⡀⠀⠀⠀⠀⠸⣿⣿⣿⣄⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⡿⠀
                                        ⠀⠀⠀⠻⣿⣿⣿⣦⡀⠀⠀⠀⠹⣿⣿⣿⣆⠀⠀⢀⣾⣿⣿⣿⠿⠛⠋⠁⠀⠀
                                        ⠀⠀⠀⠀⠙⢿⣿⣿⣿⣆⠀⠀⠀⠙⣿⣿⣿⣧⠀⣾⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⠀⠀⣠⣴⣿⣿⣿⣿⣷⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⢀⣴⣾⣿⣷⣦⡹⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⢀⣤⣾⣿⣆⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⣾⣿⣿⣿⣿⣿⣷⠘⣿⣿⣿⣿⣷⣦⣄⣠⣾⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠻⣿⣿⣿⣿⣿⠏⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠈⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠋⠀    Internet 
         


         



   /\\      /\\      /\\      /\\      /\\      /\\      /\\      /\\      /\\      /\\      /\\      /\\      /\\   
  /__\\    /__\\    /__\\    /__\\    /__\\    /__\\    /__\\    /__\\    /__\\    /__\\    /__\\    /__\\    /__\\    
 /\  /\\  /\  /\\  /\  /\\  /\  /\\  /\  /\\  /\  /\\  /\  /\\  /\  /\\  /\  /\\  /\  /\\  /\  /\\  /\  /\\  /\  /\\   
/__\/__\\/__\/__\\/__\/__\\/__\/__\\/__\/__\\/__\/__\\/__\/__\\/__\/__\\/__\/__\\/__\/__\\/__\/__\\/__\/__\\/__\/__\\  HC
         """,
         f"{name}: AHHHHHHH NOOOOOOOO!! NOOO PLEASE!!! HELP!!!!",
         "You shout to no avail and feel the spikes go though your body and tear it appart as soon as you reach the bottom.",
         "You try to move but realize that you can't feel your hand anymore.",
         "You look around to find your hand torn apart and a spike going through your arm.",
         "Your body feels empty and you see blood flowing out of the 4 separate pieces that once made your body.",
         "You close your eyes and your meaningless life flashes infront of you.",
         "Mysterious Voice: Wow! This human is ugly! Good riddance."]
    for i in a:
        print(i)
        b = input()
    again()
    return

#starts the win sequence if the player reaches the exit
def winGame():
    global win
    win = True
    print("\n"*50)
    a = ["""
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |____ EXIT!_____||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!| |MMMMMMMMMMM| |.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMMMMMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!| |MMMMMMMMMMM| |,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMMMMMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i| |MMMMMMMMMMM| | |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|MMMMMMMMMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;| |MMMMMMMMMMM| |`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMMMMMMMMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| | |MMMMMMMMMMM| ||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMMMMMMMM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[ ]MMMMMMMMMMM[ ] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._-   |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88888888888888888888888888888888888888888888888888888888888888 Internet
Press ENTER to continue""",
        "You see the door to the exit.",
        "You unlock the door using the key you have as fast as you can",
        """
                                              
                          ██████      
                        ██      ██    
                        ██      ██    
                        ██            
                      ██████████████  
                    ██              ██
                    ██      ██      ██
                    ██      ██      ██
                    ██              ██
                      ██████████████    HC
                      
                      """,
        "Mysterious Voice: You are smarter than I thought. You are the first person who has ever completed the maze",
        f"{name}: You promised that you will grant me everything I have ever wanted!",
        "Mysterious Voice: Yes yes, I remember.",
        f"{name}: Then grant me all my desires!",
        "Mysterious Voice: Close your eyes and all will be granted",
        "You close your eyes and feel relief for surviving the maze.",
        "The relief doesn't last long as it is followed by the worst feeling you have ever felt.",
        "You open your eyes to find yourself in your bedroom with a note in your right hand. It reads:",
        """
________________________________________________________________________
|                                                                      |
|                                                                      |
|                                                                      |
|                        IT WAS ALL A LIE!                             |
|                                                                      |
|                                                                      |
|              YOU CAN NEVER ESCAPE YOUR MEDIOCRE LIFE!                |
|                                                                      |
|                                                                      |
|                    I WILL SEE YOU AGAIN SOON!!                       |
|                                                                      |
|                                                                      |
|                                                                      |
|___________________________________________________________________ HC|

""",
        "Your heart sinks as you hear a wisper in your ear...",
        "Mysterious Voice: I am waiting for you"]
    for i in a:
        print(i)
        b = input()
    again()
    return

#asks the player if they want to play aganin. Recurrsive if the input is invalid
def again():
    a = input("\n\nWould you like to play again? (Y/N)\n").lower()
    if a == "y" or a == "yes":
        reset()
        start()
    elif a == "n" or a == "no":
        print("\nMysterious voice: You can never escape me! I WILL find you!\n\n")
        sys.exit()
    else:
        print("That's not a yes or a no")
        again()
    return

#resets all the global variables and calls the start function again
def reset():
    global riddle1
    global riddle2
    global riddle3
    global win
    global new
    global cheats
    riddle1 = False
    riddle2 = False
    riddle3 = False
    win = False
    new = True
    cheats = False
    return

#calls the start function to begin the game
start()
