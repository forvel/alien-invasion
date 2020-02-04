import sys
import pygame
from pygame.locals import *

def run_game():
# Инициализирует игру и создает объект экрана
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Alien Invasion")
    bgColor = (230,230,230)
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        screen.fill(bgColor)
        pygame.display.flip()
#end run_game
run_game()
