T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        A, B = B, A

    max = 0

    for i in range(M - N + 1):
        temp = 0
        for j in range(N):
            temp += A[j] * B[j + i]
        if temp > max:
            max = temp

    print(f"#{t} {max}")
