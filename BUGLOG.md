# Bug Log - Day 2

## Bug 1: Report file overwritten
- **Symptom:** Only the last line appeared in report.txt; previous lines were lost.
- **Cause:** Using single redirection `>` which overwrites the file.
- **Fix:** Used `>` only for the first line and `>>` for following lines to append data.
- **Lesson:** `>` replaces file content; `>>` appends to it.

## Bug 2: Space in path caused errors
- **Symptom:** Errors like `No such file` when file paths had spaces.
- **Cause:** Unquoted variable `$LOG` split into multiple arguments (word splitting).
- **Fix:** Put double quotes around variables: `"$LOG"`.
- **Lesson:** Always quote path variables to handle spaces correctly.

## Bug 3: Exit code overwritten by echo
- **Symptom:** Payment failure alert always printed, even when tests passed.
- **Cause:** The `echo` command ran between `grep` and `if [ $? -eq 0 ]`, changing `$?`.
- **Fix:** Put the `grep` command directly inside the `if` condition.
- **Lesson:** Check `$?` immediately or use the command directly in the condition.

## Bug 4: Wrong sorting order for top users
- **Symptom:** Least active users showed up first instead of top users.
- **Cause:** Default `sort -n` sorts in ascending order.
- **Fix:** Changed it to `sort -nr` for descending (reverse) numeric order.
- **Lesson:** Use `-r` with sort to get highest values first.
