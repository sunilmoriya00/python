import os
import shutil
SOURCE_DIR = "source-dir-path" 
DEST_DIR = "dest-dir-path"
file_type = "file-type"

for fname in os.listdir(SOURCE_DIR):
    if fname.lower().endswith(file_type):
        print "moving"
        shutil.move(os.path.join(SOURCE_DIR, fname), DEST_DIR)
