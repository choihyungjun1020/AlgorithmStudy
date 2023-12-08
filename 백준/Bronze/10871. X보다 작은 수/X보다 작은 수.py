n, x = map(int, input().split())
a = list(map(int, input().split()))
count = 0

for i in a:
    if x > i:
        print(i, end=" ")