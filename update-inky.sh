#!/bin/bash

PHAT_DIR=$HOME/inky-box
IMAGE_FILE=$PHAT_DIR/data/inky-screen.png

# Fetch the image
curl -o $IMAGE_FILE --silent $IMAGE_URL

# Update screen
python3 $PHAT_DIR/inky-update.py $IMAGE_FILE
