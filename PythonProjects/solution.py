import pygame
pygame.init() #initializes a few things that you need

WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # displays window
pygame.display.set_caption("Pong") # sets name of window

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw(window):
    win.fill(BLACK) # fills entire window white
    pygame.display.update() # performs any of the drawing operations
    
def main():
    run = True
    clock = pygame.time.Clock()
    
    while run: #Loops that constantly runs that handles everything in game
        clock.tick(FPS) # cannot run faster than 60 fps
        draw(WINDOW)

        for event in pygame.event.get(): # gets all events, clicking mouse, clicking keyboard, exiting window, etc
            if event.type == pygame.QUIT: # checks if click exit, if you do, exits loop
                run = False
                break

    pygame.quit()

if __name__ == '__main__': # if solution.py is imported it in another file, it will not work because name will not be main
    main()

# next is making paddles