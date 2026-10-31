count = 0
total_sum = 0
max_score = None
min_score = None
passed_count = 0

while True:
    user_input = input("score (or done): ").strip()
    
    if user_input.lower() == "done":
        break
    
    is_valid = True
    if user_input.startswith("-"):
        temp_input = user_input[1:]
    else:
        temp_input = user_input
        
    if not temp_input.isdigit():
        is_valid = False
    else:
        score = int(user_input)
        if not (0 <= score <= 100):
            is_valid = False
            
    if not is_valid:
        print("invalid input, try again")
        continue
    
    count += 1
    total_sum += score
    
    if max_score is None or score > max_score:
        max_score = score
        
    if min_score is None or score < min_score:
        min_score = score
        
    if score >= 50:
        passed_count += 1

if count == 0:
    print("no scores entered")
else:
    avg = total_sum / count
    pass_percentage = (passed_count / count) * 100
    print(f"count: {count} | sum: {total_sum} | avg: {avg:.1f}")
    print(f"max: {max_score} | min: {min_score}")
    print(f"passed: {passed_count} ({pass_percentage:.1f}%)")

