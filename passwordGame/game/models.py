from django.db import models
import random
# Create your models here.

def StarGame():
    gameStart = ''
    if gameStart == True:
        outline = True    
    else: 
        outline = False
    
        if outline == True:
            button = "btn-outline-secondary"
        else:
            button = "btn-secondary"



red = 'buttonRed'
green = 'buttonGreen'
blue = 'buttonBlue'
yellow = 'buttonYellow'
purple = 'buttonPurple'
gameButtons = [red, green, blue, yellow, purple]

def GeneratedButtons():
    buttons = []
    
def RandomButtons():

    # rand = random.shuffle(gameButtons)
    rand = gameButtons[0]
    
    return rand

def  Game(): 
    click = ''
    cont = []
        
    
    def GameCount():
        if click == RandomButtons:
            cont.append(click)
            GameCount()
        else:
            exit = ''
                               
                