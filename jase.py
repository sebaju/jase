import os
import sys
import jasrc
import shutil

prefix = 'pack'

def main():
    jasrc.Commands.cli(sys.argv)
    jasrc.initfs(prefix)
    jasrc.initprop(prefix)
    jasrc.initimg('red', 'white', 'blue')
    jasrc.initfs(prefix, True)
    jasrc.zipit(prefix)

if __name__ == '__main__':
    try:
        try:
            os.remove('jasrc/log/temp.txt')
        except:
            pass
        main()
        jasrc.checkup()
        os.remove('jasrc/log/temp.txt')
    except:
        try:
            os.remove('jasrc/log/temp.txt')
            shutil.rmtree(prefix)
        except:
            pass
