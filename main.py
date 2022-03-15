#import fun libraries!
import pygame, sys, time, random

pygame.init()

#setup screen size for game
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Cube Mode Activated")

cubeSize = 20

#RGB color
amber = (255, 198, 0)
blue = (5, 195, 221)
green = (0, 110, 51)
gray = (99, 102, 106)
bigcolor = (205, 150, 0)

food = [random.randrange(1, 500), random.randrange(1, 500), 10, 10]
bfood = [random.randrange(1, 500), random.randrange(1, 500), 10, 10]

cubex = 250
cubey = 250

speed = 5

run = True

while run:
  pygame. time.delay(10)
  window.fill(gray)
