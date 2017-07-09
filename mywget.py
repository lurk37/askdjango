# mywget.py

import os
import sys
import requests

def main(url):
    data = requests.get(url).content
    filename = os.path.basename(url.split('?')[0])

    with open(filename, 'wb') as f:
        f.write(data)

    print('saved : {}'.format(filename))

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except (IndexError, KeyError):
        print('usage : {} <url>'.format(sys.argv[0]))
        sys.exit(1)