import os
import math
from pico2d import *

os.chdir('D:\\2DGP\\Drill02')

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')



x=400
y=90
direction=1

while(True):
    clear_canvas_now()
    grass.draw_now(400,30)
    
    if direction==1:
        if x<800:
            character.draw_now(x, y)
            x += 5
        else:
            direction=2
            
    elif direction==2:
        if y<600:
            character.draw_now(x, y)
            y +=5
        else:
            direction=3
            
    elif direction==3:
        if x>0:
            character.draw_now(x, y)
            x -=5
        else:
             direction=4
             
    elif direction==4:
        if y>90:
            character.draw_now(x, y)
            y -=5
        else:
            direction=1
        

delay(1)
close_canvas()


