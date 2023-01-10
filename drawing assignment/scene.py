# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from turtle import width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    
    draw_pine_tree(canvas, 325, 100, 200)
    draw_pine_tree(canvas, 475, 100, 200)
    draw_pine_tree(canvas, 250, 75, 200)
    draw_pine_tree(canvas, 400, 75, 200)
    draw_clouds(canvas)
    draw_building(canvas)
    draw_birds(canvas)
    
    
    draw_grid(canvas, scene_width, scene_height, 50)
    

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


def draw_grid(canvas, width, height, interval):
     label_y = 15
     for x in range(interval, width, interval):
                draw_line(canvas, x, 0, x, height)
                draw_text(canvas, x, label_y, f"{x}")
     label_x = 15
     for y in range (interval, height, interval):
                draw_line(canvas, 0, y, width, y)
                draw_text(canvas, label_x, y, f"{y}")



# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")


def draw_clouds(canvas):
    #use the oval to draw a cloud
    draw_oval(canvas, 100, 400, 350, 500, fill="white")
    draw_oval(canvas, 400, 400, 650, 500, fill="white")
        



def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

def draw_building(canvas):
    draw_rectangle(canvas, 600, 50, 750, 400, width=1, fill="sandyBrown")
    draw_rectangle(canvas, 650, 100, 700, 150, fill="blue1")
    draw_rectangle(canvas, 650, 200, 700, 250, fill="blue1")
    draw_rectangle(canvas, 650, 300, 700, 350, fill="blue1")

def draw_birds(canvas):
    draw_polygon(canvas,
        50, 400, 75, 350, 100, 400, 75, 370, 50, 400, fill="black")

    draw_polygon(canvas,
        100, 375, 125, 325, 150, 375, 125, 345, 100, 375, fill="black")

    draw_polygon(canvas,
        150, 400, 175, 350, 200, 400, 175, 370, 150, 400, fill="black")

    draw_polygon(canvas,
        200, 400, 225, 350, 250, 400, 225, 370, 200, 400, fill="black")

    draw_polygon(canvas,
        250, 375, 275, 325, 300, 375, 275, 345, 250, 375, fill="black")

    draw_polygon(canvas,
        300, 400, 325, 350, 350, 400, 325, 370, 300, 400, fill="black")
    
    draw_polygon(canvas,
        350, 400, 375, 350, 400, 400, 375, 370, 350, 400, fill="black")

    draw_polygon(canvas,
        400, 375, 425, 325, 450, 375, 425, 345, 400, 375, fill="black")

    draw_polygon(canvas,
        450, 400, 475, 350, 500, 400, 475, 370, 450, 400, fill="black")
    
    
    
    """This is something I tried for repeating the birds but it didn't work...


    for i in range(scene_width):
        i += 50
        draw_polygon(canvas, i, 400, i + 25, 350, i + 50, 400, i + 25, 370, i, 400, fill="white")"""
        




def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()