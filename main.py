import pygame
import module
import datetime
import pygame_textinput

from sys import exit

module.init_givens()

# Set up the log messages list
log_messages = []

# Define a function for adding a new log message
def add_log_message(message):
    log_messages.append(message)

def main():
    pos = (0, 0)
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
    boarder_surface = pygame.transform.scale(boarder_surface, (40, 40))

    # Create the log window
    log_window = pygame.Surface((400, 100))

    # Set up the font for rendering text
    font = pygame.font.Font(None, 36)

    text_surface = font.render("9", True, "BLACK")


    while True:
        window.fill((225, 225, 225))
        events = pygame.event.get()
        textinput.update(events)



        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                ### text input
                # if module.check_available(pos):
                print(module.check_available(pos))
                window.blit(boarder_surface,(pos))
                
                print('blit at {}, value is {}'.format(pos, textinput.value))

            elif event.type == pygame.KEYDOWN and module.check_available(pos):
                if event.unicode == '/r':
                    print("enter!")
                elif event.unicode == '1':
                        module.overwrite(pos, 1)
                elif event.unicode == '2':
                        module.overwrite(pos, 2)
                elif event.unicode == '3':
                        module.overwrite(pos, 3)
                elif event.unicode == '4':
                        module.overwrite(pos, 4)
                elif event.unicode == '5':
                        module.overwrite(pos, 5)
                elif event.unicode == '6':
                        module.overwrite(pos, 6)
                elif event.unicode == '7':
                        module.overwrite(pos, 7)
                elif event.unicode == '8':
                        module.overwrite(pos, 8)
                elif event.unicode == '9':
                        module.overwrite(pos, 9)

                
                    
        

        window.blit(board_surface,(0,0))

        for g in module.given_list:
            module.text_render(window, g)
        
        

        # Draw the log window
        window.blit(log_window, (0, 400))

        # draw highlight boarder
        for i in range(9):
            for j in range(9):
                x = i * 42.5
                y = j * 42.5
                posi = (x,y)
                if module.check_available(posi):
                    window.blit(boarder_surface, (x+8, y+8))
                
        

        pygame.display.update()

        clock.tick(60)

if __name__=="__main__":
    
    pygame.init()
    main()