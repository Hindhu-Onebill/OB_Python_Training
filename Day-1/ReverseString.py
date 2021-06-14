stmt = input("Enter string").split()
list1 = []
for i in stmt:
    list1.append(i[::-1])
print(" ".join(list1))
