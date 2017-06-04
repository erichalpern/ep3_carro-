import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
imagem_fundo = "rua.png"
imagem_fundo_intro = pygame.image.load('tesla.png')
imagem_fundo_intro = pygame.transform.scale(imagem_fundo_intro,(800,600))

imagem_fundo_ncar = pygame.image.load('workshop.png')

black = (0,0,0)
blue =(65,105,225)
gray=(128,128,128)
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
r=0
car_width = 100
hscore=0
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Corrida Insper')
clock = pygame.time.Clock()
carImg = pygame.image.load('car_pygame1.png')
carImg2 = pygame.image.load('car_pygame.png')
pygame.transform.scale(carImg2, (int(125),int(237)))
maincar=carImg
teleport=False
pause=False
def song():
     file = 'musica.mp3'
     pygame.init()
     pygame.mixer.init()
     pygame.mixer.music.load(file)
     pygame.mixer.music.play()

def sombatida():
     file = 'batida.mp3'
     pygame.init()
     pygame.mixer.init()
     pygame.mixer.music.load(file)
     pygame.mixer.music.play()


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Pontos: "+str(count), True, white)
    gameDisplay.blit(text,(0,0))
    text2 = font.render("High Score:"+str(hscore), True, white)
    gameDisplay.blit(text2,(150,0))
    if teleport==False:
        text3 = font.render("teleport:OFF", True, white)
        gameDisplay.blit(text3,(300,0))
    else:
        text3 = font.render("teleport:ON", True, white)
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
    global carImg
    global carImg2
    global carImg3
    ncar=True
    while ncar:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(imagem_fundo_ncar,(0,0))
        button("",112,155,100,230,cyan,blue,carupdate(carImg))
        button("",612,155,100,250,cyan,blue,carupdate(carImg2))
        button("Game",412,455,100,50,cyan,blue,game_loop())

        car(100,150,carImg)
        car(590,130,carImg2)
        pygame.display.update()
        clock.tick(15)
def carupdate(i):
    global maincar
    maincar=i

def crash():
    sombatida()
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
    song()
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

    teleport_startx = random.randrange(0, display_width)
    teleport_starty=-3600
    teleport_speed = 10
    teleport_width = 50
    teleport_height = 100


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
                    x_change = -9
                if event.key == pygame.K_RIGHT:
                    x_change = 9
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
        

        things(thing_startx, thing_starty, thing_width, thing_height, red)
        things(item_startx, item_starty, item_width, item_height,blue)
        things(teleport_startx, teleport_starty, teleport_width, teleport_height,yelow)
        global m
        global teleport
        thing_starty += thing_speed
        item_starty += item_speed
        teleport_starty += teleport_speed

        car(x,y,maincar)
        things_dodged(dodged)

        if x > display_width - car_width:
            if teleport==True:
                teleport=False
                x=car_width
            else:
                crash()
        if x < 0:
            if teleport==True:
                teleport=False
                x=display_width - car_width

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 10
            thing_speed += 0.6


        if teleport_starty > display_height:
            teleport_starty=-3600
            item_startx = random.randrange(0, display_width)
    
        if item_starty > display_height:
            item_starty=-1200
            item_startx = random.randrange(0, display_width)
            m=1
        if y < teleport_starty+teleport_height:
            if x > teleport_startx and x < teleport_startx + teleport_width or x+car_width > teleport_startx and x + car_width < teleport_startx+teleport_width:
                teleport=True
        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                global hscore
                if dodged>hscore:
                    hscore=dodged
                crash()

        if y < item_starty+item_height and m==1:
            if x > item_startx and x < item_startx + item_width or x+car_width > item_startx and x + car_width < item_startx+item_width:
                dodged=dodged+1
                m=1
                
        pygame.display.update()
        clock.tick(60)
game_intro(imagem_fundo_intro,gameDisplay)
game_loop()
pygame.quit()
quit()
