stmt = input("Enter the string to format : ")
print(stmt)

for i in range(0, len(stmt), 1):
    if stmt[i] == ' ':
        stmt = stmt.replace(stmt[i], '-')

print(stmt)
