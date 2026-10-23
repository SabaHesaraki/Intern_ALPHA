# Time Machine Lab (Task 01.4.B)

## Difference Between `git diff` and `git diff --staged`
- **`git diff`**: Shows unstaged changes between the Working Directory and the Staging Area (Index). It shows what you modified but have not yet added with `git add`.
- **`git diff --staged`** (or `git diff --cached`): Shows staged changes between the Staging Area (Index) and the latest commit (`HEAD`). It shows what will go into your next commit.

## 1. Commit Log
```text
57b6b47 (HEAD -> main) feat(week-01): finish the story
e468a70 feat(week-01): add commit line
a33898f feat(week-01): add git line
ab2acc9 feat(week-01): add terminal line
31e34d9 feat(week-01): add terminal line
