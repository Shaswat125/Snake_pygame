import random
import pygame
import os

class GameSettings:

    def color_setup(self):
        # To setup or change game colors
        self.yellow = (255, 255, 0)
        self.cyan = (0, 255, 255)
        self.magneta = (255, 0, 255)
        self.silver = (192, 192, 192)
        self.white = (255, 255, 255)
        self.purple = "#6e2f98"
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.dark_green = "#59982f"
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.orange=(255, 165, 0)

    def font_setup(self):
        # To setup or change game font
        self.font = pygame.font.SysFont(None, 33)

    def game_settings(self):
        # Game state variables
        self.font_setup()
        self.color_setup()
        self.sn_size = 20
        self.snk_list = []
        self.snk_length = 1
        self.x = 60
        self.y = 60
        self.speed_x = 5
        self.speed_y = 0
        self.last_direction = 'RIGHT'
        self.score = 0
        self.in_velocity = 5
        self.game_over = False
        # High Score file retrieved and udated
        if not os.path.exists("HighScore.txt"):
            with open("HighScore.txt", "w") as f:
                f.write("0")
        with open("HighScore.txt", "r") as f:
            self.hi_score = int(f.read().strip())

        # Music and Game Over image dislayed
        self.go = pygame.image.load("gameover.png")
        self.go = pygame.transform.scale(self.go, (self.width, self.height))
        pygame.mixer.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play()

        # FPS clock for the game
        self.clock = pygame.time.Clock()
        self.fps = 60
