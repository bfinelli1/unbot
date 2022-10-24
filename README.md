# unsplashbot
setup:

pip3 install -r requirements.txt

usage: unsplash.py [-h] [-s search] [-f file] [-t font] [-a]

fetch images from unsplash

optional arguments:

  -h, --help            show this help message and exit

  -s search, --search search

                        term to search for in unsplash.

  -f file, --file file  file with text on individual lines to overlay on

                        images.

  -t font, --font font  truetype font file.

  -a                    save urls of fetched images.
