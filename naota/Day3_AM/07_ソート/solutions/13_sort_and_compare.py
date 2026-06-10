class_a = [70, 55, 90, 65, 80]
class_b = [85, 60, 75, 95, 50]

sorted_a = sorted(class_a, reverse=True)  # ① class_a を降順に並べた新しいリスト
sorted_b = sorted(class_b, reverse=True)  # ② class_b を降順に並べた新しいリスト

print("研修A（高い順）：", sorted_a)
print("研修B（高い順）：", sorted_b)
print("元の研修A：", class_a)   # 変わっていない！
print("元の研修B：", class_b)   # 変わっていない！


#出力結果
#研修A（高い順）： [90, 80, 70, 65, 55]
#研修B（高い順）： [95, 85, 75, 60, 50]
#元の研修A： [70, 55, 90, 65, 80]
#元の研修B： [85, 60, 75, 95, 50]
