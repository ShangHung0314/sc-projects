"""
File: draw_line.py
Name: Cage
-------------------------
TODO:
Use GLine and GOval functions to create circles, draw lines, remove circles, and draw the next lines.
Global variables can help store the info processed in point function.
"""

from campy.graphics.gobjects import GOval, GLine, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

# This is a window
window = GWindow()

# to store and count info of two circles
count = 0
x0 = 0
y0 = 0
x1 = 0
y1 = 0
circle1 = GOval(SIZE, SIZE)
circle2 = GOval(SIZE, SIZE)
n = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(point)


def point(m):
    global count, x0, y0, x1, y1, circle1, circle2, n
    # every click, count increase by 1
    count += 1
    n += 1
    # store the first coordinate
    if count == 1:
        window.add(circle1, m.x - SIZE / 2, m.y - SIZE / 2)
        x0 = m.x
        y0 = m.y
    # store the second coordinate and use the info stored in global to make lines and remove circles
    elif count == 2:
        window.add(circle2, m.x - SIZE / 2, m.y - SIZE / 2)
        x1 = m.x
        y1 = m.y
        line = GLine(x0, y0, x1, y1)
        window.add(line)
        window.remove(circle1)
        window.remove(circle2)
        # recount for drawing the next line
        count = 0

        # get info of lines and coordinates
        c1_label = GLabel('(' + str(x0) + ', ' + str(window.height - y0) + ')', x0, y0)
        c1_label.font = '-8'
        window.add(c1_label)
        c2_label = GLabel('(' + str(x1) + ', ' + str(window.height - y1) + ')', x1, y1)
        c2_label.font = '-8'
        window.add(c2_label)
        line_label = GLabel('L' + str(n // 2), x1, y1 - 10)
        window.add(line_label)
        y0 = window.height - y0
        y1 = window.height - y1
        b = round((y1 - y0) / (x1 - x0), 2)
        a = round(-b * x0 + y0, 2)
        print('Line: ' + str(n // 2))
        print('====================================================')
        print('(x0, y0) = ' + '(' + str(x0) + ', ' + str(y0) + ')')
        print('(x1, y1) = ' + '(' + str(x1) + ', ' + str(y1) + ')')
        print('f(x) = ' + str(a) + ' + ' + str(b) + 'x')
        print('====================================================')


if __name__ == "__main__":
    main()
