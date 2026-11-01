# Fibonacci numbers and step count

n = int(input("Enter the value of n: "))

a = 0
b = 1
step_count = 0

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")

    # Count basic operations
    step_count += 1       # print
    c = a + b
    step_count += 1       # addition
    a = b
    step_count += 1       # assignment
    b = c
    step_count += 1       # assignment

print("\nStep Count:", step_count)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")