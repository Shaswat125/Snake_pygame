import pygame
import random
pygame.init()
width=900
height=600
##Game window
gameWindow=pygame.display.set_mode((width, height))
pygame.display.set_caption("MIck's Snake game")
pygame.display.update()
##Game specific varibles
exit_game=False
game_over=False
x=60##initial position of snake
y=60
sn_size=30
clock=pygame.time.Clock()#it handles the clock of game
fps=60
speed_x=10
speed_y=0##we give speed or velocity to our snake

##lets make food for our snake
food_x=random.randint(0,width)
food_y=random.randint(0,height)
score=0##for making score go up

##Colors
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)


##Game Loop
while not exit_game:
    for event in pygame.event.get(): 
        ##print(event)
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                speed_x=10
                speed_y=0
       
            if event.key==pygame.K_LEFT:
                speed_x=-10
                speed_y=0
       
            if event.key==pygame.K_UP:
                speed_y=-10
                speed_x=0
        
            if event.key==pygame.K_DOWN:
                speed_y=10
                speed_x=0

    #changing speed
    x+=speed_x
    y+=speed_y
    
##    if x>=height:
##        x=0
##    if y>=width:
##        y=0
##        x=0
    #window color
    gameWindow.fill(white)

     
    ##Making head of snake
    pygame.draw.rect(gameWindow, red, [x,y,sn_size,sn_size])

    ##making food
    pygame.draw.rect(gameWindow, green, [food_x,food_y,sn_size,sn_size])
    if abs(x-food_x)<6 and abs(y-food_y)<6:
        score+=1
        print("Score:", score)
    ##how many frames in one sec
    clock.tick(fps)
        #after every change update
    pygame.display.update()
    
pygame.quit()
quit()
