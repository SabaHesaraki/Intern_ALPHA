
## 1. What I built
- **Environment & Machine Stats (`machine.md`)**: Configured WSL2 Ubuntu and documented system specs (CPU, RAM, disk).
- **Binary & Encodings (`binary.md`)**: Analyzed binary numbers, bits, and UTF-8 multi-byte encoding.
- **Path Mapping (`paths.md`)**: Mapped directory structures and practiced Linux paths.
- **Bug Hunt (`BUGLOG.md` & `byte_report.py`)**: Fixed bugs related to UTF-8 byte lengths, string counts, and path separators.
- **Prediction Lab (`debug_lab/`)**: Wrote prediction scripts (`pred_1.py`, `pred_2.py`, `pred_3.py`) to test Python string and OS functions before execution.

---

## 2. How to run

### WSL2 Setup (Windows PowerShell as Admin):
```powershell
wsl --install -d Ubuntu-22.04  

## 3. What was hard
- Understanding why `len(str)` counts characters while `len(str.encode('utf-8'))` counts actual bytes (causing Persian text to take 2 bytes per char).
- Fixing platform-specific path issues where Windows backslashes (`\`) break on Linux POSIX file systems.
- Setting up GitHub Personal Access Tokens (PAT) to successfully push commits.

## 4. What I learned
- How to run a real Linux kernel natively inside Windows using WSL2.
- The difference between absolute paths and relative paths, and how `os.path.normpath` works.
- Writing predictions before executing code to improve active debugging.

## 5. AI usage
- Used AI to clarify Linux kernel versions and distributions.
- Discussed edge cases in Python string encodings and binary number formatting.
- Reviewed Git rebase and merge strategies.

