import re

names = ["name1", "_name", "2_name", "__name__"]

_nam = 1

for nam in names:
    res = re.match("[a-zA-Z_]+[\w]*", nam)
    if res:
        print("%s is legal" % nam)
    else:
        print("%s is illegal" % nam)
