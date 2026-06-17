#修正方法1：sorted() に変える

scores = [78, 95, 61, 88, 43]

result = sorted(scores, reverse=True)  # ← sorted() に変える
print("高い順：", result)


#修正方法2：sort()のまま、printを直す
scores = [78, 95, 61, 88, 43]

scores.sort(reverse=True)    # 元のリスト自体が並び替えられる
print("高い順：", scores)    # ← result ではなく scores を表示


#出力結果（修正方法1, 2のどちらも同じ）
#高い順： [95, 88, 78, 61, 43]
