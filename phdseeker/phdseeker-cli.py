#!/usr/bin/env python3
'''
phdseeker-cli

Usage:
    phdseeker-cli -h
    phdseeker-cli -V
    phdseeker-cli [-k <keywords> --maxpage=<n> --output=<filetype(s)> -v]

options:
    -h --help                       Show this screen.
    -V --version                    Show version.
    -v --verbose                    Show the sought position on the terminal.
    -k <keywords>, --keywords=<keywords>    Declare desired keywords to seek. [default: Computer Science, Machine Learning, Deep Learning]
    -o <filetype(s)>, --output=<filetype(s)>     Set the output type csv/xlsx/both [default: both]
    --maxpage=<n>                   Maximum number of pages to fetch. [default: 10]
'''

import sys
from docopt import docopt
from main import PhDSeeker
from constants import __version__
from time import perf_counter
from rich import print

def main(args=docopt(__doc__)):
    """
    main()
    ======
    """
    if args['--version']:
        print(f"PhD-Seeker Version {__version__}")
        sys.exit()

    keywords = args['--keywords']
    maxpage = int(args['--maxpage'])
    verbose = args['--verbose']
    output = args['--output']

    s = 's' if maxpage>1 else ''
    print(f"Searching for the Keywords '{keywords}' in up to {maxpage} page{s}.")
    s = perf_counter()
    ps = PhDSeeker(keywords, maxpage=maxpage)
    ps.save(output)
    print(f"\nElapsed time is {perf_counter()-s:.2f} seconds.")

    if args['--verbose']:
        print(ps)


if __name__ == "__main__":
    main(docopt(__doc__))
