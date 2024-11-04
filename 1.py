map = [[0 for _ in range(10)] for _ in range(10)]
rowmap = [0,7,13,28,44,62,74,75,87,90]
for i in rowmap:
    r = i // 10
    c = i % 10
    map[r][c] = "*"

for k in range(10):
    for j in range(10):
        if map[k][j] == "*":
            continue
        count = 0
        for x in range(max(0, k-1), min(10, k+2)):
            for y in range(max(0, j-1), min(10, j+2)):
                if map[x][y] == "*":
                    count += 1
        map[k][j] = count if count > 0 else " "

for row in map:
    print(row)