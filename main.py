import pygame
from constants import *



def main():
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        
# This kills game screen by making the "x" work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            #this is the screen.  You dont need to call pygame again while in a pygame init
        screen.fill(color=(0, 0, 0), rect = None, special_flags=0)

        pygame.display.flip()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()