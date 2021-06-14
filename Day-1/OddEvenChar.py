s = input("Enter a string")

s_odd = ""
s_even = ""
for i in range(0, len(s)):
    if i % 2 == 1:
        s_odd += s[i]
    else:
        s_even += s[i]
print(s_odd+s_even)
