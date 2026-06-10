temps = [32, 25, 29, 38, 21, 35, 27]

sorted_temps = sorted(temps)          # ① 元のリストを残すので sorted() を使う
print("並び替え後：", sorted_temps)   # [21, 25, 27, 29, 32, 35, 38]
print("最低気温：", sorted_temps[0])  # ② 先頭が一番小さい → 21
print("最高気温：", sorted_temps[-1]) # ③ 末尾が一番大きい → 38


#出力結果
#並び替え後： [21, 25, 27, 29, 32, 35, 38]
#最低気温： 21
#最高気温： 38
