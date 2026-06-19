"""
チャレンジアップ 02: コードのバグを見つけよう
以下のコードにはミスが一つあります。何が問題かを突き止め、正しく直してください。

ヒント:
- scores.sort()は何かを「返して」いる？
- result = scores.sort(reverse=True) と書いたとき、resultの中身は何になる？
"""

scores = [78, 95, 61, 88, 43]

result = scores.sort(reverse=True)
print("高い順:", result)


# TODO: 正しいコードに直してみよう