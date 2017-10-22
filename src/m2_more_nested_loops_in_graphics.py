"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and JaeJung Hyun.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    upperleft=rectangle.corner_1
    lowerright=rectangle.corner_2
    upperleft1=rectangle.corner_1
    lowerright1=rectangle.corner_2

    height=rectangle.get_height()
    width=rectangle.get_width()

    for k in range(n):
        for j in range(k+1):
            rect=rg.Rectangle(upperleft, lowerright)
            rect.attach_to(window)
            window.render(.05)

            lowerright=rg.Point(lowerright.x+width,lowerright.y)
            upperleft=rg.Point(upperleft.x+width,upperleft.y)

        lowerright1=rg.Point(lowerright1.x-width/2,lowerright1.y-height)
        upperleft1=rg.Point(upperleft1.x-width/2,upperleft1.y-height)
        lowerright=lowerright1
        upperleft=upperleft1




# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
