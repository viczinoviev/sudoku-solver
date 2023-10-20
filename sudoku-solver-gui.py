import pygame
from classes import Cube

def main():
    #pygame setup
    pygame.init()
    screen = pygame.display.set_mode((720,800))
    time = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill("white")
        
        pygame.display.flip()
        
        time.tick(60)
    
main()
pygame.quit()