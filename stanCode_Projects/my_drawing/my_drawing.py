"""
File: my_drawing
Name: Cage
----------------------
TODO:
Recently, Elon Musk claimed himself the Imperator of Mars.
So, this drawing depicts the look of Elon standing on the surface of Mars.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GArc, GPolygon, GRoundRect, G3DRect
from campy.graphics.gwindow import GWindow
import random

window = GWindow(width=1000, height=650)


def main():
    """
    TODO:
    This drawing is comprised of 4 parts: background, face, and label.
    The background includes sky, sand, small rocks and a giant rock.
    I use for loops to achieve the effect of multiple layers of sky and sand.
    And the small rocks would be randomly drew on the surface.
    So it may take a minute to complete the drawing.
    """
    # ============background===============
    # ************sky************
    sky_back = GRect(1000, 650)
    sky_back.filled = True
    sky_back.fill_color = 'azure'
    window.add(sky_back)
    for i in range(70):
        sky_shade_light = GOval(900 - i * 10, 20)
        sky_shade_light.filled = True
        sky_shade_light.fill_color = 'paleturquoise'
        sky_shade_light.color = 'paleturquoise'
        window.add(sky_shade_light, -10, -10 + i * 5)
    for i in range(50):
        sky_shade_light = GOval(800 - i * 10, 20)
        sky_shade_light.filled = True
        sky_shade_light.fill_color = 'lightskyblue'
        sky_shade_light.color = 'lightskyblue'
        window.add(sky_shade_light, -10, -10 + i * 4)
    for i in range(25):
        sky_shade = GOval(600 - i * 20, 20)
        sky_shade.filled = True
        sky_shade.fill_color = 'cadetblue'
        sky_shade.color = 'cadetblue'
        window.add(sky_shade, -50, -5 + i * 5)

    # ************sand************
    ground = GRoundRect(1000, 700)
    ground.filled = True
    ground.fill_color = 'sandybrown'
    ground.color = 'sandybrown'
    window.add(ground, 0, 325)
    # from far to close texture
    for i in range(65):
        for j in range(200):
            sand = GOval(1+i*0.05,1+i*0.05)
            sand.filled=True
            sand.fill_color='sandybrown'
            sand.color='brown'
            window.add(sand,j*5,325+i*5)
    # ************rock************
    # first small rock
    rock = GPolygon()
    rock.add_vertex((100, 335))
    rock.add_vertex((110, 315))
    rock.add_vertex((140, 315))
    rock.add_vertex((150, 335))
    rock.filled = True
    rock.fill_color = 'grey'
    rock.color = 'grey'
    window.add(rock)
    round_shape = GArc(30, 30, 0, 180, x=110, y=310)
    round_shape.color = 'grey'
    round_shape.filled = True
    round_shape.fill_color = 'grey'
    window.add(round_shape)
    for k in range(3):
        rock_shade = GOval(35 - 5 * k, 3)
        rock_shade.filled = True
        rock_shade.fill_color = 'darkgrey'
        rock_shade.color = 'darkgrey'
        window.add(rock_shade, 114 + 2.5 * k, 332 - 2 * k)
    # a lot of random small rocks
    for i in range(5):
        for j in range(5):
            r = random.randrange(80, 380, 20)
            r2 = random.randrange(0, 3, 1)
            rock = GPolygon()
            rock.add_vertex((100 + (j + r2 + 1) * r, 335 + (i + r2) * r))
            rock.add_vertex((110 + (j + r2 + 1) * r, 315 + (i + r2) * r))
            rock.add_vertex((140 + (j + r2 + 1) * r, 315 + (i + r2) * r))
            rock.add_vertex((150 + (j + r2 + 1) * r, 335 + (i + r2) * r))
            rock.filled = True
            rock.fill_color = 'grey'
            rock.color = 'grey'
            window.add(rock)
            round_shape = GArc(30, 30, 0, 180, x=110 + (j + r2 + 1) * r, y=310 + (i + r2) * r)
            round_shape.color = 'grey'
            round_shape.filled = True
            round_shape.fill_color = 'grey'
            window.add(round_shape)
            for k in range(3):
                rock_shade = GOval(35 - 5 * k, 3)
                rock_shade.filled = True
                rock_shade.fill_color = 'darkgrey'
                rock_shade.color = 'darkgrey'
                window.add(rock_shade, 114 + 2.5 * k + (j + r2 + 1) * r, 332 - 2 * k + (i + r2) * r)
    # the giant rock
    bigrock = GPolygon()
    bigrock.add_vertex((700, 400))
    bigrock.add_vertex((730, 370))
    bigrock.add_vertex((740, 350))
    bigrock.add_vertex((760, 330))
    bigrock.add_vertex((780, 330))
    bigrock.add_vertex((790, 335))
    bigrock.add_vertex((795, 350))
    bigrock.add_vertex((810, 360))
    bigrock.add_vertex((820, 350))
    bigrock.add_vertex((840, 340))
    bigrock.add_vertex((850, 330))
    bigrock.add_vertex((860, 330))
    bigrock.add_vertex((870, 340))
    bigrock.add_vertex((880, 340))
    bigrock.add_vertex((890, 335))
    bigrock.add_vertex((895, 335))
    bigrock.add_vertex((910, 330))
    bigrock.add_vertex((930, 332))
    bigrock.add_vertex((930, 400))
    bigrock.filled = True
    bigrock.fill_color = 'dimgrey'
    bigrock.color = 'dimgrey'
    window.add(bigrock)
    bgshape = GArc(120, 70, 180, -160)
    bgshape.filled = True
    bgshape.fill_color = 'dimgrey'
    bgshape.color = 'dimgrey'
    window.add(bgshape, 670, 382)
    bgshape = GArc(80, 70, 90, -180)
    bgshape.filled = True
    bgshape.fill_color = 'dimgrey'
    bgshape.color = 'dimgrey'
    window.add(bgshape, 903, 330)

    # ============Face===============
    left_ear = GPolygon()
    left_ear.add_vertex((435, 420))
    left_ear.add_vertex((430, 430))
    left_ear.add_vertex((425, 432))
    left_ear.add_vertex((422, 430))
    left_ear.add_vertex((420, 430))
    left_ear.add_vertex((418, 420))
    left_ear.add_vertex((415, 410))
    left_ear.add_vertex((415, 405))
    left_ear.add_vertex((415, 395))
    left_ear.add_vertex((415, 390))
    left_ear.add_vertex((417, 380))
    left_ear.add_vertex((423, 378))
    left_ear.add_vertex((425, 378))
    left_ear.add_vertex((430, 382))
    left_ear.add_vertex((435, 395))
    left_ear.filled = True
    left_ear.fill_color = 'cornsilk'
    left_ear.color = 'grey'
    window.add(left_ear)

    earhole = GOval(6, 20)
    earhole.filled = True
    earhole.fill_color = 'coral'
    earhole.color = 'coral'
    window.add(earhole, 421, 393)
    earhole = GPolygon()
    earhole.add_vertex((417, 392))
    earhole.add_vertex((419, 384))
    earhole.add_vertex((421, 384))
    earhole.add_vertex((424, 389))
    earhole.add_vertex((420, 388))
    earhole.filled = True
    earhole.fill_color = 'black'
    earhole.color = 'black'
    window.add(earhole)

    right_ear = GPolygon()
    right_ear.add_vertex((603, 436))
    right_ear.add_vertex((605, 438))
    right_ear.add_vertex((608, 437))
    right_ear.add_vertex((612, 435))
    right_ear.add_vertex((615, 420))
    right_ear.add_vertex((616, 405))
    right_ear.add_vertex((613, 398))
    right_ear.add_vertex((612, 395))
    right_ear.add_vertex((608, 395))
    right_ear.filled = True
    right_ear.fill_color = 'cornsilk'
    right_ear.color = 'grey'
    window.add(right_ear)

    outline = GPolygon()
    outline.add_vertex((442, 490))
    outline.add_vertex((427, 400))
    outline.add_vertex((445, 280))
    outline.add_vertex((500, 280))
    outline.add_vertex((550, 280))
    outline.add_vertex((590, 280))
    outline.add_vertex((610, 290))
    outline.add_vertex((610, 400))
    outline.add_vertex((600, 445))
    outline.add_vertex((585, 490))
    outline.add_vertex((530, 520))
    outline.filled = True
    outline.fill_color = 'cornsilk'
    outline.color = 'grey'
    window.add(outline)

    leftside_hair = GPolygon()
    leftside_hair.add_vertex((423, 378))
    leftside_hair.add_vertex((423, 335))
    leftside_hair.add_vertex((430, 298))
    leftside_hair.add_vertex((453, 298))
    leftside_hair.add_vertex((443, 315))
    leftside_hair.add_vertex((448, 330))
    leftside_hair.add_vertex((437, 345))
    leftside_hair.add_vertex((433, 415))
    leftside_hair.add_vertex((429, 415))
    leftside_hair.filled = True
    leftside_hair.fill_color = 'mediumseagreen'
    leftside_hair.color = 'mediumseagreen'
    window.add(leftside_hair)

    leftside_hair = GPolygon()
    leftside_hair.add_vertex((437, 345))
    leftside_hair.add_vertex((437, 337))
    leftside_hair.add_vertex((446, 326))
    leftside_hair.add_vertex((448, 330))
    leftside_hair.filled = True
    leftside_hair.fill_color = 'yellowgreen'
    leftside_hair.color = 'yellowgreen'
    window.add(leftside_hair)

    leftside_hair = GPolygon()
    leftside_hair.add_vertex((437, 330))
    leftside_hair.add_vertex((437, 324))
    leftside_hair.add_vertex((444, 317))
    leftside_hair.add_vertex((446, 321))
    leftside_hair.filled = True
    leftside_hair.fill_color = 'yellowgreen'
    leftside_hair.color = 'yellowgreen'
    window.add(leftside_hair)

    leftside_hair = GPolygon()
    leftside_hair.add_vertex((430, 298))
    leftside_hair.add_vertex((437, 278))
    leftside_hair.add_vertex((448, 261))
    leftside_hair.add_vertex((452, 258))
    leftside_hair.add_vertex((452, 254))
    leftside_hair.add_vertex((460, 244))
    leftside_hair.add_vertex((460, 298))
    leftside_hair.filled = True
    leftside_hair.fill_color = 'coral'
    leftside_hair.color = 'coral'
    window.add(leftside_hair)

    leftside_hair = GPolygon()
    leftside_hair.add_vertex((460, 244))
    leftside_hair.add_vertex((490, 234))
    leftside_hair.add_vertex((490, 254))
    leftside_hair.add_vertex((460, 254))
    leftside_hair.filled = True
    leftside_hair.fill_color = 'green'
    leftside_hair.color = 'green'
    window.add(leftside_hair)

    leftside_hair = GPolygon()
    leftside_hair.add_vertex((460, 244))
    leftside_hair.add_vertex((464, 242))
    leftside_hair.add_vertex((464, 254))
    leftside_hair.add_vertex((460, 254))
    leftside_hair.filled = True
    leftside_hair.fill_color = 'black'
    leftside_hair.color = 'black'
    window.add(leftside_hair)

    leftside_hair = GPolygon()
    leftside_hair.add_vertex((467, 244))
    leftside_hair.add_vertex((470, 242))
    leftside_hair.add_vertex((470, 254))
    leftside_hair.add_vertex((467, 254))
    leftside_hair.filled = True
    leftside_hair.fill_color = 'black'
    leftside_hair.color = 'black'
    window.add(leftside_hair)

    leftside_hair = GPolygon()
    leftside_hair.add_vertex((490, 254))
    leftside_hair.add_vertex((490, 234))
    leftside_hair.add_vertex((510, 237))
    leftside_hair.add_vertex((540, 237))
    leftside_hair.add_vertex((545, 234))
    leftside_hair.add_vertex((550, 237))
    leftside_hair.add_vertex((570, 237))
    leftside_hair.add_vertex((573, 240))
    leftside_hair.filled = True
    leftside_hair.fill_color = 'black'
    leftside_hair.color = 'black'
    window.add(leftside_hair)

    main_hair = GPolygon()
    main_hair.add_vertex((450, 310))
    main_hair.add_vertex((438, 300))
    main_hair.add_vertex((446, 273))
    main_hair.add_vertex((455, 259))
    main_hair.add_vertex((470, 249))
    main_hair.add_vertex((490, 240))
    main_hair.add_vertex((585, 240))
    main_hair.add_vertex((595, 250))
    main_hair.add_vertex((593, 260))
    main_hair.add_vertex((602, 270))
    main_hair.add_vertex((610, 290))
    main_hair.add_vertex((618, 310))
    main_hair.add_vertex((620, 395))
    main_hair.add_vertex((610, 400))
    main_hair.add_vertex((605, 410))
    main_hair.add_vertex((608, 395))
    main_hair.add_vertex((608, 375))
    main_hair.add_vertex((602, 345))
    main_hair.add_vertex((602, 320))
    main_hair.add_vertex((580, 290))
    main_hair.add_vertex((560, 285))
    main_hair.add_vertex((540, 280))
    main_hair.add_vertex((485, 280))
    main_hair.add_vertex((460, 295))
    main_hair.filled = True
    main_hair.fill_color = 'black'
    main_hair.color = 'black'
    window.add(main_hair)

    hair = GPolygon()
    hair.add_vertex((530, 258))
    hair.add_vertex((533, 250))
    hair.add_vertex((536, 258))
    hair.add_vertex((533, 254))
    hair.filled = True
    hair.fill_color = 'purple'
    hair.color = 'purple'
    window.add(hair)

    hair = GPolygon()
    hair.add_vertex((585, 258))
    hair.add_vertex((588, 250))
    hair.add_vertex((589, 256))
    hair.add_vertex((591, 252))
    hair.add_vertex((593, 258))
    hair.add_vertex((588, 258))
    hair.add_vertex((594, 264))
    hair.filled = True
    hair.fill_color = 'mediumseagreen'
    hair.color = 'mediumseagreen'
    window.add(hair)

    between_eyebrow = GPolygon()
    between_eyebrow.add_vertex((500, 357))
    between_eyebrow.add_vertex((480, 352))
    between_eyebrow.add_vertex((520, 352))
    between_eyebrow.add_vertex((527, 360))
    between_eyebrow.add_vertex((558, 360))
    between_eyebrow.add_vertex((545, 368))
    between_eyebrow.add_vertex((509, 367))
    between_eyebrow.filled = True
    between_eyebrow.fill_color = 'lightpink'
    between_eyebrow.color = 'lightpink'
    window.add(between_eyebrow)

    left_eyebrow = GPolygon()
    left_eyebrow.add_vertex((456, 368))
    left_eyebrow.add_vertex((459, 363))
    left_eyebrow.add_vertex((469, 356))
    left_eyebrow.add_vertex((473, 353))
    left_eyebrow.add_vertex((484, 353))
    left_eyebrow.add_vertex((498, 355))
    left_eyebrow.add_vertex((500, 357))
    left_eyebrow.add_vertex((509, 367))
    left_eyebrow.add_vertex((509, 370))
    left_eyebrow.add_vertex((498, 361))
    left_eyebrow.add_vertex((496, 360))
    left_eyebrow.add_vertex((493, 360))
    left_eyebrow.add_vertex((480, 358))
    left_eyebrow.filled = True
    left_eyebrow.fill_color = 'black'
    left_eyebrow.color = 'black'
    window.add(left_eyebrow)

    right_eyebrow = GPolygon()
    right_eyebrow.add_vertex((539, 368))
    right_eyebrow.add_vertex((552, 358))
    right_eyebrow.add_vertex((564, 358))
    right_eyebrow.add_vertex((574, 363))
    right_eyebrow.add_vertex((584, 370))
    right_eyebrow.add_vertex((579, 373))
    right_eyebrow.add_vertex((574, 368))
    right_eyebrow.add_vertex((564, 363))
    right_eyebrow.add_vertex((552, 363))
    right_eyebrow.filled = True
    right_eyebrow.fill_color = 'black'
    right_eyebrow.color = 'black'
    window.add(right_eyebrow)

    left_eye = GPolygon()
    left_eye.add_vertex((462, 387))
    left_eye.add_vertex((476, 375))
    left_eye.add_vertex((483, 375))
    left_eye.add_vertex((480, 378))
    left_eye.filled = True
    left_eye.fill_color = 'black'
    left_eye.color = 'black'
    window.add(left_eye)
    left_eye = GOval(23, 4)
    left_eye.filled = True
    left_eye.fill_color = 'orange'
    left_eye.color = 'orange'
    window.add(left_eye, 473, 382)
    left_eye = GPolygon()
    left_eye.add_vertex((488, 377))
    left_eye.add_vertex((493, 377))
    left_eye.add_vertex((505, 385))
    left_eye.add_vertex((508, 391))
    left_eye.add_vertex((502, 391))
    left_eye.add_vertex((499, 385))
    left_eye.filled = True
    left_eye.fill_color = 'skyblue'
    left_eye.color = 'skyblue'
    window.add(left_eye)
    left_eye = GPolygon()
    left_eye.add_vertex((488, 377))
    left_eye.add_vertex((499, 385))
    left_eye.add_vertex((494, 385))
    left_eye.filled = True
    left_eye.fill_color = 'purple'
    left_eye.color = 'purple'
    window.add(left_eye)
    left_eye = GOval(18, 2)
    left_eye.filled = True
    left_eye.fill_color = 'lightgreen'
    left_eye.color = 'lightgreen'
    window.add(left_eye, 482, 389)
    left_eye = GPolygon()
    left_eye.add_vertex((482, 391))
    left_eye.add_vertex((472, 391))
    left_eye.add_vertex((465, 388))
    left_eye.add_vertex((467, 390))
    left_eye.add_vertex((464, 387))
    left_eye.add_vertex((465, 386))
    left_eye.add_vertex((482, 390))
    left_eye.filled = True
    left_eye.fill_color = 'violet'
    left_eye.color = 'violet'
    window.add(left_eye)

    left_pupil = GOval(11, 10)
    left_pupil.filled = True
    left_pupil.fill_color = 'black'
    left_pupil.color = 'black'
    window.add(left_pupil, 478, 375)
    left_pupil = GOval(3, 3)
    left_pupil.filled = True
    left_pupil.fill_color = 'grey'
    left_pupil.color = 'black'
    window.add(left_pupil, 480, 377)

    right_eye = GOval(25, 4)
    right_eye.filled = True
    right_eye.fill_color = 'violet'
    right_eye.color = 'violet'
    window.add(right_eye, 548, 387)
    right_eye = GOval(22, 2)
    right_eye.filled = True
    right_eye.fill_color = 'lightpink'
    right_eye.color = 'lightpink'
    window.add(right_eye, 551, 385)

    right_pupil = GOval(10, 9)
    right_pupil.filled = True
    right_pupil.fill_color = 'black'
    right_pupil.color = 'black'
    window.add(right_pupil, 553, 377)
    right_pupil = GOval(1, 1)
    right_pupil.filled = True
    right_pupil.fill_color = 'grey'
    right_pupil.color = 'black'
    window.add(right_pupil, 555, 380)

    right_eye = GPolygon()
    right_eye.add_vertex((545, 385))
    right_eye.add_vertex((555, 377))
    right_eye.add_vertex((549, 385))
    right_eye.filled = True
    right_eye.fill_color = 'indigo'
    right_eye.color = 'indigo'
    window.add(right_eye)
    right_eye = GPolygon()
    right_eye.add_vertex((558, 377))
    right_eye.add_vertex((566, 378))
    right_eye.add_vertex((575, 385))
    right_eye.filled = True
    right_eye.fill_color = 'black'
    right_eye.color = 'black'
    window.add(right_eye)

    nose = GPolygon()
    nose.add_vertex((513, 369))
    nose.add_vertex((523, 408))
    nose.add_vertex((521, 417))
    nose.add_vertex((509, 432))
    nose.add_vertex((495, 432))
    nose.filled = True
    nose.fill_color = 'greenyellow'
    nose.color = 'greenyellow'
    window.add(nose)
    nose = GOval(21, 14)
    nose.filled = True
    nose.fill_color = 'teal'
    nose.color = 'teal'
    window.add(nose, 505, 420)
    nose = GPolygon()
    nose.add_vertex((523, 408))
    nose.add_vertex((521, 417))
    nose.add_vertex((509, 432))
    nose.add_vertex((507, 432))
    nose.add_vertex((520, 390))
    nose.filled = True
    nose.fill_color = 'teal'
    nose.color = 'teal'
    window.add(nose)
    nose = GOval(21, 13)
    nose.filled = True
    nose.fill_color = 'lightskyblue'
    nose.color = 'lightskyblue'
    window.add(nose, 523, 422)
    nose = GPolygon()
    nose.add_vertex((509, 432))
    nose.add_vertex((512, 426))
    nose.add_vertex((521, 417))
    nose.add_vertex((532, 423))
    nose.add_vertex((537, 423))
    nose.add_vertex((540, 432))
    nose.filled = True
    nose.fill_color = 'purple'
    nose.color = 'purple'
    window.add(nose)
    nose = GPolygon()
    nose.add_vertex((521, 417))
    nose.add_vertex((523, 408))
    nose.add_vertex((513, 369))
    nose.add_vertex((542, 369))
    nose.add_vertex((535, 380))
    nose.add_vertex((535, 423))
    nose.add_vertex((528, 423))
    nose.filled = True
    nose.fill_color = 'ivory'
    nose.color = 'ivory'
    window.add(nose)
    nose = GPolygon()
    nose.add_vertex((537, 380))
    nose.add_vertex((537, 423))
    nose.add_vertex((535, 423))
    nose.add_vertex((535, 382))
    nose.filled = True
    nose.fill_color = 'lightskyblue'
    nose.color = 'lightskyblue'
    window.add(nose)

    nostril = GPolygon()
    nostril.add_vertex((513, 430))
    nostril.add_vertex((516, 426))
    nostril.add_vertex((519, 426))
    nostril.add_vertex((522, 430))
    nostril.filled = True
    nostril.fill_color = 'black'
    nostril.color = 'black'
    window.add(nostril)
    nostril = GPolygon()
    nostril.add_vertex((528, 429))
    nostril.add_vertex((534, 425))
    nostril.add_vertex((536, 430))
    nostril.filled = True
    nostril.fill_color = 'black'
    nostril.color = 'black'
    window.add(nostril)

    low_lip = GArc(56, 42, -0, -180)
    low_lip.filled = True
    low_lip.fill_color = 'crimson'
    low_lip.color = 'crimson'
    window.add(low_lip, 496, 453)

    low_lip = GOval(35, 6)
    low_lip.filled = True
    low_lip.fill_color = 'orangered'
    low_lip.color = 'orangered'
    window.add(low_lip, 513, 464)

    low_lip = GOval(10, 2)
    low_lip.filled = True
    low_lip.fill_color = 'coral'
    low_lip.color = 'coral'
    window.add(low_lip, 524, 467)

    mouth = GOval(25, 2)
    mouth.filled = True
    mouth.fill_color = 'lightskyblue'
    mouth.color = 'lightskyblue'
    window.add(mouth, 515, 463)

    up_lip = GPolygon()
    up_lip.add_vertex((492, 463))
    up_lip.add_vertex((512, 455))
    up_lip.add_vertex((515, 454))
    up_lip.add_vertex((522, 454))
    up_lip.add_vertex((523, 455))
    up_lip.add_vertex((527, 460))
    up_lip.add_vertex((523, 460))
    up_lip.filled = True
    up_lip.fill_color = 'purple'
    up_lip.color = 'purple'
    window.add(up_lip)
    up_lip = GPolygon()
    up_lip.add_vertex((522, 460))
    up_lip.add_vertex((526, 455))
    up_lip.add_vertex((529, 454))
    up_lip.add_vertex((535, 454))
    up_lip.add_vertex((537, 455))
    up_lip.add_vertex((557, 465))
    up_lip.add_vertex((526, 460))
    up_lip.filled = True
    up_lip.fill_color = 'purple'
    up_lip.color = 'purple'
    window.add(up_lip)
    up_lip = GPolygon()
    up_lip.add_vertex((496, 462))
    up_lip.add_vertex((515, 457))
    up_lip.add_vertex((522, 457))
    up_lip.add_vertex((523, 458))
    up_lip.add_vertex((525, 459))
    up_lip.add_vertex((527, 458))
    up_lip.add_vertex((528, 457))
    up_lip.add_vertex((534, 457))
    up_lip.add_vertex((553, 462))
    up_lip.filled = True
    up_lip.fill_color = 'black'
    up_lip.color = 'black'
    window.add(up_lip)

    low_lip = GPolygon()
    low_lip.add_vertex((500, 468))
    low_lip.add_vertex((505, 468))
    low_lip.add_vertex((513, 472))
    low_lip.add_vertex((525, 472))
    low_lip.add_vertex((527, 474))
    low_lip.add_vertex((510, 474))
    low_lip.filled = True
    low_lip.fill_color = 'darkgrey'
    low_lip.color = 'darkgrey'
    window.add(low_lip)

    neck = GPolygon()
    neck.add_vertex((438, 490))
    neck.add_vertex((435, 510))
    neck.add_vertex((430, 510))
    neck.add_vertex((495, 650))
    neck.add_vertex((610, 650))
    neck.add_vertex((555, 576))
    neck.add_vertex((568, 516))
    neck.add_vertex((530, 514))
    neck.filled = True
    neck.fill_color = 'cornsilk'
    neck.color = 'grey'
    window.add(neck)

    neck = GPolygon()
    neck.add_vertex((568, 516))
    neck.add_vertex((488, 560))
    neck.add_vertex((459, 576))
    neck.add_vertex((539, 576))
    neck.add_vertex((550, 536))
    neck.add_vertex((564, 536))
    neck.filled = True
    neck.fill_color = 'lightpink'
    neck.color = 'lightpink'
    window.add(neck)

    collar = GPolygon()
    collar.add_vertex((430, 510))
    collar.add_vertex((442, 510))
    collar.add_vertex((488, 560))
    collar.add_vertex((474, 604))
    collar.filled = True
    collar.fill_color = 'yellow'
    collar.color = 'yellow'
    window.add(collar)

    collar = GPolygon()
    collar.add_vertex((481, 582))
    collar.add_vertex((474, 604))
    collar.add_vertex((450, 554))
    collar.filled = True
    collar.fill_color = 'coral'
    collar.color = 'coral'
    window.add(collar)

    collar = GPolygon()
    collar.add_vertex((474, 604))
    collar.add_vertex((525, 650))
    collar.add_vertex((540, 650))
    collar.add_vertex((510, 625))
    collar.add_vertex((500, 605))
    collar.add_vertex((491, 560))
    collar.add_vertex((488, 560))
    collar.filled = True
    collar.fill_color = 'indigo'
    collar.color = 'indigo'
    window.add(collar)

    suit = GPolygon()
    suit.add_vertex((430, 510))
    suit.add_vertex((425, 510))
    suit.add_vertex((370, 550))
    suit.add_vertex((340, 580))
    suit.add_vertex((300, 650))
    suit.add_vertex((495, 650))
    suit.filled = True
    suit.fill_color = 'purple'
    suit.color = 'purple'
    window.add(suit)

    suit = GPolygon()
    suit.add_vertex((564, 536))
    suit.add_vertex((610, 565))
    suit.add_vertex((640, 595))
    suit.add_vertex((675, 625))
    suit.add_vertex((700, 650))
    suit.add_vertex((610, 650))
    suit.add_vertex((555, 576))
    suit.filled = True
    suit.fill_color = 'purple'
    suit.color = 'purple'
    window.add(suit)

    jaw = GPolygon()
    jaw.add_vertex((438, 490))
    jaw.add_vertex((458, 490))
    jaw.add_vertex((458, 497))
    jaw.add_vertex((548, 528))
    jaw.add_vertex((488, 560))
    jaw.add_vertex((442, 510))
    jaw.add_vertex((442, 495))
    jaw.filled = True
    jaw.fill_color = 'mediumpurple'
    jaw.color = 'mediumpurple'
    window.add(jaw)

    jaw = GPolygon()
    jaw.add_vertex((458, 497))
    jaw.add_vertex((530, 514))
    jaw.add_vertex((556, 505))
    jaw.add_vertex((568, 516))
    jaw.add_vertex((510, 545))
    jaw.add_vertex((490, 545))
    jaw.add_vertex((448, 497))
    jaw.filled = True
    jaw.fill_color = 'black'
    jaw.color = 'black'
    window.add(jaw)

    jaw = GPolygon()
    jaw.add_vertex((568, 516))
    jaw.add_vertex((590, 505))

    jaw.add_vertex((603, 436))
    jaw.add_vertex((585, 490))
    jaw.add_vertex((556, 505))
    jaw.filled = True
    jaw.fill_color = 'orange'
    jaw.color = 'orange'
    window.add(jaw)

    # ============Label===============
    label = GLabel('King of Mars', 700, 120)
    label.font = 'Courier-24-bold'
    label.color = 'orange'
    window.add(label)
    label = GLabel('Elon Musk', 700, 90)
    label.font = 'Courier-24-bold'
    label.color = 'orange'
    window.add(label)


if __name__ == '__main__':
    main()
