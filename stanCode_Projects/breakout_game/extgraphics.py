from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from breakoutgraphics import BreakoutGraphics

NUM_LIVES = 3


class Extgraphics:

    def __init__(self):
        live_label = GLabel('lives: ' + str(NUM_LIVES))
        live_label.font = 'Courier-10-bold'
        live_label.color = 'black'

    def lives_label(self, lives, text):
        if text == '':
            live_label = GLabel('lives: ' + str(lives))
            live_label.font = 'Courier-10-bold'
            live_label.color = 'black'
            g.window.add(live_label, 0, self.window.height - live_label.height)