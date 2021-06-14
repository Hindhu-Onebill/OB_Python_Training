stmt = input("Enter a string : ")
list1 = list(stmt)
set1 = set(list1)
for i in set1:
    print(i, "--", list1.count(i))
