import pygame
import sys
import time
import random
pygame.init()

screen_width= 1000
screen_height=600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Selection Sort")
clock = pygame.time.Clock()

white=(255,255,255)
green=(0,128,0)
red=(255,0,0)

array=[]
sarray=[]

for i in range(100):
    a=random.randint(1, 200)
    array.append((white,[i*10,screen_height-a*2,9,a*2]))
    sarray.append(a*2)
run=True
while run:
    pygame.time.delay(100)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
    for i in range(100):
        color, (x, y, w, h)=array[i]
        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))
        
    for i in range(100):
        min_idx=i
        color, (x, y, w, h)=array[i]
        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))
            
        for j in range(i+1,100):
            color, (x, y, w, h)=array[j]
            pygame.draw.rect(screen, red, pygame.Rect(x, y, w, h))
    
            color, (x, y, w, h)=array[j]
            pygame.draw.rect(screen, white, pygame.Rect(x, y, w, h))
            
            
            if sarray[j] < sarray[min_idx]:
                min_idx=j
            j=j+1
        if min_idx!=i:
            color, (x, y, w, h)=array[min_idx]
            pygame.draw.rect(screen, red, pygame.Rect(x, y, w, h))
            
            dummy=sarray[min_idx]
            sarray[min_idx]=sarray[i]
            sarray[i]=dummy
            
            color, (x, y, w, h)=array[i]
            array[i]=green, (i*10, screen_height-dummy, 9, dummy)
            array[min_idx]=white, (min_idx*10, screen_height-h, 9, h)
        else:
            color, (x, y, w, h)=array[i]
            array[i]=green, (i*10, screen_height-h, 9, h)
        i=i+1
        
    pygame.display.update() 
    
pygame.quit()
sys.exit()
