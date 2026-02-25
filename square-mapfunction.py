def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]

print("***This will print the square of each number***")
for num in numbers:
    print(square(num))

square_map = map(square, numbers)
print(square_map)
print(id(square_map))

square_list = list(square_map)
print(square_list)

data = list(map(int, input("Enter numbers separated by space: ").strip().split()))
print("You entered:", data)
print("Their squares:", list(map(square, data)))

   ######output
****This will print the square of each number***
1
4
9
16
25
<map object at 0x792d97ff9c60>
133236730600544
[1, 4, 9, 16, 25]
Enter numbers separated by space: 2 4 3 0
You entered: [2, 4, 3, 0]
Their squares: [4, 16, 9, 0]

=== Code Execution Successful ===
