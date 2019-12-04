import pygame
import time
import random
import sys

###pictures####
#https://ind13.com/upcoming-indie-driving-games-2018/
#https://www.hiclipart.com/free-transparent-background-png-clipart-qrpff
#https://www.amazon.com/ASHLEY-PRODUCTIONS-MAGNETIC-MAGI-STRIPS-YELLOW/dp/B00QFXEHJG
#https://www.clipartmax.com/middle/m2H7H7m2G6Z5G6K9_racing-car-top-view/
#https://www.clipartmax.com/download/m2K9A0m2G6m2N4G6_big-image-clipart-car-top-view/
#https://www.clipartmax.com/max/m2i8K9i8H7d3H7N4/
#https://www.clipartmax.com/middle/m2i8H7G6Z5A0i8G6_car-top-view/
#https://www.clipartmax.com/middle/m2i8A0A0K9A0N4G6_blue-bus-stop-sign-bus/
#https://i-love-png.com/dead-dinosaur-png-1.html
###

pygame.mixer.init()
pygame.init()
grey = (119,118,110)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,200)
brightRed = (255,0,0)
brightGreen = (0,255,0)
brightBlue = (0,0,255)
wndWidth = 800
wndHeight = 600



#Background music
#pygame.mixer.music.load("music.mp3")
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play(-1)


gameWnd = pygame.display.set_mode((wndWidth,wndHeight))
pygame.display.set_caption("car game")
clock = pygame.time.Clock()
carImg = pygame.image.load('blueCar.png')
backgroundpic = pygame.image.load("background.jpg")
yellowStrip = pygame.image.load("yellow strip.png")
strip = pygame.image.load("strip.jpg")
mainScreen = pygame.image.load("main.jpg")
mainScreen = pygame.transform.scale(mainScreen,(wndWidth,wndHeight))
carWidth = 56
pause = False

def mainWnd():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameWnd.blit(mainScreen,(0,0))
        largetext = pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("RACE GAME",largetext)
        TextRect.center = (400,100)
        gameWnd.blit(TextSurf,TextRect)
        button("PLAY",150,520,100,50,green,brightGreen,"play")
        button("QUIT",550,520,100,50,red,brightRed,"quit")
        button("INSTRUCTIONS",300,520,200,50,blue,brightBlue,"intro")
        pygame.display.update()
        clock.tick(50)


def button(msg,x1,y1,width,height,inactivecolor,activecolor,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x1 + width > mouse[0] > x1 and y1 + height > mouse[1] > y1:
        pygame.draw.rect(gameWnd,activecolor,(x1,y1,width,height))
        if click[0] == 1 and action != None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                mainWnd()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()
                

    else:
        pygame.draw.rect(gameWnd,inactivecolor,(x1,y1,width,height))
    smalltext = pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect = text_objects(msg,smalltext)
    textrect.center = ((x1+(width/2)),(y1+(height/2)))
    gameWnd.blit(textsurf,textrect)


def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameWnd.blit(mainScreen,(0,0))
        largetext = pygame.font.Font('freesansbold.ttf',80)
        smalltext = pygame.font.Font('freesansbold.ttf',20)
        mediumtext = pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect = text_objects("This is an car game in which you need aviod the obstacles",smalltext)
        textRect.center = ((350),(200))
        TextSurf,TextRect = text_objects("INSTRUCTION",largetext)
        TextRect.center = ((400),(100))
        gameWnd.blit(TextSurf,TextRect)
        gameWnd.blit(textSurf,textRect)
        stextSurf,stextRect = text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center = ((150),(400))
        hTextSurf,hTextRect = text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center = ((150),(450))
        atextSurf,atextRect = text_objects("A : ACCELERATOR",smalltext)
        atextRect.center = ((150),(500))
        rtextSurf,rtextRect = text_objects("B : BRAKE ",smalltext)
        rtextRect.center = ((150),(550))
        ptextSurf,ptextRect = text_objects("P : PAUSE  ",smalltext)
        ptextRect.center = ((150),(350))
        sTextSurf,sTextRect = text_objects("CONTROLS",mediumtext)
        sTextRect.center = ((350),(300))
        gameWnd.blit(sTextSurf,sTextRect)
        gameWnd.blit(stextSurf,stextRect)
        gameWnd.blit(hTextSurf,hTextRect)
        gameWnd.blit(atextSurf,atextRect)
        gameWnd.blit(rtextSurf,rtextRect)
        gameWnd.blit(ptextSurf,ptextRect)
        button("BACK",600,450,100,50,blue,brightBlue,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause
    while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gameWnd.blit(mainScreen,(0,0))
            largetext = pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect = text_objects("PAUSED",largetext)
            TextRect.center = ((wndWidth/2),(wndHeight/2))
            gameWnd.blit(TextSurf,TextRect)
            button("CONTINUE",150,450,150,50,green,brightGreen,"unpause")
            button("RESTART",350,450,150,50,blue,brightBlue,"play")
            button("MAIN MENU",550,450,200,50,red,brightRed,"menu")
            pygame.display.update()
            clock.tick(30)

def unpaused():
    global pause
    pause = False


def countdown_background():
    font = pygame.font.SysFont(None,35)
    x = (wndWidth*0.45)
    y = (wndHeight*0.8)
    gameWnd.blit(backgroundpic,(0,0))
    gameWnd.blit(backgroundpic,(0,200))
    gameWnd.blit(backgroundpic,(0,400))
    gameWnd.blit(backgroundpic,(700,0))
    gameWnd.blit(backgroundpic,(700,200))
    gameWnd.blit(backgroundpic,(700,400))
    gameWnd.blit(yellowStrip,(400,100))
    gameWnd.blit(yellowStrip,(400,200))
    gameWnd.blit(yellowStrip,(400,300))
    gameWnd.blit(yellowStrip,(400,400))
    gameWnd.blit(yellowStrip,(400,100))
    gameWnd.blit(yellowStrip,(400,500))
    gameWnd.blit(yellowStrip,(400,0))
    gameWnd.blit(yellowStrip,(400,600))
    gameWnd.blit(strip,(120,200))
    gameWnd.blit(strip,(120,0))
    gameWnd.blit(strip,(120,100))
    gameWnd.blit(strip,(680,100))
    gameWnd.blit(strip,(680,0))
    gameWnd.blit(strip,(680,200))
    gameWnd.blit(carImg,(x,y))
    text = font.render("DODGED: 0",True, white)
    score = font.render("SCORE: 0",True,red)
    gameWnd.blit(text,(0,50))
    gameWnd.blit(score,(0,30))
    button("PAUSE",650,0,150,50,blue,brightBlue,"pause")

def countdown():
    countdown = True
    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gameWnd.fill(red)
            countdown_background()
            largetext = pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect = text_objects("3",largetext)
            TextRect.center = ((wndWidth/2),(wndHeight/2))
            gameWnd.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gameWnd.fill(grey)
            countdown_background()
            largetext = pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect = text_objects("2",largetext)
            TextRect.center = ((wndWidth/2),(wndHeight/2))
            gameWnd.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gameWnd.fill(grey)
            countdown_background()
            largetext = pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect = text_objects("1",largetext)
            TextRect.center = ((wndWidth/2),(wndHeight/2))
            gameWnd.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gameWnd.fill(grey)
            countdown_background()
            largetext = pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect = text_objects("GO!",largetext)
            TextRect.center = ((wndWidth/2),(wndHeight/2))
            gameWnd.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()

def obstacle(obs_startx,obs_starty,obs):
    if obs == 0:
        obs_pic = pygame.image.load("pinkCar.png")
        gameWnd.blit(obs_pic,(obs_startx,obs_starty))
        
    elif obs == 1:
        obs_pic = pygame.image.load("raceCar.png")
        gameWnd.blit(obs_pic,(obs_startx,obs_starty))
        
    elif obs == 2:
        obs_pic = pygame.image.load("bluebus.png")
        gameWnd.blit(obs_pic,(obs_startx,obs_starty))
        
    elif obs == 3:
        obs_pic = pygame.image.load("police.png")
        gameWnd.blit(obs_pic,(obs_startx,obs_starty))
        
    elif obs == 4:
        obs_pic = pygame.image.load("dead.png")
        gameWnd.blit(obs_pic,(obs_startx,obs_starty))
        
    elif obs == 6:
        obs_pic = pygame.image.load("carCrash.png")
        gameWnd.blit(obs_pic,(obs_startx,obs_starty))

    elif obs == 7:
        obs_pic = pygame.image.load("2cars.png")
        gameWnd.blit(obs_pic,(obs_startx,obs_starty))

    elif obs == 8:
        obs_pic = pygame.image.load("car.png")
        gameWnd.blit(obs_pic,(obs_startx,obs_starty))
    
    elif obs == 9:
        obs_pic = pygame.image.load("carCrash.png")
        gameWnd.blit(obs_pic,(obs_startx,obs_starty))

    elif obs == 10:
        obs_pic = pygame.image.load("powerup.png")
        gameWnd.blit(obs_pic,(obs_startx,obs_starty))
        


    
def score_system(passed,score):
    font = pygame.font.SysFont(None,25)
    text = font.render("Passed "+str(passed),True,white)
    score = font.render("Score "+str(score),True,red)
    gameWnd.blit(text,(0,50))
    gameWnd.blit(score,(0,30))


def text_objects(text,font):
    textsurface = font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center = ((wndWidth/2),(wndHeight/2))
    gameWnd.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("CRASHED")


def background():
    gameWnd.blit(backgroundpic,(0,0))
    gameWnd.blit(backgroundpic,(0,200))
    gameWnd.blit(backgroundpic,(0,400))
    gameWnd.blit(backgroundpic,(700,0))
    gameWnd.blit(backgroundpic,(700,200))
    gameWnd.blit(backgroundpic,(700,400))
    gameWnd.blit(yellowStrip,(400,0))
    gameWnd.blit(yellowStrip,(400,100))
    gameWnd.blit(yellowStrip,(400,200))
    gameWnd.blit(yellowStrip,(400,300))
    gameWnd.blit(yellowStrip,(400,400))
    gameWnd.blit(yellowStrip,(400,500))
    gameWnd.blit(strip,(120,0))
    gameWnd.blit(strip,(120,100))
    gameWnd.blit(strip,(120,200))
    gameWnd.blit(strip,(680,0))
    gameWnd.blit(strip,(680,100))
    gameWnd.blit(strip,(680,200))

def car(x,y):
    gameWnd.blit(carImg,(x,y))

    
def game_loop():
    global pause
    x = (wndWidth*0.45)
    y = (wndHeight*0.8)
    x_change = 0
    obstacle_speed = 11
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200,(wndWidth-200))
    obs_starty = -750
    obs_width = 60
    obs_height = 125
    passed = 0
    level = 0
    score = 0
    y2 = 7
    fps = 120

    flag = False
    while not flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change=-5
                if event.key == pygame.K_RIGHT:
                    x_change=5
                if event.key == pygame.K_a:
                    obstacle_speed+=2
                if event.key == pygame.K_b:
                    obstacle_speed-=2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x += x_change
        pause = True
        gameWnd.fill(grey)

        rel_y = y2 % backgroundpic.get_rect().width
        gameWnd.blit(backgroundpic,(0,rel_y - backgroundpic.get_rect().width))
        gameWnd.blit(backgroundpic,(700,rel_y - backgroundpic.get_rect().width))
        if rel_y < 800:
            gameWnd.blit(backgroundpic,(0,rel_y))
            gameWnd.blit(backgroundpic,(700,rel_y))
            gameWnd.blit(yellowStrip,(400,rel_y))
            gameWnd.blit(yellowStrip,(400,rel_y + 100))
            gameWnd.blit(yellowStrip,(400,rel_y + 200))
            gameWnd.blit(yellowStrip,(400,rel_y + 300))
            gameWnd.blit(yellowStrip,(400,rel_y + 400))
            gameWnd.blit(yellowStrip,(400,rel_y + 500))
            gameWnd.blit(yellowStrip,(400,rel_y - 100))
            gameWnd.blit(strip,(120,rel_y - 200))
            gameWnd.blit(strip,(120,rel_y + 20))
            gameWnd.blit(strip,(120,rel_y + 30))
            gameWnd.blit(strip,(680,rel_y - 100))
            gameWnd.blit(strip,(680,rel_y + 20))
            gameWnd.blit(strip,(680,rel_y + 30))

        y2 += obstacle_speed


        obs_starty -= (obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty += obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x > 690 - carWidth or x < 110:
            crash()
        if x > wndWidth - (carWidth + 110) or x < 110:
            crash()
        if obs_starty > wndHeight:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170,(wndWidth-170))
            obs = random.randrange(0,11)
            if obs == 10:
                obstacle_speed += 10
            passed = passed + 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed + 4
                largetext = pygame.font.Font("freesansbold.ttf",100)
                textsurf,textrect=text_objects("LEVEL "+str(level),largetext)
                textrect.center = ((wndWidth/2),(wndHeight/2))
                gameWnd.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)


        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + carWidth > obs_startx and x + carWidth < obs_startx + obs_width:
                crash()
        button("Pause",650,0,150,50,blue,brightBlue,"pause")
        pygame.display.update()
        clock.tick(60)
mainWnd()
game_loop()
pygame.quit()
quit()
