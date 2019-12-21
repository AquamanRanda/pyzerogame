import string
from random import choice,randint
import pgzrun

WIDTH = 500
HEIGHT = 500
black = (0,0,0)
white = (255,255,255)
velocity=1
score = {"right" : 0,"wrong": 0}
LETTERS = list()
LETTER =dict()

for i in range(0,4):
    LETTER = {"letter": choice(string.ascii_letters).lower(), "x": randint(0,WIDTH-10), "y": 0}
    LETTERS.append(LETTER)

def draw():
    screen.clear()
    screen.fill(black)
    for i in range(0,4):
        cordinates = (LETTERS[i]["x"],LETTERS[i]["y"])
        screen.draw.text(LETTERS[i]["letter"],(cordinates),color=(randint(0,255),randint(0,255),randint(0,255)),fontsize = 45)
    screen.draw.text("Right: " +str(score["right"]),(0,10),color=(0,255,30),fontsize= 30)
    screen.draw.text("Wrong: " +str(score["wrong"]),(0,40),color=(255,7,30),fontsize=30)

def  on_key_down(key,mod,unicode):
    if unicode:
        for i in range(4):
            flag =0
            if unicode == LETTERS[i]["letter"]:
                flag = 1
                score["right"] += 1
                update_letter(i)
                break
        if(flag != 1):
            score["wrong"]+= 1

def update_letter(i):
    LETTERS[i]["letter"] = choice(string.ascii_letters).lower()
    LETTERS[i]["x"] = randint(10, WIDTH-10)
    LETTERS[i]["y"] = 0


def update():
    for i in range(4):
        LETTERS[i]["y"] += velocity
        if(LETTERS[i]["y"] == HEIGHT):
            LETTERS[i]["y"] = 0
            score["wrong"] +=1
            update_letter(i)
            break

pgzrun.go()