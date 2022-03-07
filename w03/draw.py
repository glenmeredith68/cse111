####### I WANT TO RANDOMIZE AT LEAST PART OF THIS PROGRAM
from this import d
from turtle import width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    #Call the start_drawing function in the draw2d.py library which will open a window and create a canvas.
    canvas = start_drawing('Scene', scene_width, scene_height)
    
    #Call drawing functions here fron back to front of scene
    paint_sky(canvas, scene_width, scene_height)
    paint_ground(canvas, scene_width, scene_height)
    paint_grid(canvas, scene_width, scene_height, 50)

    paint_pine_tree(canvas, 100, 50, 250)
    paint_pine_tree(canvas, 700, 70, 150)
    
    # Call the finish_drawing function in the draw2d.py library.
    finish_drawing(canvas)

# Define drawing functions here. 
def paint_grid(canvas, width, height, interval):
    label_y = 15
    # draw vertical lines
    for x in range(interval, width, interval):
        # draw_line(canvas,x, 0, 30, height) This one draws a cool splash of rays!
        draw_line(canvas,x, 0, x, height)
        draw_text(canvas, x, label_y, f'{x}')
        
        # Draw horixontal lines
        label_x = 15
        for y in range(interval, height, interval):
            draw_line(canvas,0, y, width, y)
            draw_text(canvas, label_x, y, f'{y}')
def paint_sky(canvas, scene_width, scene_height):
    # draws sky and clouds
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill='cornflowerBlue')
    i = 1 
    while i != 0:
        if i > 5:
            x0 = scene_width / random.randint(2, 10)
        else:
            x0 = scene_width - (scene_width / random.randint(2, 10))
            
        i = random.randint(0,10)
        y0 = scene_height - (scene_height / random.randint(2, 5))
        x1 = x0 + random.randint(80, 200)
        y1 = y0 + random.randint(20, 120)
        draw_oval(canvas, x0, y0, x1, y1, width=0, fill='lavender')

def paint_ground(canvas, scene_width, scene_height):
    i = random.randint(1,4)
    if i == 1:
        color = 'coral4'
    elif i == 2:
        color = 'seashell4'
    elif i == 3:
        color = 'burlywood4'
    else:
        color = 'saddleBrown'
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill=color)

def paint_pine_tree(canvas, center_x, bottom, height):
    # draw trunk
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    top_trunk = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom, right_trunk, top_trunk, fill='tomato4')

    # draw skirt
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = top_trunk
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height
    skirt_center = center_x
    draw_polygon(canvas, skirt_left, skirt_bottom, skirt_center, skirt_top, skirt_right, skirt_bottom, fill='darkOliveGreen')

main()