from datetime import *
string = input("enter time( 01:01:20 AM/PM):")
result = datetime.strptime(string, "%I:%M:%S %p")
print(result.strftime("%H:%M:%S %p"))
