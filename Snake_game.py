import pygame
x=pygame.init()

##It displays the type of x
##print(x)
##We need to make a window for game playing :
gameWindow=pygame.display.set_mode((1200,500))

##this takes tuple as height and width of window gameWin is var

##to set the title of game window
pygame.display.set_caption("Roy's game")

##to end the game we need a variable, if this var is true then game ends
exit_game=False
game_over=False##to ask wheter to restart

i=0
##we create game loop that handles all operations within a game
while(not exit_game):
    ##this returns what happens in a window this shows which key presses or handled
    for event in pygame.event.get():
        print(event)##this tells which event is done
    ##we just need to handle these events for game
        ##go to pygame.events docs for more events

        
        if event.type==pygame.QUIT:
            exit_game=True
##this ends the game when u click on cross of window

##For handling keypress in keyboard
        if event.type==pygame.KEYDOWN:
            if(event.key==pygame.K_RIGHT):
                print("right key pressed")

        
##when game loop ends the pygame should end and python should end
pygame.quit()
quit()

