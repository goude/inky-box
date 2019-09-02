'''Render an overlay on a background image, and display on the
inky pHAT.
'''

import os
import datetime
import sys
from PIL import Image, ImageFont, ImageDraw

import inkyphat

WHITE = 0
BLACK = 1
RED = 2


def show_image(filepath):
    img = Image.open(filepath)

    fnt = ImageFont.truetype('./fonts/SFPixelate.ttf', 9)
    d = ImageDraw.Draw(img)
    msg = [
        'Hello, World!',
        datetime.datetime.now().isoformat(),
    ]
    d.multiline_text((10, 10), '\n'.join(msg), font=fnt, fill=WHITE)

    inkyphat.set_colour('black')  # 'red' is much slower
    inkyphat.set_border(inkyphat.BLACK)
    inkyphat.set_image(img)
    inkyphat.show()


def main():
    filepath = sys.argv[1]

    if os.path.isfile(filepath):
        show_image(filepath)
    else:
        print('error opening ' + filepath)


if __name__ == "__main__":
    main()
