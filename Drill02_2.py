import os
import math
from pico2d import *

os.chdir('D:\\2DGP\\Drill02')
open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')

x,y=0,0
center_x = 400
center_y = 300
radius = 200
angle=0

while(True):
    clear_canvas_now()
    grass.draw_now(400,30)

    x= center_x+radius*math.cos(angle)
    y= center_y+radius*math.sin(angle)
    
    character.draw_now(x,y)
    angle +=math.radians(1)
    
    delay(0.01)

close_canvas()
    
