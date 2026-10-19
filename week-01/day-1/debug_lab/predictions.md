# Predictions (before running)

- to_binary(72): I expect the loop to stop early and give 1001000 (only 7 bits).
- to_binary(5): I think it gives 01 or something wrong, because the loop stops when n becomes 1.
- to_binary(1): probably an empty string, since the loop condition n > 1 is false right away.
- to_binary(0): empty string, the loop never runs.
- char_count("Hi"): 2 (correct by accident).
- char_count("سلام"): 8 (it counts bytes instead of characters).

