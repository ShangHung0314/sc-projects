import tkinter
import marketcap_ext
import marketcapgraphicsgui_ext as gui

CANVAS_WIDTH = 1400
CANVAS_HEIGHT = 600
YEARS = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
         2019, 2020, 2021]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 1
MAX_CAP = 2350


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


def draw_caps(canvas, ticker_data, lookup_names):
    """
    Given a dict of market cap data and a list of tickers, plots
    the historical trend of those companies onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        ticker_data (dict): Dictionary holding market cap data
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
            if str(YEARS[year]) in ticker_data[lookup_names[names]]:
                y0 = CANVAS_HEIGHT - (int(ticker_data[str(lookup_names[names])][str(YEARS[year])])) * (
                        CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_CAP - GRAPH_MARGIN_SIZE
            else:
                y0 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            x1 = get_x_coordinate(CANVAS_WIDTH, year + 1)
            if str(YEARS[year + 1]) in ticker_data[lookup_names[names]]:
                y1 = CANVAS_HEIGHT - (int(ticker_data[str(lookup_names[names])][str(YEARS[year + 1])])) * (
                        CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_CAP - GRAPH_MARGIN_SIZE
            else:
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            # lines
            canvas.create_line(x0, y0, x1, y1, width=LINE_WIDTH, fill=COLORS[names % 4])
            # name tags
            if str(YEARS[year]) in ticker_data[lookup_names[names]]:
                rank_text = str(ticker_data[lookup_names[names]][str(YEARS[year])])
            else:
                rank_text = '*'
            canvas.create_text(x0 + TEXT_DX, y0, text=rank_text, anchor=tkinter.SW,
                               fill=COLORS[names % 4], font='times 8')
        # tags on last point
        x_last = get_x_coordinate(CANVAS_WIDTH, len(YEARS) - 1) + TEXT_DX
        if str(YEARS[-1]) in ticker_data[lookup_names[names]]:
            rank_text = str(ticker_data[lookup_names[names]][str(YEARS[-1])])
            y_last = CANVAS_HEIGHT - (int(ticker_data[str(lookup_names[names])][
                                              str(YEARS[len(YEARS) - 1])])) * (
                             CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_CAP - GRAPH_MARGIN_SIZE
        else:
            rank_text = '*'
            y_last = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
        canvas.create_text(x_last - 8 * TEXT_DX, y_last,
                           text=str(lookup_names[names]),
                           anchor=tkinter.SW, fill=COLORS[names % 4], font='times 8')
        canvas.create_text(x_last - 8 * TEXT_DX, y_last + 8 * TEXT_DX,
                           text=rank_text,
                           anchor=tkinter.SW, fill=COLORS[names % 4], font='times 8')


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    cap_data, ticker_data = marketcap_ext.get_cap()
    # Create the window and the canvas
    top = tkinter.Tk()

    top.wm_title('Market Cap')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, cap_data, draw_caps, marketcap_ext.search_names,
                          ticker_data)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
