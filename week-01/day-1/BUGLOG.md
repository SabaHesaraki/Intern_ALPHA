# Bug Log — byte_report.py

## 1. Real Bugs

### Bug 1: Persian Text Count (Characters vs Bytes)
- **Problem**: `len()` counts string letters, not bytes. Persian letters take 2 bytes in UTF-8, so "سلام" counted wrong.
- **Fix**: Used `text.encode('utf-8')` to get the correct byte size.

### Bug 2: Windows Path Slash Error
- **Problem**: Using Windows backslashes (`\`) broke file paths on Linux/WSL2.
- **Fix**: Used `os.path.join()` so paths work everywhere.

---

## 2. Learning Notes (Extra Improvements)
*(Notes on small edge cases, not actual bugs)*

- **Zero Binary Fix**: `bin(0)` gave weird output, so we added a simple check to handle zero correctly.
- **8-bit Padding**: Used `.zfill(8)` to make sure binary numbers always show 8 full digits (like `01001000`).
