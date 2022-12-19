import pygame_textinput
import pygame

def main():


    x = 0
    y = 0

            

    

    # Create TextInput-object
    textinput = pygame_textinput.TextInputVisualizer()

    screen = pygame.display.set_mode((1000, 200))
    clock = pygame.time.Clock()

    while True:
        
        screen.fill((225, 225, 225))

        events = pygame.event.get()

        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        # screen.blit(textinput.surface, (10, 10))

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                print(x,y)
        screen.blit(textinput.surface, (x, y))    
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    main()