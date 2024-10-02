#1.
import pygame
from constants import *
from player import Player

def main():
  #2.
  pygame.init()
  #3.
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  #4.
  clock = pygame.time.Clock()
  dt = 0
  
  #5.
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  #6.
  Player.containers = (updatable, drawable)
  #7.
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  #8.
  while True:
    #9.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
     
    #10.
    screen.fill((0,0,0))
    
    #11.
    for obj in updatable:
      obj.update(dt)
    for obj in drawable:
      obj.draw(screen)
    
    #12.
    pygame.display.flip()
    #13.
    dt = clock.tick(60) / 1000
  
#14.
if __name__ == "__main__":
  main()



#Explanation:
#1. this allows us to use code from the open-source pygame library throughout this file + import all infos from constants.py file
    # + import Player class from player.py file
#2. initialising the pygame
#3. creating display
#4. creating a clock object
#5. creating two groups
#6. adding the player to both groups
#7. creating the player object
#8. creating a running loop
#9. creating a loop to check events that are occurring and make the X button of the frame responsive
#10. setting a background
#11. iterate over all "updatables" and .update() them, then iterate over all "drawables" and .draw() them
#12. updating the display
#13. pausing the game loop until 1/60th of a second has passed
     # the .tick() method also returns the amount of time that has passed since the last time it was called: the delta time (dt variable)
#14. This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module.
     # It's considered the "pythonic" way to structure an executable program in Python. Technically,the program will work fine 
     # by just calling main(), but you might get an angry letter from Guido van Rossum if you don't.

