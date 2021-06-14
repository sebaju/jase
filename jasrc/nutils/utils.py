import requests
from jasrc import cfu

def update():
    if cfu == True:
        r = requests.get('https://raw.githack.com/sebaju/jase/main/VERSION.txt')
        newv = int(r.text)
        with open('jasrc/nutils/VERSION.txt', 'r') as r:
            oldv = int(r.read())

        if not oldv == newv:
            return False
        else:
            return True
    else:
        return