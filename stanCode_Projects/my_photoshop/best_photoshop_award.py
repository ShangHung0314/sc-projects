"""
File: best_photoshop_award.py
Name: Cage
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.25
BLACK_PIXEL = 120


def combine(background_img, figure_img):
    """
    :param background_img: (SimpleImage) the original image that will replace the green screen
    :param figure_img: (SimpleImage) the original image with green screen
    :return: the updated image with green screen replaced as the background space ship
    """
    background_img.make_as_big_as(figure_img)
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            figure_p = figure_img.get_pixel(x, y)
            avg = (figure_p.red + figure_p.green + figure_p.blue) // 3
            total = figure_p.red + figure_p.green + figure_p.blue
            if figure_p.green > avg * THRESHOLD and total > BLACK_PIXEL:
                bg_p = background_img.get_pixel(x, y)
                figure_p.red = bg_p.red
                figure_p.green = bg_p.green
                figure_p.blue = bg_p.blue
    return figure_img


def main():
    """
    TODO:
    Because of the pandemic, we can not travel.
    I photoshop myself to the Amsterdam!
    """
    me = SimpleImage("image_contest/me.jpg")
    background = SimpleImage("image_contest/amsterdam.jpg")
    result = combine(background, me)
    result.show()


if __name__ == '__main__':
    main()
