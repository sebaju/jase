import os
import jasrc
import shutil

prefix = 'pack'
colors = 'red', 'white', 'blue'

def second():
    jasrc.initfs(prefix)
    jasrc.initprop(prefix, colors)
    jasrc.initimg(colors)
    jasrc.initfs(prefix, True)
    jasrc.zipit(prefix)

def main()
    try:
        try:
            os.remove('jasrc/log/temp.txt')
        except:
            pass
        second()
        jasrc.checkup()
        os.remove('jasrc/log/temp.txt')
    except:
        try:
            os.remove('jasrc/log/temp.txt')
            shutil.rmtree(prefix)
        except:
            pass