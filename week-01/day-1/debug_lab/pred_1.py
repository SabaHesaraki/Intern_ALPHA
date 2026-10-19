# PREDICT: What are the character and byte counts?

word = "Hi"
farsi = bytes.fromhex("d8b3 d984 d8a7 d985").decode("utf-8")

print(len(word), len(word.encode("utf-8")))
print(len(farsi), len(farsi.encode("utf-8")))
print(farsi.encode("utf-8"))

