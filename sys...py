
import sys

print("Enter numbers (0 to stop):")

while True:
    num = int(input("Enter a number: "))

    # Exit condition
    if num == 0:
        print("Program terminated.")
        sys.exit()

    # Skip negative numbers
    if num < 0:
        print("Negative number skipped.")
        continue

    # Placeholder for future logic
    if num == 1:
        pass   # maybe special handling later

    # Branching logic
    if num % 2 == 0:
        print(num, "is an EVEN number")
    else:
        print(num, "is an ODD number")

    # Stop loop after number exceeds limit
    if num > 50:
        print("Limit exceeded, stopping loop.")
        break

print("Loop ended normally.")
### output 
        Enter numbers (0 to stop):
Enter a number: -4
Negative number skipped.
Enter a number: 5
5 is an ODD number
Enter a number: -88
Negative number skipped.
Enter a number: 23
23 is an ODD number
Enter a number: 85
85 is an ODD number
Limit exceeded, stopping loop.
Loop ended normally.
>>>
