import jasrc.nutils
import jasrc

def checkup():
    if jasrc.nutils.update() == True:
        jasrc.vlog('No new updates', 1)
    elif jasrc.nutils.update() == False:
        jasrc.log('An update is availible. If you would like to stop seeing these messages, edit jasrc/econf.py', 1)