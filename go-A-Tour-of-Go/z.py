import os

name = ["nil-slices", "append", "range"]
for i in range(41, 42):
    for j in name:
        os.system("mkdir %s-%s" % (i ,j))
        os.system("touch %s-%s.go" % (i, j))