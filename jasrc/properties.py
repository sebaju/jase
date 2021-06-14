import jasrc

def initprop(prefix, *col):
	redmeta = 14
	bluemeta = 11
	whitemeta = 0

	split = jasrc.conf()['split']

	def checkcol(i):
		global meta
		if i == 'red':
			meta = redmeta
		elif i == 'blue':
			meta = bluemeta
		elif i == 'white':
			meta = whitemeta
		else:
			meta= '69'

	def topbridge():
		for i in col:
			with open(f'{prefix}/assets/minecraft/mcpatcher/ctm/clay/topbridgeclay/{i}/{i}topbridge.properties', 'w') as w:
				checkcol(i)
				mcptemp = f'matchBlocks=159\nmetadata={meta}\nmethod=ctm\nheights={split}-255\ntiles=0-46'
				w.write(str(mcptemp))

	def bridge():
		s = int(split)-1
		for i in col:
			with open(f'{prefix}/assets/minecraft/mcpatcher/ctm/clay/{i}/clay.properties', 'w') as w:
				checkcol(i)
				mcptemp = f'matchBlocks=159\nmetadata={meta}\nmethod=ctm\nheights=0-{s}\ntiles=0-46'
				w.write(str(mcptemp))

	topbridge()
	bridge()
        
