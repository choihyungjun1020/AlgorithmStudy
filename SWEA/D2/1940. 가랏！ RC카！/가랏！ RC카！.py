T = int(input())

for t in range(1, T + 1):
    N = int(input())
    length = 0
    speed = 0
    for _ in range(N):
        command = list(map(int, input().split()))
        if command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            if (speed - command[1]) < 0:
                speed = 0
            else:
                speed -= command[1]
        length += speed
    print(f"#{t} {length}")