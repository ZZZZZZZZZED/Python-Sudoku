import pygame
import datetime

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 500)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('My Pygame Window')

# Create the log window
log_window = pygame.Surface((400, 100))

# Set up the font for rendering text
font = pygame.font.Font(None, 36)

# Set up the log messages list
log_messages = []

# Define a function for adding a new log message
def add_log_message(message):
    log_messages.append(message)

# Run the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            # Get the current local time
            current_time = datetime.datetime.now()

            # Format the time as a string
            time_string = current_time.strftime('%Y-%m-%d %H:%M:%S')

            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Format the mouse position as a string
            mouse_string = f'Mouse position: ({mouse_x}, {mouse_y})'

            # Add the time and mouse position strings to the log messages
            add_log_message(time_string)
            add_log_message(mouse_string)

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Fill the log window with black
    log_window.fill((0, 0, 0))

    # Render the log messages onto the log window
    for i, message in enumerate(log_messages):
        text = font.render(message, True, (255, 255, 255))
        log_window.blit(text, (10, 10 + i * 36))

    # Draw the log window
    screen.blit(log_window, (0, 400))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

