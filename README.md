# unsplashbot
fetch random images from unsplash and overlay text on those images

setup:

pip3 install -r requirements.txt

have file called '.env' with line: Client-ID=\<your client id\>

usage: 

./unsplash.py [-h] [-s search] [-f file] [-t font] [-a]

optional arguments:

  -h, --help            show this help message and exit

  -s search, --search   term to search for in unsplash.

  -f file, --file       file with text on individual lines to overlay on images.

  -t font, --font       truetype font file.

  -a                    save urls of fetched images.
