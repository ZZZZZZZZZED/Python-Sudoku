import pygame
from sys import exit

pygame.init()

def main():
    window = pygame.display.set_mode(size=(400,500))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,50)
    board_surface = pygame.image.load('graphics/board.png')
    note_surface = pygame.Surface((500,100))
    note_surface.fill('White')
    text_surface = font.render("My game", True, "BLACK")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        window.blit(board_surface,(0,0))
        window.blit(text_surface,(0,0))
        window.blit(note_surface,(0,400))
        pygame.display.update()
        clock.tick(60)

if __name__=="__main__":
    # call the main function
    main()