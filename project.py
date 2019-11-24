import pygame
import time
import random
import sys
pygame.init()  #creating the wnd

black = (0,0,0)  #RGB values   
red = (255,0,0)
display_width = 1000
display_height = 800
game_display = pygame.display.set_mode((display_width,display_height))   #setting the width and height
pygame.display.set_caption("Car Racing Game")
clock = pygame.time.Clock()
carImg = pygame.image.load("blueCar.png")
carImg = pygame.transform.scale(carImg,(100,160))
backgroundpic = pygame.image.load("background.png")
roadpic = pygame.image.load("Road2.jpg")
roadpic = pygame.transform.scale(roadpic,(750,800))
carWidth = 100
car2Img = pygame.image.load("PinkCar.png")
car2Img = pygame.transform.scale(car2Img,(100,160))
mainScreen = pygame.image.load("main.jpg")

def obstacle(obs_startx,obs_starty,obs):
    if obs == 0:
        obs_pic = pygame.image.load("bluebus.png")
        obs_pic = pygame.transform.scale(obs_pic,(150,160))

    elif obs == 1:
        obs_pic = pygame.image.load("police.png")
        obs_pic = pygame.transform.scale(obs_pic,(150,160))
      

    elif obs == 2:
        obs_pic = pygame.image.load("raceCar.png")
        obs_pic = pygame.transform.scale(obs_pic,(150,160))

        
    elif obs == 3:
        obs_pic = pygame.image.load("carCrash.png")
        obs_pic = pygame.transform.scale(obs_pic,(150,160))
    

    elif obs == 4:
        obs_pic = pygame.image.load("dead.png")
        obs_pic = pygame.transform.scale(obs_pic,(150,160))


    elif obs == 5:
        obs_pic = pygame.image.load("branch.png")
        obs_pic = pygame.transform.scale(obs_pic,(150,160))
   

    elif obs == 6:
        obs_pic = pygame.image.load("greenCar.png")
        obs_pic = pygame.transform.scale(obs_pic,(150,160))
        

    game_display.blit(obs_pic,(obs_startx,obs_starty))


def crash():
    message_display("CRASHED")


def message_display(text):
     txt = pygame.font.Font("freesansbold.ttf",100)
     textsurf,textrect = text_object(text,txt)     #create a function to edit the message
     textrect.center = (display_width/2,display_height/2)
     game_display.blit(textsurf,textrect)
     pygame.display.update()
     #time.sleep(3)
     main() 


def text_object(text,font):   #display the message after the crash
    textsurface = font.render(text,True,red)   
    return textsurface,textsurface.get_rect() #restart the game


def background():
    game_display.blit(backgroundpic,(0,0))
    game_display.blit(backgroundpic,(0,200))
    game_display.blit(backgroundpic,(0,400))
    game_display.blit(backgroundpic,(900,0))
    game_display.blit(roadpic,(120,0))

def player(x,y):
    game_display.blit(carImg,(x,y))    #puts the image into the window

"""
def computer(x1,y1):
    game_display.blit(car2Img,(x1,y1))
"""
        
# All functions are called from this function
def main():
    x = (display_width*0.45)
    y = (display_height*0.8)
    x_change = 0
    #x1 = (display_width*0.54)
    #y1 = (display_height*0.8)
    obstacle_speed = 17
    obs = 0
    obs_startx = random.randrange(200,(display_width-200))
    obs_starty = -1000
    obs_width = 150
    obs_height = 100
    x_axis = 0
    y_axis = 0
    
    bumped = False     #if the game is not any problem to start
    while not bumped:
        for event in  pygame.event.get():   #if any input is given
            if event.type ==  pygame.QUIT: #if the exit button is pressed      
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:


                    x_change = 0
        x += x_change
        #firstWnd()
        game_display.fill(black)

        y_move = y_axis % backgroundpic.get_rect().width
        game_display.blit(backgroundpic,(0,y_move-backgroundpic.get_rect().width))
        game_display.blit(backgroundpic,(900,y_move-backgroundpic.get_rect().width))
        if y_move < display_height:
            game_display.blit(backgroundpic,(0,y_move))
            game_display.blit(backgroundpic,(900,y_move))
            game_display.blit(roadpic,(300,y_move+300))
            game_display.blit(roadpic,(700,y_move+100))
            
        x_axis += obstacle_speed
        

        background()
        obs_starty -= (obstacle_speed / 4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty += obstacle_speed
        player(x,y)
        #computer(x1,y1)
        if x < 175 or x > 720:
            bumped = True
            crash()
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(200,(display_width-200))
            obs = random.randrange(0,6)

        if y > obs_startx and x < obs_startx + obs_width or x + carWidth > obs_startx and x + carWidth < obs_startx + obs_width:
            crash()
                
            
        pygame.display.update()   #update the display
        clock.tick(60)

        
main()
pygame.quit()
quit()
