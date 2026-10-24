total_seconds = int(input("Seconds: "))

days, rest = divmod(total_seconds, 86400)

hours, rest = divmod(rest, 3600)

minutes, seconds = divmod(rest, 60)

print(f"{total_seconds} seconds = {days} days, {hours:02d}:{minutes:02d}:{seconds:02d}")
