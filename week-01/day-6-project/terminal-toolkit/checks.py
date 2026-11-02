"""Assertion tests for terminal toolkit pure functions."""

from toolkit import text_stats, tip_breakdown

# Test tip_breakdown function
tip_res = tip_breakdown(100.0, 10, 2)
assert tip_res == (10.0, 110.0, 55.0)

# Test text_stats function
stats_res = text_stats("Hello World")
assert stats_res["chars"] == 11
assert stats_res["words"] == 2

print("checks ok")

