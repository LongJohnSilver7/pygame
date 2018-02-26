import os, sys
import time
import pygame
import random
from pygame.locals import *
from pygame import display 

def generate_randomvect(dimension, lower_bound_vector, upper_bound_vector):
    return tuple( random.randint(lower_bound_vector[c], upper_bound_vector[c]) for c in range(dimension))
    
    #print( tuple(lst + c for c in range(lower_bound,upper_bound, step))   ) 

if __name__ == "__main__": 

    os.environ['SDL_VIDEODRIVER'] = 'windib'
    pygame.display.set_caption('Something with vectors')
    
    pygame.init()

    if pygame.display.get_init():
        screen = pygame.display.set_mode((780,460))
        screen.fill((0, 0, 0))
        height = getattr(display.Info(), 'current_h')
        width = getattr(display.Info(), 'current_w')
        
        dim = 3
        lower_bound_vector = tuple(0 for i in range(dim))
        upper_bound_vector = (width,height, 0)
        
        num_vectors = 5
        vects = [generate_randomvect(dim, lower_bound_vector, upper_bound_vector) for i in range(num_vectors)]
        
        dotcolor = (255,255,255)
        for dot in vects:
            args = tuple(dot[i] for i in range(2))
            print(args)
            screen.set_at( args, dotcolor  )
        pygame.display.flip()
        while True:
            time.sleep(1)

   