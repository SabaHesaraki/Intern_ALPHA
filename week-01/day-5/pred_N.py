a = "5"
b = 3

print(a * b)
print(int(a) * b)
print(a + str(b))
print(float(a) / 2, int(a) // 2, -7 // 2)

name = " Mina "
name.strip()
print(f"[{name}]")
name = name.strip().upper()
print(f"[{name}]", len(name))
print(name[1:3], name[-1], name[::-1])

total = 10 + 20 * 3 ** 2 / 6
print(total)
print(0.1 * 3 == 0.3, round(0.1 * 3, 2) == 0.3)
print(round(2.5), round(3.5), round(2.675, 2))
print(int(" 42 "), int(9.99))

