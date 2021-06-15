import re
import jasrc

def tempconf(index):
    global confdir

    with open('jasrc/log/temp.txt', 'r') as r:
        out = r.read()
        out = out.split('\n')

        return out[index]


def conf(index):
    # config = tempconf()[0]
    config = 'conf.txt'

    stage1, stage2, stage3 = [], [], {}
    with open(config, 'r') as r:
        stage0 = r.read()
        stage0 = stage0.split('\n')

        for i in stage0:
            if i == '':
                stage0.remove(i)
        for i in stage0:
            if i.startswith('#'):
                stage0.remove(i)
        for i in stage0:
            stage1.append(i.split(':', 1))
        for i in stage1:
            stage2.append(
                [i[0], 
                str(i[1]).strip()]
                )   
        for i in stage2:
            stage3[i[0]] = i[1]

        return stage3[index]