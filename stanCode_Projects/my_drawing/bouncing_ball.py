"""
File: bouncing_ball.py
Name: Cage
-------------------------
TODO:
This program simulates how a ball would bounce.
Use onmouseclicked functions within an onmouseclicked function to achieve multiple clicking purposes.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 20
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 40
START_Y = 40
N = 3
# This is a window
window = GWindow(800, 500, title='bouncing_ball.py')
# Create a ball
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
# Count the click time
click_time = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # put the ball at the start point
    ball.filled = True
    ball.fill_color = 'black'
    ball.color = 'black'
    window.add(ball)
    print(str(N) + ' drops remain.')
    onmouseclicked(drop_the_ball)


def drop_the_ball(m):
    global VX, ball, click_time
    # everytime after a click, click plus 1
    click_time += 1

    # ball drop
    vertical_speed = VX
    # before a while loop end, no matter how many times you click, it won't affect the bouncing
    onmouseclicked(invalid_clicks)
    # use count variable to decide whether the ball is falling or bouncing back.
    count = 0
    while ball.x <= window.width:
        ball.move(VX, vertical_speed)
        if ball.y + ball.height < window.height:
            # count = 0 -> drop ; count = 1 -> rise
            if count == 0:
                vertical_speed = vertical_speed + GRAVITY
            else:
                # if vertical speed is higher than the gravity, it will keep rising and maintain count equals 1.
                if vertical_speed >= GRAVITY:
                    vertical_speed = vertical_speed * REDUCE
                # if vertical speed is lower than the gravity, it should start to fall so the count will be 0.
                else:
                    count = 0
        elif ball.y + ball.height >= window.height:
            count += 1
            vertical_speed = -vertical_speed * REDUCE
        pause(DELAY)

    # the ball will present again until click time = 3
    if click_time < 3:
        ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
        ball.filled = True
        ball.fill_color = 'black'
        ball.color = 'black'
        window.add(ball)
        # use this function so that you can drop the ball again
        onmouseclicked(drop_the_ball)
        print(str(N - click_time) + ' drops remain.')
    else:
        print('No drop remain.')


# it's a function to create the invalid clicks
# just type something under so that the program won't be an error or present annoying warnings
def invalid_clicks(m):
    print('Stop! It is an invalid click!')


if __name__ == "__main__":
    main()
