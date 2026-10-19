# Binary & UTF-8 Findings

- Every 8 bits equal one Byte (e.g., 0100 means 4 bits, so 8 bits make a full byte).
- When using `wc -c` on the Persian string "سلام", it returns 8 instead of 4 because each Persian character in UTF-8 takes 2 bytes, making 4 * 2 = 8 bytes in total.
- The value `48` in Hex converts to Decimal 72, which represents the ASCII/Unicode character 'H' (or the 8th letter corresponding to binary values).

