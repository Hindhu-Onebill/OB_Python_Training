stmt = input("Enter string:")
list1 = list(stmt)
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print("".join(list2))
