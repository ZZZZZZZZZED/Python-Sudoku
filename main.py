import pygame
import module
import view
import datetime
import pygame_textinput

from sys import exit

init = False
module.init_givens()
view.init_highlight_pos()

# Set up the log messages list
log_messages = []

# Define a function for adding a new log message
def add_log_message(message):
    log_messages.append(message)

def main():
    global init
    pos = (0, 0)
    module.input = 0
    # Create TextInput-object
    textinput = pygame_textinput.TextInputVisualizer()
    window = pygame.display.set_mode(size=(400,500))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,50)
    board_surface = pygame.image.load('graphics/board.png').convert()

    # boarder png 
    boarder_surface = pygame.image.load('graphics/boarder.png')
    # scale boarder to proper size
    boarder_surface = pygame.transform.scale(boarder_surface, (44, 44))

    # Create the log window
    log_window = pygame.Surface((400, 100))

    # Set up the font for rendering text
    font = pygame.font.Font(None, 36)




    while True:
        window.fill((225, 225, 225))
        events = pygame.event.get()
        textinput.update(events)



        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = (event.pos[0] - 11, event.pos[1] - 11)

            elif event.type == pygame.KEYDOWN and module.check_available(pos):
                if event.unicode == '/r':
                    print("enter!")
                elif event.unicode == '1':
                    module.input = 1
                elif event.unicode == '2':
                    module.input = 2
                elif event.unicode == '3':
                    module.input = 3
                elif event.unicode == '4':
                    module.input = 4
                elif event.unicode == '5':
                    module.input = 5
                elif event.unicode == '6':
                    module.input = 6
                elif event.unicode == '7':
                    module.input = 7
                elif event.unicode == '8':
                    module.input = 8
                elif event.unicode == '9':
                    module.input = 9
                elif event.unicode == '/b' or '0':
                    module.input = 0
                module.overwrite(pos, module.input)
                


        window.blit(board_surface,(0,0))

        # Render givens
        for g in module.given_list:
            module.text_render(window, g, pos)



        
        # Draw the log window
        window.blit(log_window, (0, 400))

        # Draw highlight boarder
        # +8 means pos fix; for consistency of showing pos and logical pos
        if module.check_available(pos):
            window.blit(boarder_surface, (view.find_gridpos_by_click(pos)[0] + 8, view.find_gridpos_by_click(pos)[1] + 8))
                        
        

        pygame.display.update()

        clock.tick(30)

if __name__=="__main__":
    
    pygame.init()
    main()