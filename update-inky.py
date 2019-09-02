#!/usr/bin/env python3

import os
import sys
from PIL import Image

import inkyphat

colour = 'black'
#colour = 'red'

filepath = sys.argv[1]

if os.path.isfile(filepath):
    inkyphat.set_colour(colour)
    inkyphat.set_border(inkyphat.BLACK)
    inkyphat.set_image(Image.open(filepath))
    inkyphat.show()
else:
    print('error opening ' + filepath)
