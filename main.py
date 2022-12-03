import pygame
import module
# import pygame_textinput

from sys import exit


### text input
# textinput = pygame_textinput.TextInputVisualizer()
###
module.init_givens()



def main():
    window = pygame.display.set_mode(size=(400,500))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,50)
    board_surface = pygame.image.load('graphics/board.png').convert()
    note_surface = pygame.Surface((500,100))
    note_surface.fill('Grey')
    text_surface = font.render("9", True, "BLACK")
    num_rect = board_surface.get_rect(topleft =(55,55))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        ### text input
        # events = pygame.event.get()
        # textinput.update(events)
        # window.blit(textinput.surface, (20, 20))
        ###
        window.blit(board_surface,(0,0))
        window.blit(text_surface,(63,55))
        window.blit(text_surface,(63,13))
        window.blit(text_surface,(63,55))
        window.blit(note_surface,(0,400))
        pygame.display.update()
        clock.tick(60)

if __name__=="__main__":
    pygame.init()
    main()