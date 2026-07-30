# Day2 extra contents - exercises 2
# enumerate を使ってみよう

# Q1: 以下のリストを enumerate で「1番: 〇〇」の形式で表示してください。
subjects = ['国語', '数学', '英語', '理科', '社会']
for ???, ??? in enumerate(subjects, start=???):
    print(f'???番: ???')

print('---')

# Q2: 得点が 70 点以上の人を「〇番目: 〇〇（〇〇点）」と表示してください。
scores = [('田中', 85), ('鈴木', 62), ('佐藤', 90), ('山田', 73)]
for i, (name, score) in enumerate(scores):
    if ???:
        print(f'{i}番目: {name}（{score}点）')
