stmt = input("Enter the string")
li = list(stmt)
num_check, alpha, digit, upper, lower = False, False, False, False, False

for i in li:
    if i.isalnum():
        num_check = True
    if i.isalpha():
        alpha = True
    if i.isdigit():
        digit = True
    if i.isupper():
        upper = True
    if i.islower():
        lower = True

print("\n", num_check, "\n", alpha, "\n", digit, "\n", upper, "\n", lower)
