def help():
    print('''
    usage: python jase.py [ARGS]

    args:
          -c --config [CONFIG_PATH]     --- Path to config file (defaults to jase.conf)
          -C --clean                    --- Cleans the file system
          -g --genconf opt.[IMAGE_PATH] --- Generates a config file (optionaly based on a pallete image)
          -h --help                     --- Displays this message
          -v --verbose                  --- Displays more in depth status messages
    ''')