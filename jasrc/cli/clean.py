import os
import shutil

def clean():
	os.remove('jasrc/temp.txt')
	shutil.rmtree('pack')
