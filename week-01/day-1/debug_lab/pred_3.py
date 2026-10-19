# PREDICT: Which paths are absolute, and what will be printed?

import os

print(os.path.join("home", "sara", "code"))
print(os.path.normpath("/home/sara/code/../notes.txt"))
print(os.path.isabs("code/hello.py"))
print(os.path.isabs("/etc/hosts"))

