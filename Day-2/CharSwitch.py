stmt = input("Enter the string")
position, character = int(input("Enter the position and letters:")), input()

print(position)
print(character)
print("After replacement")
print(stmt[:position]+character+stmt[position:])
