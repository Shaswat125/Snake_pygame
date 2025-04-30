import pygame
import random
import os
from game_settings import GameSettings
from utils import Utility


class SnakeGame(GameSettings, Utility):
    def __init__(self):
        pygame.init()
        # Game Window settings
        self.width = 900
        self.height = 600
        self.gameWindow = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("The Vintage Snake Game")
        self.gameWindow.fill((192, 192, 192))

    def game_welcome_screen(self):
        # Setting Game Headers
        self.game_settings()
        exit_game = False
        # Welcome Screen for the game
        while not exit_game:
            self.gameWindow.fill((30, 60, 134))
            self.text_screen("Welcome to The Vintage Snake Game", self.white, 250, 30)
            self.text_screen("Rules are simple:", self.green, 20, 200)
            self.text_screen("1. Keep eating food and grow the snake until it hits a wall or its body.", self.yellow, 20, 280)
            self.text_screen("2. Remember, you lose when you turn the snake's head 180 degrees.", self.yellow, 20, 310)
            self.text_screen("3. Press 'Esc' Key anytime to exit the game.", self.cyan, 20, 400)
            self.text_screen("Press Enter to start!", self.white, 300, 450)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_RETURN:
                        self.gameloop()  # Start the game when Enter is pressed

            pygame.display.update()
            self.clock.tick(self.fps)

    def gameloop(self):
        exit_game = False
        game_over = False
        self.snk_list = []
        self.snk_length = 1
        self.x = 60
        self.y = 60
        self.speed_x = 5
        self.speed_y = 0
        self.last_direction = 'RIGHT'
        self.score = 0
        food_x = random.randint(30, self.width / 2)
        food_y = random.randint(30, self.height / 2)

        # Actual game starts
        while not exit_game:
            if game_over:
                with open("HighScore.txt", "w") as f:
                    f.write(str(self.hi_score))
                self.gameWindow.fill(self.white)
                self.gameWindow.blit(self.go, (0, 0))
                self.text_screen("Press Enter to play again", self.white, 300, 520)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.gameloop()  # Restart the game if Enter is pressed
                        if event.key == pygame.K_ESCAPE:
                            exit_game = True
                            pygame.quit()
                            quit()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        # Skipping reverse steps and increasing velocity for other steps
                        if event.key == pygame.K_RIGHT and self.last_direction != 'LEFT':
                            self.speed_x = self.in_velocity
                            self.speed_y = 0
                            self.last_direction = 'RIGHT'
                        elif event.key == pygame.K_LEFT and self.last_direction != 'RIGHT':
                            self.speed_x = -self.in_velocity
                            self.speed_y = 0
                            self.last_direction = 'LEFT'
                        elif event.key == pygame.K_UP and self.last_direction != 'DOWN':
                            self.speed_y = -self.in_velocity
                            self.speed_x = 0
                            self.last_direction = 'UP'
                        elif event.key == pygame.K_DOWN and self.last_direction != 'UP':
                            self.speed_y = self.in_velocity
                            self.speed_x = 0
                            self.last_direction = 'DOWN'
                        if event.key == pygame.K_c:
                            self.score += 100
                        if event.key == pygame.K_v:
                            self.in_velocity += 1
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            exit_game = True
                            pygame.quit()
                            quit()
                # Increasing speed
                self.x += self.speed_x
                self.y += self.speed_y

                if self.x > self.width or self.x < 0 or self.y < 0 or self.y > self.height:
                    game_over = True

                self.gameWindow.fill(self.white)
                self.text_screen(f"Score: {self.score}  High Score: {self.hi_score}", self.blue, 10, 10)
                self.plot_snake()
                pygame.draw.rect(self.gameWindow, self.orange, [food_x, food_y, self.sn_size, self.sn_size])

                if abs(self.x - food_x) < 15 and abs(self.y - food_y) < 15:
                    self.score += 10
                    food_x = random.randint(10, self.width / 1.5)
                    food_y = random.randint(10, self.height / 2)
                    self.snk_length += 5

                    if self.score > self.hi_score:
                        self.hi_score = self.score
                        with open("HighScore.txt", "w") as f:
                            f.write(str(self.hi_score))

                head = [self.x, self.y]
                self.snk_list.append(head)
                if len(self.snk_list) > self.snk_length:
                    del self.snk_list[0]

                if head in self.snk_list[:-1]:
                    game_over = True

            pygame.display.update()
            self.clock.tick(self.fps)
        # Exit game
        pygame.quit()
        quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.game_welcome_screen()

