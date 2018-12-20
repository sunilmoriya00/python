import os

files = os.listdir(os.curdir)
#print files
for file in files:
	if file.endswith('.txt'):
		print file
