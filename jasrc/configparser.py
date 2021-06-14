import jasrc

def tempconf():
    global confdir

    try:
        with open('jasrc/log/temp.txt', 'r') as r:
            out = r.read()
            out = out.split('\n')

            return out
    except:
        pass

def conf():

    try:
        config = tempconf()[0]

        c = []
        cl = []
        co = []
        with open(config, 'r') as r:
            out = r.read()
            out = out.split('\n')

            for i in out:
                c.append(i.split(':'))
            for i in c:
                cl.append(i[-1])
            for i in cl:
                co.append(i.strip())
            for i in co:
                if i == '':
                    co.remove(i)
            for i in co:
                if i.startswith('#'):
                    co.remove(i)

            return {
                'w': co[0], 'wd': co[1], 'tw': co[2], 'twd': co[3], 
                'r': co[4], 'rd': co[5], 'tr': co[6], 'trd': co[7], 
                'b': co[8], 'bd': co[9], 'tb': co[10], 'tbd': co[11],
                'name': co[12], 'desc': co[13], 'icon': co[14],
                'split': co[15],
                'mcf': co[16]

            }
    except:
        jasrc.log('Error parsing config', 0)