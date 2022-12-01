import pygame
from sys import exit

pygame.init()

def main():
    window = pygame.display.set_mode(size=(500,500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

if __name__=="__main__":
    # call the main function
    main()