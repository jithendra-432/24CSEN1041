my_set = {10, 20, 30}

for item in my_set:
    print(item)

##output 
10
20
30


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)
print(A.union(B))
print(A & B)
print(A.intersection(B))
print(A - B)
print(A.difference(B))
print(A ^ B)
print(A.symmetric_difference(B))

##output
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
{3, 4}
{3, 4}
{1, 2}
{1, 2}
{1, 2, 5, 6}
{1, 2, 5, 6}

=== Code Execution Successful ===

s = {1, 2, 3}

# Add element
s.add(4)

# Remove element (error if not found)
s.remove(2)

# Discard element (no error if not found)
s.discard(10)

# Pop random element
s.pop()

# Clear all elements
s.clear()

print(s)

##output

set()

=== Code Execution Successful ===
