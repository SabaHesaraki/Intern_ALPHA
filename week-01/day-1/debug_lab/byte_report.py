import os

def to_binary(n):
    if n == 0:
        return "0"
    
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
        
    return bits.zfill(8)

def char_count(text):
    return len(text)

def byte_count(text):
    return len(text.encode("utf-8"))

def note_path(folder, file_name):
    return os.path.join(folder, file_name)

def report(word, number, folder):
    print(f"word          : {word}")
    print(f"characters    : {char_count(word)}")
    print(f"utf-8 bytes   : {byte_count(word)}")
    print(f"binary({number}) : {to_binary(number)}")
    
    path = note_path(folder, "binary.md")
    print(f"saving to     : {path}")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(to_binary(number) + "\n")
        
    print(f"saved?        : {os.path.exists(os.path.join(folder, 'binary.md'))}")

os.makedirs("notes", exist_ok=True)

report("Hi", 72, "notes")
report(bytes.fromhex("d8b3 d984 d8a7 d985").decode("utf-8"), 0, "notes")
