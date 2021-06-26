"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 1
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    n = len(YEARS)
    interval = (width - 2 * GRAPH_MARGIN_SIZE) / n
    return year_index * interval + GRAPH_MARGIN_SIZE


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas
    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill='grey')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='grey')
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT, width=LINE_WIDTH, fill='grey')
    canvas.create_line(CANVAS_WIDTH - GRAPH_MARGIN_SIZE, 0, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT, width=LINE_WIDTH, fill='grey')

    for year in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year), 0, get_x_coordinate(CANVAS_WIDTH, year), CANVAS_HEIGHT,
                           width=LINE_WIDTH, fill='grey')
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX,
                           text=YEARS[year], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    #################################
    for names in range(len(lookup_names)):
        for year in range(len(YEARS) - 1):
            # coordinates
            x0 = get_x_coordinate(CANVAS_WIDTH, year)
            if str(YEARS[year]) in name_data[lookup_names[names]]:
                y0 = int(name_data[str(lookup_names[names])][str(YEARS[year])]) * (
                        CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK + GRAPH_MARGIN_SIZE
            else:
                y0 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            x1 = get_x_coordinate(CANVAS_WIDTH, year + 1)
            if str(YEARS[year + 1]) in name_data[lookup_names[names]]:
                y1 = int(name_data[str(lookup_names[names])][str(YEARS[year + 1])]) * (
                        CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK + GRAPH_MARGIN_SIZE
            else:
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            # lines
            canvas.create_line(x0, y0, x1, y1, width=LINE_WIDTH, fill=COLORS[names % 4])
            # name tags
            if str(YEARS[year]) in name_data[lookup_names[names]]:
                rank_text = str(name_data[lookup_names[names]][str(YEARS[year])])
            else:
                rank_text = '*'
            canvas.create_text(x0 + TEXT_DX, y0, text=str(lookup_names[names]) + ' ' + rank_text, anchor=tkinter.SW,
                               fill=COLORS[names % 4])
        # tags on last point
        x_last = get_x_coordinate(CANVAS_WIDTH, len(YEARS) - 1) + TEXT_DX
        if str(YEARS[-1]) in name_data[lookup_names[names]]:
            rank_text = str(name_data[lookup_names[names]][str(YEARS[-1])])
            y_last = int(name_data[str(lookup_names[names])][
                             str(YEARS[len(YEARS) - 1])]) * (
                             CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK + GRAPH_MARGIN_SIZE
        else:
            rank_text = '*'
            y_last = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
        canvas.create_text(x_last, y_last,
                           text=str(lookup_names[names]) + ' ' + rank_text,
                           anchor=tkinter.SW, fill=COLORS[names % 4])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)
    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
