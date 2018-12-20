file1 = "file1-path"
file2 = "file2-path"

with open(file1, 'r') as f1:
    data = f1.read()
    d1 = data.split("\n")
    print "data in file1 is: ", d1

with open(file2, 'r') as f2:
    data = f2.read()
    d2 = data.split("\n")
    print "data in file2 is: ", d2

for item in d1:
    if item in data:
        print item, "is present "
    else:
        print item, "is not present"
