# Testing Documentation - Terminal Toolkit

This document outlines the manual test plan and test cases for `terminal-toolkit`.

## Test Environment
- **OS:** Linux / Windows
- **Python Version:** 3.10+
- **Manager:** uv

---

## Test Cases

### 1. Unit Converter
- **Test ID:** TC-CONV-01
- **Input Sequence:** `1` -> `km2mi` -> `42.195`
- **Expected Output:** `42.20 km = 26.22 mi`
- **Status:** Passed

- **Test ID:** TC-CONV-02 (Error Handling)
- **Input Sequence:** `1` -> `c2f` -> `abc`
- **Expected Output:** `Error: Please enter a valid number.`
- **Status:** Passed

---

### 2. Tip Calculator
- **Test ID:** TC-TIP-01
- **Input Sequence:** `2` -> `100` -> `15` -> `2`
- **Expected Output:**
```text
  Tip amount: $15.00
  Total bill: $115.00
  Each person pays: $57.50
  

