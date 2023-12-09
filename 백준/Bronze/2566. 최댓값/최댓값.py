lst = [list(map(int, input().split())) for _ in range(9)]

mx = 0
maxR, maxC = 0, 0

for row in range(9):
    for col in range(9):
        if mx <= lst[row][col]:
            maxR = row + 1
            maxC = col + 1
            mx = lst[row][col]

print(mx)
print(maxR, maxC)
