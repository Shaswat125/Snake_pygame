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
sn_size=20
clock=pygame.time.Clock()#it handles the clock of game
fps=60
in_velocity=5
speed_x=5
speed_y=0##we give speed or velocity to our snake
##lets make score print on display board
font=pygame.font.SysFont(None,20)
def text_screen(text,color,x,y):
    screen=font.render(text,True,color)##this take 3 variables and print in
    gameWindow.blit(screen,(x,y))##blit func prints in on screen
    
##lets make food for our snake random function returns random variable between a nad b
food_x=random.randint(10,width/2)
food_y=random.randint(10,height/2)
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
                speed_x=in_velocity
                speed_y=0
       
            if event.key==pygame.K_LEFT:
                speed_x=-in_velocity
                speed_y=0
       
            if event.key==pygame.K_UP:
                speed_y=-in_velocity
                speed_x=0
        
            if event.key==pygame.K_DOWN:
                speed_y=in_velocity
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
    text_screen("Score:"+str(score),blue,15,15)
    ##prints score on display
     
    ##Making head of snake
    pygame.draw.rect(gameWindow, red, [x,y,sn_size,sn_size])

    ##making food and eating it
    pygame.draw.rect(gameWindow, green, [food_x,food_y,sn_size,sn_size])
    if abs(x-food_x)<15 and abs(y-food_y)<15:
        score+=10
        ##print("Score:", score)
        food_x=random.randint(10,width/1.5)
        food_y=random.randint(10,height/2)
    ##how many frames in one sec
    clock.tick(fps)
        #after every change update
    pygame.display.update()
    
pygame.quit()
quit()
