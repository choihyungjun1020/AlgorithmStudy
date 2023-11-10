# 구현문제

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    length = 0
    speed = 0
    for _ in range(N):
        value = list(map(int, input().split()))
        if value[0] == 0:
            length += speed
        elif value[0] == 1:
            speed += value[1]
            length += speed
        else:
            if value[1] > speed:
                speed = 0
                length = length
            else:
                speed -= value[1]
                length += speed
    print(f"#{t} {length}")
