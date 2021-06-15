import time
import jasrc
from colorama import Fore, Style

def log(a, t, n=False):

    logfile = 'jasrc/log/jase.log'

    error = '{}[{}ERROR{}{}]{}{} '.format(Style.BRIGHT, Fore.RED, Fore.RESET, Style.BRIGHT, Style.NORMAL, Fore.RESET)
    info = '{}[{}INFO{}{}]{}{} '.format(Style.BRIGHT, Fore.YELLOW, Fore.RESET, Style.BRIGHT, Style.NORMAL, Fore.RESET)
    success = '{}[{}SUCCESS{}{}]{}{} '.format(Style.BRIGHT, Fore.GREEN, Fore.RESET, Style.BRIGHT, Style.NORMAL, Fore.RESET)

    if n == False:
        if t == 0:
            print(error + a)
        elif t == 1:
            print(info + a)
        elif t == 2:
            print(success + a)
    else:
        pass

    t = time.strftime('%d-%M-%S', time.localtime())

    with open(logfile, 'a') as w:
        w.write(t, a + '\n')

def vlog(a, t, n=False):
    if jasrc.tempconf(3) == 'True':
        log(a, t, n)