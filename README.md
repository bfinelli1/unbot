# unsplashbot
setup:

pip3 install -r requirements.txt



usage: 

./unsplash.py [-h] [-s search] [-f file] [-t font] [-a]

fetch random images from unsplash and overlay text on images

optional arguments:

  -h, --help            show this help message and exit

  -s search, --search   term to search for in unsplash.

  -f file, --file       file with text on individual lines to overlay on images.

  -t font, --font       truetype font file.

  -a                    save urls of fetched images.
