"""
Day3: 集合の基本（追加問題・任意）解答
"""

# 【基本】集合を作って操作してみよう

# 数値4つを入れた集合を作り、printで表示してみよう
nums = {1, 2, 3, 4}
print(nums)  # → {1, 2, 3, 4}

# リスト [1, 2, 2, 3, 3] から set() で集合を作り、printしてみよう
print(set([1, 2, 2, 3, 3]))  # → {1, 2, 3}

# 空の集合を set() で作り、printしてみよう
empty = set()
print(empty)  # → set()


# 【普通】追加・削除・確認をしてみよう

# 集合 {1, 2, 3} に add() で 4 を追加し、printしてみよう
nums = {1, 2, 3}
nums.add(4)
print(nums)  # → {1, 2, 3, 4}

# 集合 {1, 2, 3, 4} から remove() で 2 を削除し、printしてみよう
nums.remove(2)
print(nums)  # → {1, 3, 4}

# 集合 {1, 2, 3} に対して 3 in と 9 in の結果をそれぞれprintしてみよう
nums = {1, 2, 3}
print(3 in nums)  # → True
print(9 in nums)  # → False


# 【難しい】複数の操作を組み合わせてみよう

# 文字列のリスト ["東京", "大阪", "東京", "名古屋", "大阪"] から
# 重複を除いた集合を作り、要素数をlen()でprintしてみよう
cities = ["東京", "大阪", "東京", "名古屋", "大阪"]
unique_cities = set(cities)
print(len(unique_cities))  # → 3

# 集合 {1, 2, 3, 4, 5} に add() で 6 を追加し、remove() で 1 を削除した後
# 4 in と 9 in の結果をそれぞれprintしてみよう
nums = {1, 2, 3, 4, 5}
nums.add(6)
nums.remove(1)
print(4 in nums)  # → True
print(9 in nums)  # → False

# 集合に対して in と and を組み合わせて
# 「3も4も含まれているか」を1行で確認してprintしてみよう
nums = {1, 2, 3, 4, 5}
print(3 in nums and 4 in nums)  # → True