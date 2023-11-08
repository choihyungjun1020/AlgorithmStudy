T = int(input())

for t in range(1, T + 1):
    N = int(input())
    val = ""
    for _ in range(N):
        C, K = input().split()
        K = int(K)
        val += C * K
    print(f"#{t}")

    for i in range(len(val)):
        if (i + 1) % 10 == 0:
            print(val[i])
        else:
            print(val[i], end="")
    print()
