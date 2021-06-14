import jasrc
from PIL import Image, ImageColor

def htr(hex):
	return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def initicon():
	jc = jasrc.conf()
	img = Image.new('RGB', (16, 16))
	new = [htr(jc['rd']),htr(jc['rd']),htr(jc['rd']),htr(jc['rd']),htr(jc['rd']),htr(jc['rd']),htr(jc['wd']),htr(jc['wd']),htr(jc['wd']),htr(jc['wd']),htr(jc['bd']),htr(jc['bd']),htr(jc['bd']),htr(jc['bd']),htr(jc['bd']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['r']),htr(jc['rd']),htr(jc['wd']),htr(jc['w']),htr(jc['w']),htr(jc['wd']),htr(jc['bd']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['b']),htr(jc['bd']),
		htr(jc['rd']),htr(jc['rd']),htr(jc['rd']),htr(jc['rd']),htr(jc['rd']),htr(jc['rd']),htr(jc['wd']),htr(jc['wd']),htr(jc['wd']),htr(jc['wd']),htr(jc['bd']),htr(jc['bd']),htr(jc['bd']),htr(jc['bd']),htr(jc['bd']),htr(jc['bd'])]

	img.putdata(new)
	img.save('pack/pack.png')