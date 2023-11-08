T = int(input())

for t in range(1, T + 1):
    answer = []
    N = int(input())

    for i in range(N):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(answer[i - 1][j - 1] + answer[i - 1][j])
        answer.append(temp)
    print('#%d' % t)
    for i in answer:
        print(*i)
