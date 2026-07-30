# Day2 extra contents - solution 6
# enumerate チャレンジ問題の回答

# Challenge 1:
# 次のリストを使って、「偶数番目」(2番, 4番, ...) の科目だけを表示してください。
subjects = ['国語', '数学', '英語', '理科', '社会', '音楽']
for i, subject in enumerate(subjects, start=1):
    if i % 2 == 0:
        print(f'{i}番: {subject}')

print('---')

# Challenge 2:
# 80 点以上の人だけを「1位: 名前（点数）」の形式で表示してください。
# 条件に合った人だけに順位を振る
scores = [('田中', 85), ('鈴木', 62), ('佐藤', 90), ('山田', 73), ('高橋', 88)]
rank = 1
for name, score in scores:
    if score >= 80:
        print(f'{rank}位: {name}（{score}点）')
        rank += 1

print('---')

# Challenge 3:
# 次の買い物リストの中から、3文字以上のものだけを「番号: 商品名」の形式で表示してください。
items = ['パン', 'りんご', '牛乳', 'チョコ', '米']
for i, item in enumerate(items, start=1):
    if len(item) >= 3:
        print(f'{i}番: {item}')
