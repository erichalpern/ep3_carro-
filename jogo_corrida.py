import pygame
import time
import random
import socket, pickle

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green=(0,200,0)
turquoise=(72,209,204)
bright_red = (255,50,0)
bright_green = (0,255,0)
cyan=(0,255,255)

block_color = (53,115,255)

car_width = 100
hscore=0
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Corrida Insper')
clock = pygame.time.Clock()

carImg = pygame.image.load('car_pygame1.png')
pause=False

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('127.0.0.1', 8080))



def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Pontos: "+str(count), True, white)
    gameDisplay.blit(text,(0,0))
    text2 = font.render("High Score:"+str(hscore), True, white)
    gameDisplay.blit(text2,(150,0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

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
    
    

def crash():
    message_display('Perdeu')
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
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
        button("Quit",550,450,100,50,red,bright_red,quit)       
        pygame.display.update()
        clock.tick(15)
def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Vai melhorar",largeText)
        TextRect.center = ((display_width/2),(display_height/2-50))
        gameDisplay.blit(TextSurf, TextRect)
        button("Start",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quit)
        button("New Cars",350,450,100,50,turquoise,cyan,quit)       
        pygame.display.update()
        clock.tick(15)
    
def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

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
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key==pygame.K_p:
                    pause=True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change


        coordenada_x=str(x)
        coordenada_x=pickle.dumps(coordenada_x)
        server.send(coordenada_x)
        coordenada_x=server.recv(1024)
        coordenada_x=pickle.loads(coordenada_x)
        print(coordenada_x)
        coordenada_y=str(y)
        coordenada_y=pickle.dumps(coordenada_y)
        server.send(coordenada_y)
        coordenada_y=server.recv(1024)
        coordenada_y=pickle.loads(coordenada_y)
        print(coordenada_y)
       



        gameDisplay.fill(black)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, green)


        
        thing_starty += thing_speed
        
        
        #car(x,y)
        car(float(coordenada_x),float(coordenada_y))
        car(float(coordenada_x)+100,float(coordenada_y))
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 0.6
            #thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                global hscore
                if dodged>hscore:
                    hscore=dodged
                crash()
        
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()