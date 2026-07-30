# Day2 extra contents - solution 2
# enumerate を使ってみよう

# Q1: 科目を 1 番から表示する
subjects = ['国語', '数学', '英語', '理科', '社会']
for i, s in enumerate(subjects, start=1):
    print(f'{i}番: {s}')

print('---')

# Q2: 70点以上の人を表示する
scores = [('田中', 85), ('鈴木', 62), ('佐藤', 90), ('山田', 73)]
for i, (name, score) in enumerate(scores):
    if score >= 70:
        print(f'{i}番目: {name}（{score}点）')
