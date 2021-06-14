list1 = [int(x) for x in input("Enter tuple elements").split(",")]
tuple1 = tuple(list1)
print("Sum:", sum(tuple1))
avg = sum(tuple1)/len(tuple1)
print("Average :", avg)
