import os, sys
import time
import pygame
import random
from pygame.locals import *
from pygame import display 
import inspect
from itertools import chain

#generators always return two entries to be flipped with ids
class Algorithms:
    def bubblesort_generator(unsorted_list):
        
        itemcount = len(unsorted_list)
        for j in range(itemcount):
            for i in range(itemcount-j-1): 
                if unsorted_list[i]<unsorted_list[i+1]:
                    yield l_swap(unsorted_list,i, i+1)

    def quicksort_generator(unsorted_list, lower, upper):
        if lower >= upper:
            return
        
        ind_pivot = lower
        val_pivot = unsorted_list[ind_pivot]
        
        ind_upper = upper
        ind_lower = lower+1
   
        if ind_upper <= ind_lower:
            return

        fix = True

        while(ind_upper > ind_lower):
            print('calculating')
            swp_lower = None
            for i in range(ind_lower,upper+1):
                if unsorted_list[i]>val_pivot:
                    ind_lower = i
                    swp_lower = i
                    break

            swp_upper = None
            for j in range(ind_upper,lower, -1):
                if unsorted_list[j]<val_pivot:
                    ind_upper = j
                    swp_upper = j
                    break
   

            if swp_upper != None and swp_lower != None:  
                yield l_swap(unsorted_list, swp_lower, swp_upper)
            elif swp_upper is None and swp_lower is None:
                return
            elif swp_upper is None:
                fix = False
                break
            elif swp_lower is None:
                yield l_swap(unsorted_list, ind_pivot, ind_upper)
                ind_pivot = ind_upper
                fix = False
                break


        if fix == True:
            yield l_swap(unsorted_list, swp_lower, swp_upper)
            yield l_swap(unsorted_list, ind_pivot, swp_upper)
            ind_pivot = swp_upper
        
        
        rec_lower = Algorithms.quicksort_generator(unsorted_list, lower, ind_pivot-1)
        rec_upper = Algorithms.quicksort_generator(unsorted_list, ind_pivot+1,upper)
        rec = chain(rec_lower, rec_upper)
        for k in rec:
            yield k

    def pivot_heuristic(lst):
        # round down
        return round(len(lst)/2)  

    lst_algos = {'bubblesort': bubblesort_generator, 'quicksort': quicksort_generator}




def generate_randomsequence(lower_bound, upper_bound, length):
    return [random.randint(lower_bound, upper_bound) for i in range(length)]
    
    #print( tuple(lst + c for c in range(lower_bound,upper_bound, step))   ) 

def drawline_straight(screen, position, color,  length, frameheight):
    strt = (position,frameheight)
    fin = (position,frameheight-length)
    pygame.draw.line(screen,color, strt, fin)

def delline_straight(screen, position, backgroundcolor, frameheight):
    drawline_straight(screen, position, backgroundcolor, frameheight, frameheight )



def l_swap(lst, in1, in2):
    temp = lst[in2]
    lst[in2] = lst[in1]
    lst[in1] = temp
    return (in1, lst[in1], in2, lst[in2])

def start_sort(unsorted_list, identifier, frameheight, backgroundcolor):
    global algorithms
    fnct = Algorithms.lst_algos.get(identifier, None)
    #print(fnct)
    if identifier == 'quicksort':
        fnct = fnct(unsorted_list, 0, len(unsorted_list)-1)
    else:
        fnct = fnct(unsorted_list)
    
    pygame.display.set_caption('Sortingalgorithms' + ' | ' + identifier  )

    #print(fnct)
    color = (255,255,255)
    if fnct is not None:
        for i in fnct:
            #print(i)
            in1 = i[0]
            len1 = i[1]
            in2 = i[2]
            len2 = i[3]
            delline_straight(screen, in1, backgroundcolor, frameheight)
            delline_straight(screen, in2, backgroundcolor, frameheight)
            drawline_straight(screen, in1, color, len1, frameheight)
            drawline_straight(screen, in2, color, len2, frameheight)
            pygame.display.flip()
            #print( in1, in2)







if __name__ == "__main__": 

    os.environ['SDL_VIDEODRIVER'] = 'windib'

    
    pygame.init()
    pygame.display.set_caption('Sortingalgorithms')
    if pygame.display.get_init():
        screen = pygame.display.set_mode((780,460))
        bckgr = (0,0,0)
        screen.fill(bckgr)
        height = getattr(display.Info(), 'current_h')
        width = getattr(display.Info(), 'current_w')
        

        lower_bound = 0
        upper_bound = height
        
        length = width
        numbers_unsorted = generate_randomsequence(lower_bound, upper_bound, length)
        #numbers_unsorted = [i for i in range(100,200)]
        #numbers_unsorted += [i for i in range(0,100)]
        #print(numbers_unsorted)
        clr = (255,255,255)
        for ind, num in enumerate(numbers_unsorted):
            drawline_straight(screen,ind,clr, num, height)
        pygame.display.flip()
        time.sleep(1)
        algorithm = 'bubblesort'
        print(numbers_unsorted)
        start_sort(numbers_unsorted, algorithm, height, bckgr)
        
        #for i in range(100):
            #delline_straight(screen, i , bckgr, height)
        
        
        print(numbers_unsorted)
        pygame.display.flip()
        while True:
            time.sleep(1)

   