import os
import jasrc

class Commands:
    
    def help():
        print('''
        usage: python jase.py [ARGS]

        args:
              -c --config [CONFIG_PATH]     --- Path to config file (defaults to conf.txt) 
              -h --help                     --- Displays this message
              -m --minecraft                --- Outputs the pack archive directly into the 
                                                .minecraft folder specified in your config
              -n --noerr                    --- Stops the output of errors
              -v --verbose                  --- Displays more in depth status messages
        ''')

    def write(v):
        try:
            with open('jasrc/log/temp.txt', 'a') as w:
                w.write(str(v) + '\n')
        except:
            jasrc.log('Tempfile error', 0)

    def cli(v):

        if '-h' in v or '--help' in v:
            Commands.help()
            pass

        if '-c' in v or '--config' in v:
            try:
                Commands.write(v[v.index('-c')+1])
            except:
                Commands.write(v[v.index('--config')+1])
        else:
            Commands.write('conf.txt')

        if '-m' in v or '--minecraft' in v:
            Commands.write('True')
        else:
            Commands.write('False')

        if '-n' in v or '--nolog' in v:
            Commands.write('True')
        else:
            Commands.write('False')

        if '-v' in v or '--verbose' in v:
            Commands.write('True')
        else:
            Commands.write('False')

        jasrc.vlog(f'Selected args: {v}', 1)
        if jasrc.tempconf()[3] == 'False':
            print('Progress: %0')
