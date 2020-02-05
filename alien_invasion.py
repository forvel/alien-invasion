import sys
import pygame
from pygame.locals import *

def run_game():
# Инициализирует игру и создает объект экрана
    pygame.init()
    gameSettings = Settings()
    screen = pygame.display.set_mode((gameSettings.screenWidth, gameSettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        screen.fill(gameSettings.bgColor)
        pygame.display.flip()
#end run_game
run_game()
