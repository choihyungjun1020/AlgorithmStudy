n, m = map(int, input().split())

b = [i+1 for i in range(n)]

for i in range(m):
    r1, r2 = map(int, input().split())
    b[r1-1], b[r2-1] = b[r2-1], b[r1-1]

print(*b)