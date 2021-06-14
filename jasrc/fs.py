import os
import jasrc
import shutil

def initfs(prefix, post=False):
    mcmetatemp = {
        "pack": {
        "pack_format": 1,
        "description": jasrc.conf()['desc']
        }
    }

    def defaulticon():
        jasrc.initicon()
        if jasrc.tempconf()[3] == 'False':
            print('Progress: %100')
        jasrc.log('No icon found, using default template', 1)

    def icon():
        try:
            shutil.copyfile(cfg['icon'], f'{prefix}/pack.png')
        except:
            defaulticon()

    def mcmeta():
        with open(f'{prefix}/pack.mcmeta', 'w') as w:
            w.write(str(mcmetatemp))

    def dirs():
        os.makedirs(f'{prefix}/assets/minecraft/textures/blocks')
        os.makedirs(f'{prefix}/assets/minecraft/mcpatcher/ctm/clay/blue')
        os.mkdir(f'{prefix}/assets/minecraft/mcpatcher/ctm/clay/red')
        os.mkdir(f'{prefix}/assets/minecraft/mcpatcher/ctm/clay/white')
        os.makedirs(f'{prefix}/assets/minecraft/mcpatcher/ctm/clay/topbridgeclay/blue')
        os.mkdir(f'{prefix}/assets/minecraft/mcpatcher/ctm/clay/topbridgeclay/red')
        os.mkdir(f'{prefix}/assets/minecraft/mcpatcher/ctm/clay/topbridgeclay/white')

    if post == True:
        icon()
    else:
        dirs()
        mcmeta()