# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
     
     screen.fill((0,0,0))
     pygame.display.flip()


if __name__ == "__main__":
    main()

#This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module.
#It's considered the "pythonic" way to structure an executable program in Python. Technically,
#the program will work fine by just calling main(), but you might get an angry letter from Guido van Rossum if you don't.