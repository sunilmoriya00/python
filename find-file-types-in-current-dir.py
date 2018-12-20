import os

files = os.listdir(os.curdir)
for file in files:
	if file.endswith('.txt'):
		print file
