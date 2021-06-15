from random import *
import math
import string
t = []
for i in range(6):
    if i % 2 == 0:
        t.append(choice(string.digits))
    elif i % 2 == 1:
        t.append(choice(string.ascii_lowercase))
print("Password : ", *t, sep="")
