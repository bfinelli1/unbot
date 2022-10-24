#!/usr/bin/env python3

import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
import random
import textwrap
import re
import argparse
import os
from dotenv import load_dotenv
load_dotenv()

num_images=1 #num of images to request from unsplash
left_margin=40
top_margin=40
text_line_width=30 #text wrap
name_size=20
text_size=70
Red=150
Green=150
Blue=150


parser = argparse.ArgumentParser(description='fetch images from unsplash')
parser.add_argument('-s', '--search', metavar='search', default='space', help='term to search for in unsplash.')
parser.add_argument('-f', '--file', metavar='file', default="", help="file with text on individual lines to overlay on images.")
parser.add_argument('-t', '--font', metavar='font', default="arial.ttf", help="truetype font file.")
parser.add_argument('-a',  action='store_true', help="save urls of fetched images.")
args = parser.parse_args()

font_name=args.font
try:
    file = open(args.file, 'r')
    text = file.readlines()
except:
    #example text to overlay on images
    text = ["Space: the final frontier. These are the voyages of the starship Enterprise. Its five-year mission: to explore strange new worlds.",
    "Space: the final frontier. These are the voyages of the starship Enterprise.",
    "Space is big", 
    "In space no one can hear you scream", 
    "the sun is a star", 
    "one small step for man; one giant leap for mankind.",]


r = requests.get(f'https://api.unsplash.com/photos/random?query={args.search}&count={num_images}', 
headers={'Authorization': f'Client-ID {os.getenv("Client-ID")}'})

if not r:
    print(r.text)
    print(r.status_code)
    exit()

for entry in r.json():
    if args.a:
        with open('urls.txt', "a") as file:
            file.write(entry['urls']['regular'])
    print(entry['urls']['regular'])
    print(entry['alt_description'])
    print(entry['user']['name'])

    img_data = requests.get(entry['urls']['regular']).content

    #download_location
    download_loc = entry['links']['download_location']
    dreq = requests.get(download_loc, headers={'Authorization': f'Client-ID {os.getenv("Client-ID")}'})
    print(f"download status code: {dreq.status_code}")

    name = entry['user']['name']
    name = re.sub(r'[^a-zA-Z -.]', '', name)
    img = Image.open(io.BytesIO(img_data))
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype(font=font_name, size=name_size)
    I1.text((10,10), f"image by: {name}", (Red,Green,Blue), font=myFont)

    myFont = ImageFont.truetype(font=font_name, size=text_size)
    offset=top_margin
    for line in textwrap.wrap(random.choice(text), width=text_line_width):
        I1.text((left_margin,offset), line, (Red,Green,Blue), font=myFont)
        offset+=myFont.getsize(line)[1]
    img.save(f"{name}-{entry['id']}.jpg")
    