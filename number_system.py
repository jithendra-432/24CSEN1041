print("Supported Bases:")
print("2  -> Binary")
print("8  -> Octal")
print("10 -> Decimal")
print("16 -> Hexadecimal")
print("---------------------------------------------")

num = input("Enter the number: ")
source_base = int(input("Enter source base (2 / 8 / 10 / 16): "))
target_base = int(input("Enter target base (2 / 8 / 10 / 16): ")) 

decimal = int(num, source_base)

if target_base == 2:
    result = bin(decimal)[2:]
elif target_base == 8:
    result = oct(decimal)[2:]
elif target_base == 10:
    result = decimal
elif target_base == 16:
    result = hex(decimal)[2:].upper()
else:
    result = "Invalid base"

print("\nConverted Value =", result)


#output 
   Supported Bases:
2  -> Binary
8  -> Octal
10 -> Decimal
16 -> Hexadecimal
---------------------------------------------
Enter the number: 1010
Enter source base (2 / 8 / 10 / 16): 2
Enter target base (2 / 8 / 10 / 16): 16

Converted Value = A
