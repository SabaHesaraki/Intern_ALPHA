Bug Log - Week 1 / Day 1

Bug 1: to_binary(0) is empty
- Problem: When I ran to_binary(0), it gave nothing.
- Cause: The loop condition was n > 1, so it skipped 0 and 1.
- Fix: Handled n == 0 right at the start and changed the loop to while n > 0.

Bug 2: to_binary(72) is only 7 bits
- Problem: Number 72 printed as 1001000 instead of 8 bits.
- Cause: The loop stopped too early and lost the last bit, plus no padding.
- Fix: Fixed the loop condition and used .zfill(8) to make it 8 bits.

Bug 3: char_count counts bytes
- Problem: For the Persian word سلام, char_count returned 8 characters (which is the byte size).
- Cause: The function was using len(text.encode("utf-8")).
- Fix: Changed it to just len(text).

Bug 4: wrong path on Linux
- Problem: It created a weird file named notes\binary.md in the main folder instead of inside the notes folder.
- Cause: Using hardcoded Windows backslash in note_path.
- Fix: Replaced it with os.path.join(folder, file_name).
