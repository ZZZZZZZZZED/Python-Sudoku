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
                window.blit(textinput.surface, pos)
                print('blit at {}'.format(pos))
                if isinstance(textinput.value, int):
                    module.overwrite(pos, textinput.value)
                    print(textinput.value)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("enter!")
                    print(textinput.value)
                    
        

        window.blit(board_surface,(0,0))

        for g in module.given_list:
            module.text_render(window, g)

        

        # Draw the log window
        window.blit(log_window, (0, 400))

        

        pygame.display.update()

        clock.tick(60)

if __name__=="__main__":
    
    pygame.init()
    main()