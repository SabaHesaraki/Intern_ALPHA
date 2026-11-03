```text
FUNCTION make_change(amount: int) -> str:
coins = [20, 10, 5]
result = []

FOR coin IN coins:
WHILE amount >= coin:
amount -= coin
result.append(coin)

RETURN result
END FUNCTION
