#!/bin/bash

INKY_DIR=$HOME/inky-box
INKY_IMAGE_FILE=$INKY_DIR/data/inky-screen.png

# Fetch the image
curl -o $INKY_IMAGE_FILE --silent $INKY_IMAGE_URL

# Update screen
python3 $INKY_DIR/update-inky.py $INKY_IMAGE_FILE
