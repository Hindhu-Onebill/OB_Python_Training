lst = []
n = int(input("Enter the number of scores: "))

for i in range(0, n):
    value = int(input())
    lst.append(value)
print("The scores are:")
print(lst)

lst.sort()
print("Runner up score is: ")
print(lst[n-2])
