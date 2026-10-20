# Linux & Bash Cheat Sheet

1. `pwd`: Print current working directory.
2. `ls -la`: List all files including hidden ones with details.
3. `cd ..`: Move up one directory level.
4. `mkdir -p dir/sub`: Create nested directories without errors.
5. `touch file.txt`: Create a new empty file.
6. `cp -r src dest`: Copy directories recursively.
7. `mv old new`: Move or rename files and folders.
8. `rm -r folder`: Remove a folder and its contents.
9. `cat file`: Display file content.
10. `head -n 5 file`: Show the first 5 lines of a file.
11. `tail -n 5 file`: Show the last 5 lines of a file.
12. `wc -l file`: Count total lines in a file.
13. `wc -c file`: Count byte size of a file.
14. `grep "word" file`: Search for text patterns in a file.
15. `grep -n "word" file`: Search text and show line numbers.
16. `grep -v "word" file`: Show lines not matching the pattern.
17. `grep -E "a|b" file`: Search multiple patterns (OR condition).
18. `cut -d' ' -f2 file`: Extract specific columns using delimiters.
19. `awk '{print $3}' file`: Process and print specific text columns.
20. `sort -nr`: Sort numbers in reverse (descending) order.
21. `uniq -c`: Count duplicate consecutive lines.
22. `>`: Redirect output and overwrite file.
23. `>>`: Redirect output and append to file.
24. `|` (Pipe): Send output of one command as input to another.
25. `chmod +x script.sh`: Make a script executable.
26. `echo $?`: Show exit status of the last command (0 = success).
27. `source ~/.bashrc`: Reload bash configuration instantly.
