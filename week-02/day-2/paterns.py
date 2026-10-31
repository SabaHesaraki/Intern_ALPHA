while True:
    user_input = input("Enter n (between 2 and 15): ").strip()
    
    is_valid = True
    if user_input.startswith("-"):
        temp = user_input[1:]
    else:
        temp = user_input
        
    if not temp.isdigit():
        is_valid = False
    else:
        n = int(user_input)
        if not (2 <= n <= 15):
            is_valid = False
            
    if not is_valid:
        print("invalid input, try again")
        continue
    break

print("\npattern 1 (right triangle)")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\npattern 2 (number triangle)")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\npattern 3 (hollow square)")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\npattern 4 (diamond)")
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    for s in range(spaces):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

for i in range(n - 2, 0, -2):
    spaces = (n - i) // 2
    for s in range(spaces):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

