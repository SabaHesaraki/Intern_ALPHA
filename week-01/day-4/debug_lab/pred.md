# Predict -> Run -> Explain Lab (Task 01.4.PRED)

## Snippet 1
- **What happens:** `git show HEAD:a.txt` prints "v1". `git status` shows `a.txt` has unstaged changes.
- **Why:** Changing the file to "v2" after doing `git add` does not include "v2" in the commit. Git commits what was staged, not what is currently in the working directory.

## Snippet 2
- **What happens:** `.gitignore` ignores untracked files, but not files that are already tracked or staged.
- **Why:** Once a file is added to Git, putting it in `.gitignore` won't stop Git from tracking it unless you remove it first using `git rm --cached`.

## Snippet 3
- **What happens:** `git commit --amend` updates the last commit instead of creating a new one, so the total commit count stays the same. `git rm --cached` stops tracking the `.env` file.
- **Why:** Amend is useful for fixing the previous commit, and `rm --cached` keeps the local file while removing it from Git control.

