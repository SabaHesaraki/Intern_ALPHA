from byte_report import to_binary, char_count, note_path

assert to_binary(72) == "01001000", to_binary(72)
assert to_binary(0) == "0", to_binary(0)
assert to_binary(1) == "00000001", to_binary(1)
assert to_binary(5) == "00000101", to_binary(5)
assert char_count("سلام") == 4, char_count("سلام")
assert note_path("notes", "binary.md") == "notes/binary.md", note_path("notes", "binary.md")
print("all good")

