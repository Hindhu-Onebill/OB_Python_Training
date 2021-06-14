stmt1 = input("Enter first string :")
stmt2 = input("Enter second string :")
if stmt1 == stmt2:
    print("Equal")
else:
    if len(stmt1) > len(stmt2):
        print("First string is larger than second")
    else:
        print("Second is larger than first")
