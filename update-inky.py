"""Render an overlay on a background image, and display on the
inky pHAT.
"""

import datetime
import os
import sys
from subprocess import check_output

import requests

import inkyphat
from PIL import Image, ImageDraw, ImageFont

WHITE = 0
BLACK = 1
RED = 2

WIDTH=212
HEIGHT=104

def dump_image():
    im = Image.new((WIDTH, HEIGHT), 1)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            p = inkyphat.getpixel((x, y))
            im.putpixel(p)

    im.save('~/inkypi-test.png')


def chunkstring(string, length):
    return (string[0 + i : length + i] for i in range(0, len(string), length))


def get_font(name, size):
    path = os.path.join(os.environ["INKY_DIR"], "fonts/" + name)
    font = ImageFont.truetype(path, size)
    return font


def show_image(filepath):
    img = Image.open(filepath)

    pixel_font = get_font("SFPixelate.ttf", 9)
    medium_font = get_font("SFPixelate.ttf", 18)
    # large_font = get_font('SFPixelate.ttf', 36)

    d = ImageDraw.Draw(img)

    time_string = datetime.datetime.now().strftime("%H:%M")
    ip_address = check_output(["hostname", "-I"]).decode("utf-8").strip()
    info_string = f"{ip_address} / {time_string}"

    d.text((1, 95), info_string, font=pixel_font, fill=WHITE)

    quote_url = "https://notify.goude.se/quote"
    quote = requests.get(quote_url).text
    quote_font = pixel_font
    chunk_width = 35

    quote = "\n".join(chunkstring(quote, chunk_width))

    d.multiline_text((1, 1), quote, font=quote_font, fill=WHITE)

    inkyphat.set_colour("black")  # 'red' is much slower
    inkyphat.set_border(inkyphat.BLACK)
    inkyphat.set_image(img)
    inkyphat.show()


def main():
    filepath = sys.argv[1]

    if os.path.isfile(filepath):
        show_image(filepath)
    else:
        print("error opening " + filepath)

    dump_image()

if __name__ == "__main__":
    main()
