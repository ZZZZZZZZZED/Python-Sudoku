import pygame
import module
import pygame_textinput

from sys import exit

module.init_givens()



def main():
    pos = (0, 0)
    # Create TextInput-object
    textinput = pygame_textinput.TextInputVisualizer()
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
        window.fill((225, 225, 225))
        events = pygame.event.get()
        textinput.update(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos


        



        window.blit(board_surface,(0,0))

        for g in module.given_list:
            module.text_render(window, g)
        ### text input
        window.blit(textinput.surface, pos)
        if isinstance(textinput.value, int):
            module.overwrite(pos, textinput.value)
            print(textinput.value)
        pygame.display.update()
        clock.tick(60)

if __name__=="__main__":
    
    pygame.init()
    main()