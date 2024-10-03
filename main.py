#1.
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  #6.
  Player.containers = (updatable, drawable)
  #6.1
  Asteroid.containers = (asteroids, updatable, drawable)
  #6.2
  AsteroidField.containers = updatable
  #7.
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  #7.1
  asteroid_field = AsteroidField()

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
    for obj in asteroids:
      if obj.collides(player):
        sys.exit("Game over!")
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
#5. creating two groups,then create one more group called asteroids and in the end create the shots group
#6. adding the Player to first two groups and adding Asteroid to all groups.
#6.1 this ensures that every instance of the Asteroid class is automatically added to these groups upon creation
#6.2 set the static containers field of the AsteroidField class to only the updatable group (it's not drawable, and it's not an 
     # asteroid itself)
#7. creating the player object
#7.1 create a new AsteroidField object in the initialization code
#8. creating a running loop
#9. creating a loop to check events that are occurring and make the X button of the frame responsive
#10. setting a background
#11. iterate over all "updatables" and .update() them, then iterate over all "drawables" and .draw() them, then iterate over asteroids and 
     # detect collisions using .collides()
#12. updating the display
#13. pausing the game loop until 1/60th of a second has passed
     # the .tick() method also returns the amount of time that has passed since the last time it was called: the delta time (dt variable)
#14. This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module.
     # It's considered the "pythonic" way to structure an executable program in Python. Technically,the program will work fine 
     # by just calling main(), but you might get an angry letter from Guido van Rossum if you don't.

