#!/usr/bin/env bash

# 1. Total lines
echo "= total lines ="
wc -l < server.log

# 2. Level counts
echo "= levels ="
awk '{print $3}' server.log | sort | uniq -c | sort -nr

# 3. All ERROR lines with line numbers
echo "= error lines ="
grep -n "ERROR" server.log

# 4. Save non-INFO and non-DEBUG lines to problems.txt
grep -E "WARNING|ERROR" server.log > problems.txt

# 5. Top user
echo "= top user ="
grep -o 'user=[a-z]*' server.log | sort | uniq -c | sort -nr | head -n 1

