import os
import math
import jasrc
from PIL import Image, ImageColor

def htr(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def initimg(*cols):
    aa = 1
    prog = 0
    dar = ['a', 'b']
    for a in list(cols):
        jasrc.vlog(f'Now on {a}', 1)
        if a == 'white':
            col = 'w'
            cold = 'wd'
        elif a == 'red':
            col = 'r'
            cold = 'rd'
        elif a == 'blue':
            col = 'b'
            cold = 'bd'

        for b in dar:
            jasrc.vlog(f'Now on {b}', 1)
            if b == 'a':
                col = col
                cold = cold
            elif b == 'b':
                col = 't' + col
                cold = 't' + cold
                a = 'topbridgeclay/' + a

            for c in os.listdir('res/variation'):
                img = Image.open('res/variation/' + c)
                data = img.getdata()
                new = []

                for d in data:
                    if d == (255,255,255):
                        new.append(htr(jasrc.conf()[col]))
                    else:
                        new.append(htr(jasrc.conf()[cold])) 

                img.putdata(new)           
                img.save(f'pack/assets/minecraft/mcpatcher/ctm/clay/{a}/' + c)
                jasrc.vlog(c, 2)

                aa += 1
                progBef = prog
                prog = math.floor(aa/284*100)
                
                if jasrc.tempconf()[3] == 'False':
                    if not progBef == prog:
                        print(f'Progress: %{prog}')


    for a in list(cols):
        if a == 'white':
            col = 'w'
            cold = 'wd'
        elif a == 'red':
            col = 'r'
            cold = 'rd'
        elif a == 'blue':
            col = 'b'
            cold = 'bd'

        img = Image.open('res/base/base.png')
        data = img.getdata()
        new = []

        for b in data:
            if d == (255,255,255):
                new.append(htr(jasrc.conf()[col]))
            else:
                new.append(htr(jasrc.conf()[cold]))
 
        img.putdata(new)
        img.save(f'pack/assets/minecraft/textures/blocks/hardened_clay_stained_{a}.png')
        jasrc.vlog(f'{a}.png', 2)

