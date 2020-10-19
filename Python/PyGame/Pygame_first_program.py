# Library can be found online at https://www.pygame.org/news

import pygame

def main():
    pygame.init()
    pygame.display.set_caption("first program")

    screen = pygame.display.set_mode((240,180))

    running = True

    while running:
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False   

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()