scores = [85, 42, 96, 71, 58]
print("元のリスト:", scores)  # [85, 42, 96, 71, 58]

new_scores = sorted(scores) # 並び替え後の新しいリストを作成
print("元のリスト:", scores)  # [85, 42, 96, 71, 58] ← 変わっていない！
print("並び替え後:", new_scores)  # [42, 58, 71, 85, 96]
