import pygame
import os

class Utility:
    # Utility Class and Methods

    def text_screen(self, text, color, x, y):
        screen = self.font.render(text, True, color)
        self.gameWindow.blit(screen, (x, y))

    def plot_snake(self):
        for a, b in self.snk_list:
            pygame.draw.rect(self.gameWindow, self.dark_green, [a, b, self.sn_size, self.sn_size])
