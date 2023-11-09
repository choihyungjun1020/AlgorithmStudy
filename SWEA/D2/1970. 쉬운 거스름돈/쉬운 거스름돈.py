# 최소한의 거스름 돈 갯수
moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    count_list = []

    for i in range(len(moneys)):
        count_list.append(N // moneys[i])
        N %= moneys[i]

    print(f"#{t}")

    for i in count_list:
        print(f"{i}", end=" ")
    print()
