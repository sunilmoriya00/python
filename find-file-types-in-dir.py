import os

dirpath = "enter dir path"
ftype = "enter file type"
files = os.listdir(dirpath)
for file in files:
	if file.endswith(ftype):
		print file
