n, m = map(int, input().split())

b = [0] * n

for i in range(m):
    r1, r2, num = map(int, input().split())
    r1 -= 1
    for j in range(r1, r2):
        b[j] = num

print(*b)