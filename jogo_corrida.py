import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
imagem_fundo = "rua.png"
imagem_fundo_intro = pygame.image.load('tesla.png')
imagem_fundo_intro = pygame.transform.scale(imagem_fundo_intro,(800,600))
black = (0,0,0)
blue =(65,105,225)

white = (255,255,255)
red = (255,0,0)
green=(0,200,0)
turquoise=(72,209,204)
bright_red = (255,50,0)
bright_green = (0,255,0)
cyan=(0,255,255)
yelow=(255,255,102)

block_color = (53,115,255)
color=[blue,white,red]

m=1
car_width = 100
hscore=0
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Corrida Insper')
clock = pygame.time.Clock()
carImg = pygame.image.load('car_pygame1.png')
carImg2 = pygame.image.load('car_pygame.png')
carImg3 = pygame.image.load('car_pygame1.png')
maincar=carImg
shield=False
pause=False



def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Pontos: "+str(count), True, white)
    gameDisplay.blit(text,(0,0))
    text2 = font.render("High Score:"+str(hscore), True, white)
    gameDisplay.blit(text2,(150,0))
    if shield==False:
        text3 = font.render("Shield:OFF", True, white)
        gameDisplay.blit(text3,(300,0))
    else:
        text3 = font.render("Shield:ON", True, white)
        gameDisplay.blit(text3,(300,0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y,img):
    gameDisplay.blit(img,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()   
def newcars():
    ncar=True
    while ncar:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(green)
        button("",112,155,100,230,cyan,blue,carupdate(carImg))
        button("",362,155,100,230,cyan,blue,carupdate(carImg2))
        button("",612,155,100,230,cyan,blue,carupdate(carImg3))
        car(100,150,carImg)
        car(350,150,carImg2)
        car(600,150,carImg3)
        pygame.display.update()
        clock.tick(15)
def carupdate(img):
    maincar=img
def crash():
    message_display('Perdeu')
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1  and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
def unpause():
    global pause
    pause=False
def paused():
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Pause",largeText)
        TextRect.center = ((display_width/2),(display_height/2-50))
        gameDisplay.blit(TextSurf, TextRect)
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,game_intro)       
        pygame.display.update()
        clock.tick(15)
def game_intro(imagem_fundo_intro,gameDisplay):
    gameDisplay.blit(imagem_fundo_intro,(0,0))
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
       
        button("Start",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quit)
        button("New Cars",350,450,100,50,turquoise,cyan,newcars)       
        pygame.display.update()
        clock.tick(15)
    
def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 6
    thing_width = 100
    thing_height = 100

    item_startx = random.randrange(0, display_width)
    item_starty=-1200
    item_speed = 20
    item_width = 100
    item_height = 100

    shield_startx = random.randrange(0, display_width)
    shield_starty=-3600
    shield_speed = 14
    shield_width = 50
    shield_height = 100


    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7
                if event.key==pygame.K_p:
                    pause=True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        
        background = pygame.image.load(imagem_fundo).convert()
        background = pygame.transform.scale(background,(800,600))
        gameDisplay.blit(background,[0,0])
        

        things(thing_startx, thing_starty, thing_width, thing_height, green)
        things(item_startx, item_starty, item_width, item_height,blue)
        things(shield_startx, shield_starty, shield_width, shield_height,yelow)
        global m
        global shield
        thing_starty += thing_speed
        item_starty += item_speed
        shield_starty += shield_speed

        car(x,y,maincar)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 10
            thing_speed += 0.6


        if shield_starty > display_height:
            shield_starty=-3600
            item_startx = random.randrange(0, display_width)
    
        if item_starty > display_height:
            item_starty=-1200
            item_startx = random.randrange(0, display_width)
            m=1
        if y < shield_starty+shield_height:
            if x > shield_startx and x < shield_startx + shield_width or x+car_width > shield_startx and x + car_width < shield_startx+shield_width:
                shield=True
        if shield==False and  y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                global hscore
                if dodged>hscore:
                    hscore=dodged
                crash()
        if y < thing_starty+thing_height and shield==True:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                shield=False

        if y < item_starty+item_height and m==0:
            if x > item_startx and x < item_startx + item_width or x+car_width > item_startx and x + car_width < item_startx+item_width:
                dodged=dodged+1
                m=1
        pygame.display.update()
        clock.tick(60)
game_intro(imagem_fundo_intro,gameDisplay)
game_loop()
pygame.quit()
quit()
