# Trace Table Tasks - Week 02 / Day 2

## Trace 1
```python
x = 1
for i in range(4):
x = x * 2 + i
print(x)

Step	Variable i	Previous x	Operation (x * 2 + i)	New x
Start (Init)	-	-	-	1
Loop 1 (i = 0)	0	1	1 * 2 + 0	2
Loop 2 (i = 1)	1	2	2 * 2 + 1	5
Loop 3 (i = 2)	2	5	5 * 2 + 2	12
Loop 4 (i = 3)	3	12	12 * 2 + 3	27               



n = 37
steps = 0
while n != 1:
n = n // 2 if n % 2 == 0 else 3 * n + 1
steps += 1
if steps > 5:
break
print(n, steps)


Step	Check n != 1	Check Even n % 2 == 0	New n	New steps	Check steps > 5
Start	-	-	37	0	-
Step 1	37 ≠ 1 (True)	Odd (False)	3 * 37 + 1 = 112	1	No
Step 2	112 ≠ 1 (True)	Even (True)	112 // 2 = 56	2	No
Step 3	56 ≠ 1 (True)	Even (True)	56 // 2 = 28	3	No
Step 4	28 ≠ 1 (True)	Even (True)	28 // 2 = 14	4	No
Step 5	14 ≠ 1 (True)	Even (True)	14 // 2 = 7	5	No
Step 6	7 ≠ 1 (True)	Odd (False)	3 * 7 + 1 = 22	6	Yes -> break 


s = ""
for i in range(3):
for j in range(i + 1):
s += str(j)
s += "|"
print(s)


Outer Loop i	Inner Loop j	Changes to s	Current s
Start	-	-	""
i = 0	j = 0	s += "0", `s += "	"`
i = 1	j = 0, 1	s += "0", s += "1", `s += "	"`
i = 2	j = 0, 1, 2	s += "0", s += "1", s += "2", `s += "	"`



count = 0
for ch in "mississippi":
if ch == "s":
continue
if ch == "p":
break
count += 1
else:
count = -1
print(count)



Character ch	Check ch == ‘s’	Check ch == ‘p’	count Value	Explanation
'm'	False	False	1	Increased (0 + 1)
'i'	False	False	2	Increased (1 + 1)
's'	True (continue)	-	2	Skipped
's'	True (continue)	-	2	Skipped
'i'	False	False	3	Increased (2 + 1)
's'	True (continue)	-	3	Skipped
's'	True (continue)	-	3	Skipped
'i'	False	False	4	Increased (3 + 1)
'p'	False	True (break)	4	Loop stops




