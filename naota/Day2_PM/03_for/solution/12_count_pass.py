scores = [45, 72, 58, 90, 61]
pass_count = 0

for score in scores:
    if score >= 60:
        pass_count += 1

print(f"合格した人数: {pass_count} 人")
