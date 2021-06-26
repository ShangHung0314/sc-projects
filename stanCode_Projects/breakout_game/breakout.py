"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE:
move_step variable is used to control the distance to bounce so that the ball would not stick on the paddle.
speed variable is used to increase the difficulty of the game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 fr
# ames per second
NUM_LIVES = 3  # Number of attempts


def main():
    lives = NUM_LIVES
    graphics = BreakoutGraphics(brick_cols=15, brick_rows=10, paddle_width=120)
    bricks_remove = 0
    move_step = 0
    speed = 0
    score = 0
    graphics.lives_label(lives)
    graphics.score_label(score)
    # Add animation loop here!
    while True:
        # update
        if graphics.start_count > 0:
            move_step += 1
            if speed <= 1000:
                speed += 1
            graphics.ball.move(graphics.get_dx() * (1.0002 ** speed), graphics.get_dy() * (1.0002 ** speed))
        # check
        if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
            graphics._dx = - graphics.get_dx()
        elif graphics.ball.y <= 0:
            graphics._dy = - graphics.get_dy()
        elif graphics.ball.y >= graphics.window.height:
            graphics.window.remove(graphics.ball)
            lives -= 1
            graphics.live_count += 1
            graphics.start_count = 0
            graphics.set_ball()
            move_step = 0
            speed = 0
            graphics.live_label.text = 'lives: ' + str(lives)
            if lives == 0:
                graphics.lose_label()
        # collisions
        obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        obj1 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                             graphics.ball.y + graphics.ball.height)
        obj2 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        obj3 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                             graphics.ball.y)
        bounce = 0
        while bounce == 0:
            # (0,1)
            if obj is not None and obj is not graphics.live_label and obj is not graphics.score_label:
                if move_step > graphics.paddle.height // 2:
                    graphics.bounce()
                    move_step = 0
                    bounce += 1
                    if obj is not graphics.paddle:
                        graphics.window.remove(obj)
                        bricks_remove += 1
                        score += 1
                        graphics.score_label.text = 'score: ' + str(score)
                else:
                    bounce += 1
            # (1,1)
            elif obj1 is not None and obj1 is not graphics.live_label and obj1 is not graphics.score_label:
                if move_step > graphics.paddle.height // 2:
                    graphics.bounce()
                    move_step = 0
                    bounce += 1
                    if obj1 is not graphics.paddle:
                        graphics.window.remove(obj1)
                        bricks_remove += 1
                        score += 1
                        graphics.score_label.text = 'score: ' + str(score)
                else:
                    bounce += 1
            # (0,0)
            elif obj2 is not None and obj2 is not graphics.live_label and obj2 is not graphics.score_label:
                if move_step > graphics.paddle.height // 2:
                    graphics.bounce()
                    move_step = 0
                    bounce += 1
                    if obj2 is not graphics.paddle:
                        graphics.window.remove(obj2)
                        bricks_remove += 1
                        score += 1
                        graphics.score_label.text = 'score: ' + str(score)
                else:
                    bounce += 1
            # (1,0)
            elif obj3 is not None and obj3 is not graphics.live_label and obj3 is not graphics.score_label:
                if move_step > graphics.paddle.height:
                    graphics.bounce()
                    move_step = 0
                    bounce += 1
                    if obj3 is not graphics.paddle:
                        graphics.window.remove(obj3)
                        bricks_remove += 1
                        score += 1
                        graphics.score_label.text = 'score: ' + str(score)
                else:
                    bounce += 1
            else:
                bounce += 1
        if bricks_remove == graphics.total_bricks:
            graphics.win_label()
            break
        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
