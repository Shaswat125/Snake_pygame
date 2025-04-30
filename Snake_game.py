import pygame
import random
import os
pygame.init()
width = 900
height = 600

go = pygame.image.load("gameover.png")
go = pygame.transform.scale(go,(width,height))
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

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

font = pygame.font.SysFont(None, 33)

def text_screen(text, color, x, y):
    screen = font.render(text, True, color)  
    gameWindow.blit(screen, (x, y)) 

def plot_snake(gameWindow, color, snk_list, sn_size):
    for a,b in snk_list:
        pygame.draw.rect(gameWindow, dark_green, [a, b, sn_size, sn_size])

        
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
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                  gameloop()
           
            pygame.display.update()
            clock.tick(fps)

def gameloop():
    exit_game = False
    game_over = False
    x = 60
    y = 60
    sn_size = 20
    clock = pygame.time.Clock()
    fps = 60
    in_velocity = 5
    speed_x = 5
    speed_y = 0  
    last_direction = 'RIGHT'
    if not os.path.exists("HighScore.txt"):
        f = open("HighScore.txt", "w")
        f.write("0")
        f.close()
    f = open("HighScore.txt", "r")
    hi_score = f.read()
    f.close()
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
            gameWindow.blit(go, (0, 0))
            text_screen("Press enter to play again", white, 300, 520)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                        pygame.quit()
                        quit()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and last_direction != 'LEFT':
                        speed_x = in_velocity
                        speed_y = 0
                        last_direction = 'RIGHT'
                    elif event.key == pygame.K_LEFT and last_direction != 'RIGHT':
                        speed_x = -in_velocity
                        speed_y = 0
                        last_direction = 'LEFT'
                    elif event.key == pygame.K_UP and last_direction != 'DOWN':
                        speed_y = -in_velocity
                        speed_x = 0
                        last_direction = 'UP'
                    elif event.key == pygame.K_DOWN and last_direction != 'UP':
                        speed_y = in_velocity
                        speed_x = 0
                        last_direction = 'DOWN'
                    if event.key == pygame.K_c:
                        score += 100
                    if event.key == pygame.K_v:
                        in_velocity -= 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                        pygame.quit()
                        quit()
            x += speed_x
            y += speed_y
            if x > width or x < 0 or y < 0 or y > height:
                game_over = True
            gameWindow.fill(silver)
            text_screen("Score:" + str(score) + "  High Score:" + str(hi_score), blue, 10, 10)
            plot_snake(gameWindow, red, snk_list, sn_size)
            pygame.draw.rect(gameWindow, purple, [food_x, food_y, sn_size, sn_size])
            if abs(x - food_x) < 15 and abs(y - food_y) < 15:
                score += 10
                food_x = random.randint(10, width / 1.5)
                food_y = random.randint(10, height / 2)
                snk_length += 5
                if score > int(hi_score):
                    hi_score = score
                    f = open("HighScore.txt", "w")
                    f.write(str(hi_score))
                    f.close()
            head = []
            head.append(x)
            head.append(y)
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
        clock.tick(fps)
        pygame.display.update()
    pygame.quit()
    quit()

if True:
    welcome()
    gameloop()


