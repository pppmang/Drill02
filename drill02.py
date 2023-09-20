from pico2d import *

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

def square():
    x=0
    y=0

    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 90)
        x+=5
        delay(0.01)

    x=800
    y=90

    while(y<600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y+=5
        delay(0.01)

    x=800
    y=600

    while(x>0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x-=5
        delay(0.01)

    x=0
    y=600

    while(y>60):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y-=5
        delay(0.01)
        

def circle():
    import math
    center_x=400
    center_y=300
    angle=0

    while(angle<360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        x=center_x+250*math.cos(math.radians(angle))
        y=center_y+250*math.sin(math.radians(angle))
        character.draw_now(x,y)
        angle+=2
        delay(0.01)
    

while(True):
    square()
    circle()
