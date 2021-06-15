import os
import jasrc

class Main:

    def write(v):
        with open('jasrc/log/temp.txt', 'a') as w:
            w.write(str(v) + '\n')

    def handle(v):

        # help
        if '-h' in v or '--help' in v:
            jasrc.cli.help()

        # config 
        if '-c' in v or '--config' in v:
            try:
                Main.write(
                    v[v.index('-c')+1]
                    )
            except:
                Main.write(
                    v[v.index('--config')+1]
                    )
        else:
            Main.write(jasrc.Vars.confpath)


        # verbose
        if '-v' in v or '--verbose' in v:
            Main.write('True')
        else:
            Main.write('False')

        # clean
        if '-C' in v or '--clean' in v:
            jasrc.cli.clean()

        # genconf 
        if '-g' in v or '--genconf' in v:
            jasrc.cli.genconf()

        # confgen  
        if '-G' in v or '--confgen' in v:
            try:
                jasrc.cli.confgen(
                    v[c.index('-g')+1]
                    )
            except:
                jasrc.cli.confgen(
                    v[c.index('--genconf')+1]
                    )

        if not '-G' in v or '--confgen' or '-g' in v or '--genconf' or '-C' in v or '--clean':
            jasrc.main()
            