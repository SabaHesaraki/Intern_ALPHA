# Debug Lab & PRED Log (Task 01.3.PRED)

## Snippet 1
- Code:
  x = 7
  x * 6
  print(x * 6)
  "hello".upper()
  print("done")
- Prediction: It will print 42 and done. The expression x * 6 alone doesn't print without print().
- Actual Output: 42, done
- Explanation: In scripts, expression results are not printed automatically unless wrapped in print(). "hello".upper() changes case but doesn't print or save unless assigned or printed.

## Snippet 2
- Code:
  print("start")
  if 2 > 3:
      print(undefined_name)
  print("middle")
  print(undefined_name)
  print("end")
- Prediction: It prints "start", "middle", and then crashes with a NameError because undefined_name is not defined.
- Actual Output: start, middle, NameError: name 'undefined_name' is not defined
- Explanation: Python executes line by line. The `if` condition (2 > 3) is False, so the code inside it is skipped (no error there!). But the last `print(undefined_name)` runs outside the if block and crashes the program at runtime.

## Snippet 3
- Code:
  import dis
  def double(n):
      return n * 2
  dis.dis(double)
  print(double.__code__.co_varnames)
- Prediction: It disassembles the function into bytecode instructions and prints variable names.
- Actual Output: Bytecode instructions (LOAD_FAST, BINARY_OP, etc.) and tuple ('n',)
- Explanation: Python compiles source code into Bytecode so the Python Virtual Machine (PVM) can execute it. `dis` lets us inspect those low-level instructions.

