matrix = [[1, -2, 3], [0, 5, -1], [4, 0, 2]]

result = []
for row in matrix:
    for x in row:
        if x > 0:
            result.append(x)

print(result)
