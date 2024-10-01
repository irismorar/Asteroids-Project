# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *
from player import Player

def main():
  # initialising the pygame
  pygame.init()
  # creating display
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  # creating the player object:
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
  # creating a clock object
  clock = pygame.time.Clock()
  dt = 0
  
  # creating a running loop
  while True: 
     # creating a loop to check events that are occurring and make the X button of the frame functionable
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
     
     # setting a background
     player.update(dt)
     screen.fill((0,0,0))
     player.draw(screen)
     # updating the display
     pygame.display.flip()

     # pausing the game loop until 1/60th of a second has passed
     # the .tick() method also returns the amount of time that has passed since the last time it was called: the delta time (dt variable)
     dt = clock.tick(60) / 1000
  


if __name__ == "__main__":
    main()
#This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module.
#It's considered the "pythonic" way to structure an executable program in Python. Technically,
#the program will work fine by just calling main(), but you might get an angry letter from Guido van Rossum if you don't.