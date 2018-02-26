import os, sys
import time
import random
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Psychedelic testenvironment')
screen = pygame.display.set_mode((500, 500))

screen.fill((0, 0, 0))

screen_w = screen.get_width()
screen_h = screen.get_height()

stepsize = 10
clr = (0,0,255)

rev = False
while True:
    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    
    if rev is False:
        stepsize = stepsize-1
        if stepsize == 1:
            rev = True
    else:
        stepsize +=1
        if stepsize == 10:
            rev = False

    for i in range(0,screen_w,stepsize):
        pygame.draw.line(screen,clr, (0,screen_h-i),(i,0))
        pygame.draw.line(screen,clr,(i,0),(screen_w,i))
        pygame.draw.line(screen,clr,(screen_w,i),(screen_w-i,screen_h))
        pygame.draw.line(screen,clr,(screen_w-i,screen_h),(0,screen_h-i))
        pygame.display.flip()
        time.sleep(0.01)
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    clr = (r,g,b)
