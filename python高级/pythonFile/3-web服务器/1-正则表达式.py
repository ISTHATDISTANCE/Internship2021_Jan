import re

# 判断163邮箱地址

email = input("Email address: ")

if (re.match(r'^[a-zA-Z0-9_]{4,20}@(163|126|qq)\.com$', email)):
    print("Valid")
else:
    print("Invalid")