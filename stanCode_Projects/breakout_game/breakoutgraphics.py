"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 70  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 6  # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.color = 'blue'
        self.paddle.filled = True
        self.paddle.fill_color = 'blue'
        self.window.add(self.paddle, window_width / 2 - paddle_width / 2, window_height - paddle_offset - paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.color = 'grey'
        self.ball.filled = True
        self.ball.fill_color = 'grey'
        self.window.add(self.ball, window_width / 2 - ball_radius, window_height / 2 - ball_radius)

        # Default initial velocity for the ball
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self._dx = -self._dx

        # Initialize our mouse listeners
        self.start_count = 0
        self.live_count = 0
        onmouseclicked(self.click)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                self.bricks.fill_color = self.color_transform(i)
                self.bricks.color = 'black'
                self.window.add(self.bricks, j * (brick_width + brick_spacing),
                                1 * brick_offset + i * (brick_height + brick_spacing))
        self.total_bricks = brick_cols * brick_rows

    def click(self, mouse):
        self.start_count += 1
        onmouseclicked(self.invalid_click)
        if self.live_count < 2:
            onmouseclicked(self.click)

    def bounce(self):
        self._dx = self.get_dx()
        self._dy = -self.get_dy()

    # Getter
    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    def paddle_move(self, mouse):
        if self.window.width - self.paddle.width / 2 > mouse.x > self.paddle.width / 2:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def set_ball(self):
        self.ball = GOval(self.ball.width, self.ball.height)
        self.ball.color = 'grey'
        self.ball.filled = True
        self.ball.fill_color = 'grey'
        self.window.add(self.ball, self.window.width / 2 - self.ball.width / 2,
                        self.window.height / 2 - self.ball.height / 2)

    @staticmethod
    def color_transform(i):
        s = ''
        if i // 2 == 0:
            s += 'red'
        elif i // 2 == 1:
            s += 'orange'
        elif i // 2 == 2:
            s += 'yellow'
        elif i // 2 == 3:
            s += 'green'
        elif i // 2 == 4:
            s += 'blue'
        return s

    @staticmethod
    def invalid_click(mouse):
        m = ""

    def lose_label(self):
        self.window.clear()
        lose = GLabel('You lose!')
        lose.font = 'Courier-40-bold'
        lose.color = 'black'
        self.window.add(lose, self.window.width / 2 - lose.width / 2, self.window.height / 2 - lose.height / 2)

    def win_label(self):
        self.window.clear()
        win = GLabel('You win!')
        win.font = 'Courier-40-bold'
        win.color = 'black'
        self.window.add(win, self.window.width / 2 - win.width / 2, self.window.height / 2 - win.height / 2)

    # ----------------------------------------------------------------------
    def lives_label(self, lives):
        self.live_label = GLabel('lives: ' + str(lives))
        self.live_label.font = 'Courier-10-bold'
        self.live_label.color = 'black'
        self.window.add(self.live_label, 0, self.window.height - self.live_label.height)

    def score_label(self, score):
        self.score_label = GLabel('score: ' + str(score))
        self.score_label.font = 'Courier-10-bold'
        self.score_label.color = 'black'
        self.window.add(self.score_label, self.window.width - self.score_label.width * 1.5
                        , self.window.height - self.score_label.height)
