'''Render an overlay on a background image, and display on the
inky pHAT.
'''

import datetime
import os
import requests
import sys
from subprocess import check_output

from PIL import Image, ImageFont, ImageDraw

import inkyphat

WHITE = 0
BLACK = 1
RED = 2


def chunkstring(string, length):
    return (string[0 + i:length + i] for i in range(0, len(string), length))


def get_font(name, size):
    path = os.path.join(os.environ['INKY_DIR'], 'fonts/' + name)
    font = ImageFont.truetype(path, size)
    return font


def show_image(filepath):
    img = Image.open(filepath)

    pixel_font = get_font('SFPixelate.ttf', 9)
    large_font = get_font('SFPixelate.ttf', 36)

    d = ImageDraw.Draw(img)

    time_string = datetime.datetime.now().strftime('%H:%M')
    ip_address = check_output(['hostname', '-I']).decode('utf-8').strip()
    info_string = f'{ip_address} / {time_string}'

    d.text((1, 95), info_string, font=pixel_font, fill=WHITE)
    # d.text((1, 65), time_string, font=large_font, fill=WHITE)

    quote_url = 'https://notify.goude.se/quote'
    quote = requests.get(quote_url).text
    chunk_width = 20
    quote = '\n'.join(chunkstring(quote, chunk_width))  # split string if it doesn't fit

    if len(quote) < 50:
        quote_font = large_font
    else:
        quote_font = pixel_font

    d.multiline_text((1, 1), quote, font=quote_font, fill=WHITE)

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
