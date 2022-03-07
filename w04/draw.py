####### I WANT TO RANDOMIZE AT LEAST PART OF THIS PROGRAM
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
    paint_smoke(canvas, scene_width, scene_height, 100)

    paint_ground(canvas, scene_width, scene_height) 
    paint_smoke(canvas, scene_width, scene_height, 300)
    paint_pine_tree(canvas, 430, 150, 75)
    paint_dead_trees(canvas, scene_width, scene_height)
    paint_volcano(canvas, scene_width, scene_height)
    paint_lava(canvas, scene_width, scene_height)
    # paint_grid(canvas, scene_width, scene_height, 50)
    paint_middle_trees(canvas, scene_width, scene_width)
    paint_pine_tree(canvas, 200, 0, 120)
    paint_pine_tree(canvas, 700, scene_height / 3, 100)
    
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
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill='lightSkyBlue1')
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
        draw_oval(canvas, x0, y0, x1, y1, width=1, outline='gray70', fill='lavender')

def paint_ground(canvas, scene_width, scene_height):
    i = random.randint(1,4)
    if i == 1:
        color = 'mistyRose3'
    elif i == 2:
        color = 'seashell4'
    elif i == 3:
        color = 'burlywood4'
    else:
        color = 'navajoWhite3'
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill=color)

def paint_pine_tree(canvas, center_x, bottom, height):
    # draw trunk
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    top_trunk = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom, right_trunk, top_trunk, width=0, outline='tomato4', fill='tomato4')

    # draw skirt
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = top_trunk
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height
    skirt_center = center_x
    draw_polygon(canvas, skirt_left, skirt_bottom, skirt_center, skirt_top, skirt_right, skirt_bottom, outline='darkOliveGreen', fill='darkOliveGreen')

# draw volcano
def paint_volcano(canvas, width, height):
    draw_polygon(canvas, 50, 125, 450, 125, 375, 325, 325, 300, 275, 310, 200, 300, 175, 325, 140, 350, 125, 325, width=0, outline='red4', fill='red4')
    # round volcano base
    draw_oval(canvas, 50, 80, 450, 170, width=0, fill='red4')

# draw lava
def paint_lava(canvas, width, height):
    draw_polygon(canvas, 140, 350, 175, 325, 200, 300, 275, 310, 325, 300, 375, 325, 403, 250, 325, 275, 250, 200, 200, 250, 175, 275, 78, 200, 125, 325, width=0, outline='orangered1', fill='orangered1')

# draw smoke 
def paint_smoke(canvas, width, height, start):
    for i in range(start, height, random.randint(20, 35)):
        draw_oval(canvas, i - 50, i - 50, i + random.randint(25,105), i + random.randint(30, 75), width=1, outline='gray64', fill='gray44')
    
# draw dead trees
def paint_dead_trees(canvas, width, height):
    for i in range(int(round(height / 3)), 0, -50):
        bottom = i
        for j in range(0, width, random.randint(50, 75)):
            # trunk
            if j > 0 and j < 450 and bottom < 150 :
                continue
            else:   
                draw_polygon(canvas, j - 6, bottom, j + 6, bottom, j, bottom + 100, width=1, outline='gray36', fill='gray21')
                # draw branches
                draw_polygon(canvas, j, bottom + 60, j, bottom + 65, j + 20, bottom + 70, outline='gray36', fill='gray21')
                draw_polygon(canvas, j, bottom + 40, j, bottom + 43, j - 30, bottom + 60, outline='gray36', fill='gray21')

# draw a couple dead trees in the milddle to cover volcano edge
def paint_middle_trees(canvas, width, height):
    bottom = 70
    for j in range(0, width, random.randint(50, 75)):
        # trunk
        draw_polygon(canvas, j - 6, bottom, j + 6, bottom, j, bottom + 100, width=1, outline='gray36', fill='gray21')
        # draw branches
        draw_polygon(canvas, j, bottom + 60, j, bottom + 65, j + 20, bottom + 70, outline='gray36', fill='gray21')
        draw_polygon(canvas, j, bottom + 40, j, bottom + 43, j - 30, bottom + 60, outline='gray36', fill='gray21')

    bottom = 10
    for j in range(0, width, random.randint(50, 75)):
        # trunk
        draw_polygon(canvas, j - 6, bottom, j + 6, bottom, j, bottom + 100, width=1, outline='gray36', fill='gray21')
        # draw branches
        draw_polygon(canvas, j, bottom + 60, j, bottom + 65, j + 20, bottom + 70, outline='gray36', fill='gray21')
        draw_polygon(canvas, j, bottom + 40, j, bottom + 43, j - 30, bottom + 60, outline='gray36', fill='gray21')



main()