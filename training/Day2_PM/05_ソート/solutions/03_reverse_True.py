scores = [85, 42, 96, 71, 58]

scores.sort(reverse=True)
print(scores)

# 逆順に並び替える [96, 85, 71, 58, 42]



scores = [85, 42, 96, 71, 58]

new_scores = sorted(scores, reverse=True)
print(new_scores)

# 逆順に並び替える（新しいリストを作成） [96, 85, 71, 58, 42]



names = ["田中", "佐藤", "鈴木", "伊藤", "渡辺"]

print(sorted(names)) # 昇順に並び替える ["伊藤", "鈴木", "田中", "佐藤", "渡辺"]
print(sorted(names, reverse=True)) # 降順に並び替える ["渡辺", "佐藤", "田中", "鈴木", "伊藤"]


