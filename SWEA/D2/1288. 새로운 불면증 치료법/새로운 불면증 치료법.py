# set, update를 사용하면 됨.

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = set()
    answer = N
    while (True):
        for i in list(str(answer)):
            nums.add(i)
        if len(nums) == 10:
            break
        answer += N
    print(f"#{t} {answer}")