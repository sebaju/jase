def confgen(v):
	if v == 

def genconf(v):
	with open('jasrc/cli/res/defaultconf.txt', 'r') as r:
		out = r.read()
		out = out.replace('{{1}}', jasrc.Vars.genheight)

		with open(jasrc.Vars.confpath, 'w') as w:
			w.write(out)