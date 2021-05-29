import pygame
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
                x=x+10
       
            if event.key==pygame.K_LEFT:
                x=x-10
       
            if event.key==pygame.K_UP:
                y=y-10
        
            if event.key==pygame.K_DOWN:
                y=y+10

    #window color
    gameWindow.fill(white)

    ##Making head of snake
    pygame.draw.rect(gameWindow, red, [x,y,sn_size,sn_size])

        #after every change update
    pygame.display.update()
    
pygame.quit()
quit()
