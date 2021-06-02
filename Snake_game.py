import pygame
import random



pygame.init()
width = 900
height = 600
##Game window
gameWindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vintage Snake game")
pygame.display.update()

font = pygame.font.SysFont(None, 40)

def text_screen(text, color, x, y):
    screen = font.render(text, True, color)  ##this take 3 variables and print in window
    gameWindow.blit(screen, (x, y))  ##blit func prints in on screen
#the snake function makes the length of the snake


def plot_snake(gameWindow, color, snk_list, sn_size):
    for a,b in snk_list:
        pygame.draw.rect(gameWindow, red, [a, b, sn_size, sn_size])
    # print(snk_list)
    ## display every element of the snk_list and append accordingly

#Welcome screen of the game
def welcome():
    fps=60
    clock = pygame.time.Clock()
    exit_game=False
    while not exit_game:
        gameWindow.fill((45,67,88))
        text_screen("Welcome to Snake game, Press Enter", black,180,245)
        text_screen("Press Esc to end", white, 220, 305)
        for event in pygame.event.get():
            ##print(event)
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                  gameloop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            pygame.display.update()
            clock.tick(fps)
            # after every change update


##Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)



##Game Loop
def gameloop():
    ##Game specific varibles
    exit_game = False
    game_over = False
    x = 60  ##initial position of snake
    y = 60
    sn_size = 20
    clock = pygame.time.Clock()  # it handles the clock of game
    fps = 60
    in_velocity = 5
    speed_x = 5
    speed_y = 0  ##we give speed or velocity to our snake
    ##lets make score print on display board

    ##Now we put high score to our program
    f = open("HighScore.txt", "r")
    hi_score = f.read()
    f.close()
    ##another way to store high
    # with open("Highscore.txt","r") as f:
    #     hi_score=f.read()

    ##for increasing length of snake
    snk_list = []  ##we make a empty list and increase it but we make it list of list using head list
    snk_length = 1

    ##lets make food for our snake random function returns random variable between a nad b
    food_x = random.randint(30, width / 2)
    food_y = random.randint(30, height / 2)
    score = 0  ##for making score go up


    while not exit_game:
        if game_over:
            f = open("HighScore.txt", "w")
            f.write(str(hi_score))
            f.close()
            gameWindow.fill(white)
            text_screen("Game Over! Press enter to play again.", black, 170, 240)
            for event in pygame.event.get():
                ##print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        #this was to make game over when snake hits walls and ask to restart

        else:
            for event in pygame.event.get():
                ##print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        speed_x = in_velocity
                        speed_y = 0

                    if event.key == pygame.K_LEFT:
                        speed_x = -in_velocity
                        speed_y = 0

                    if event.key == pygame.K_UP:
                        speed_x = 0
                        speed_y = -in_velocity
                       

                    if event.key == pygame.K_DOWN:
                        speed_x = 0
                        speed_y = in_velocity
                        
                    #For cheat codes, to increase score without eating food is c
                    if event.key == pygame.K_c:
                        score+=10
                    #cheat code to decrease velocity is v
                    if event.key == pygame.K_v:
                        in_velocity-=1

            # changing speed
            x += speed_x
            y += speed_y

            if x>width or x<0 or y<0 or y>height:
                game_over=True
                # print("Game over")
            # window color
            gameWindow.fill(white)
            text_screen("Score:" + str(score)+ "  High Score:"+str(hi_score), blue, 15, 15)
            ##prints score on display

            ##Making head of snake
            # pygame.draw.rect(gameWindow, red, [x, y, sn_size, sn_size])
            ##now we make heads of head by a func
            plot_snake(gameWindow,red, snk_list,sn_size)##this plots the coordinates to areas
            ##snk_list contains the coordinates of the positions


            ##making food and eating it
            pygame.draw.rect(gameWindow, green, [food_x, food_y, sn_size, sn_size])
            if abs(x - food_x) < 15 and abs(y - food_y) < 15:
                score += 10
                ##print("Score:", score)
                food_x = random.randint(10, width / 1.5)
                food_y = random.randint(10, height / 2)
                snk_length+=5
                #only when the snake eats food its size should be increased
                if score>int(hi_score):
                    hi_score=score
                    f = open("HighScore.txt", "w")
                    f.write(str(hi_score))
                    f.close()


            #we append head because initially we need a head
            head=[]
            head.append(x)#it stores the previous value of head bcz x and y changes in every loop
            head.append(y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]

            #only when the snake eats food its size should be increased done by del
            #whenever size of snake is more than len we del first element. Snk_len controls the size of snk,list

            #Now we end the game when snake hits its own body, snk_list has all coordinates of the snake
            #When snake hits any coordinate that the list has except the last coordinate the game is over
            #the last coordinate is the head of snake we need to find whether any other coordinates matches
            # or not. The if here iterates for all values in snk list except last and checks for head
            if head in snk_list[:-1]:
                game_over=True
            ##[:-1] is to stop taking last element

        ##how many frames in one sec
        clock.tick(fps)
        # after every change update
        pygame.display.update()

    pygame.quit()
    quit()

welcome()
gameloop()
#We make the whole game loop and its variables inside a game loop funct and call that fun when u press enter

