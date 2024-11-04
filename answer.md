# 期中考
>
>學號：112111219
><br />
>姓名：陳恩偉
><br />
>作業撰寫時間：50 (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2024/11/04
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容


a. 小題

Ans

```python
map = [[0 for _ in range(10)] for _ in range(10)]
```

b. 小題

Ans

```python
rowmap = [0,0,0,0,0,0,0,0,0,0]

```
c. 小題

Ans

```python
rowmap = [0,7,13,28,44,62,74,75,87,90]
```

d. 小題

Ans
```python
map = [[0 for _ in range(10)] for _ in range(10)]
rowmap = [0,7,13,28,44,62,74,75,87,90]
for i in rowmap:
    r = i // 10
    c = i % 10
    map[r][c] = "*"

```

e. 小題

Ans
```python
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
```
