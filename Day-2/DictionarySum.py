d = dict()

for i in range(int(input("how many inputs ?"))):
    key, value = input("enter key and value:").split()
    d[key] = int(value)

sum1 = 0
for value in d.values():
    sum1 += value

print("sum of values:", sum1)

