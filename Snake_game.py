import pygame
import random
import os
pygame.mixer.init()
pygame.init()

width = 900
height = 600

#to add image in game this func
go = pygame.image.load("gameover.png")
go = pygame.transform.scale(go,(width,height))

#to add music in game this func
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

#These are the colors used in the game
yellow=(255,255,0)
cyan=(0,255,255)
magneta=(255,0,255)
silver=(192,192,192)
white = (255, 255, 255)
purple="#6e2f98"
red = (255, 0, 0)
green = (0, 255, 0)
dark_green="#59982f"
blue = (0, 0, 255)
black = (0, 0, 0)

gameWindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Vintage Snake game")
pygame.display.update()

#font for entire game and its size
font = pygame.font.SysFont(None, 33)
def text_screen(text, color, x, y):
    screen = font.render(text, True, color)  
    gameWindow.blit(screen, (x, y)) 


def plot_snake(gameWindow, color, snk_list, sn_size):
    for a,b in snk_list:
        pygame.draw.rect(gameWindow, dark_green, [a, b, sn_size, sn_size])
    #it display every element of the snk_list and append accordingly

#The Welcome screen of the game
def welcome():
    fps=60
    clock = pygame.time.Clock()
    exit_game=False
    while not exit_game:
        gameWindow.fill((30,60,134))
        text_screen("Welcome to The Vintage Snake game", white,250,30)
        text_screen("Rules are simple:" , green,20,200)
        text_screen("Keep eating food and grow the snake until it hits a wall or it's body." , yellow,20,280)
        text_screen("Remember you lose when you turn it's head 180 degrees at a point." , yellow,20,310)
        text_screen("Press 'Esc' Key anytime to end the game.", cyan, 20, 400)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            ##print(event)
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                  gameloop()
           
            pygame.display.update()
            clock.tick(fps)



##  Game Loop
def gameloop():
    exit_game = False
    game_over = False
    x = 60  ##initial position of snake
    y = 60
    sn_size = 20
    clock = pygame.time.Clock()  #
    fps = 60
    in_velocity = 5
    speed_x = 5
    speed_y = 0  
    # make score print on display board


    if(not os.path.exists("HighScore.txt")):
        f = open("HighScore.txt", "w")
        f.write("0")
        f.close()

    f = open("HighScore.txt", "r")
    hi_score = f.read()
    f.close()
 
    ##for increasing length of snake
    snk_list = [] 
    snk_length = 1


    food_x = random.randint(30, width / 2)
    food_y = random.randint(30, height / 2)
    score = 0 

    while not exit_game:
        if game_over:
            f = open("HighScore.txt", "w")
            f.write(str(hi_score))
            f.close()
            gameWindow.fill(silver)
            gameWindow.blit(go,(0,0))
     
            text_screen("Press enter to play again", white, 300, 520)
             
            for event in pygame.event.get():
                ##print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                        pygame.quit()
                        quit()
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
                        speed_y = -in_velocity
                        speed_x = 0

                    if event.key == pygame.K_DOWN:
                        speed_y = in_velocity
                        speed_x = 0
                    #For cheat codes, to increase score without eating food is c
                    if event.key == pygame.K_c:
                        score+=100
                    #cheat code to decrease velocity is v
                    if event.key == pygame.K_v:
                        in_velocity-=1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                        pygame.quit()
                        quit()

            # changing speed
            x += speed_x
            y += speed_y

            if x>width or x<0 or y<0 or y>height:
                game_over=True

            gameWindow.fill(silver)
            text_screen("Score:" + str(score)+ "  High Score:"+str(hi_score), blue, 10, 10)
            ##prints score on display


            plot_snake(gameWindow,red, snk_list,sn_size)

            pygame.draw.rect(gameWindow, purple, [food_x, food_y, sn_size, sn_size])
            if abs(x - food_x) < 15 and abs(y - food_y) < 15:
                score += 10

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
            head.append(x)
            head.append(y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
            ##[:-1] is to stop taking last element

        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    quit()

if True:
    welcome()
    gameloop()


