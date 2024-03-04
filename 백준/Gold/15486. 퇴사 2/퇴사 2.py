import sys

n = int(sys.stdin.readline())

# 상담을 하는데 필요한 시간 리스트 t
# 상담을 하면 얻을 수 있는 이익 리스트 p
t, p = [], []

# i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
dp = [0] * (n + 1)

for _ in range(n):
    # 날짜별 상담 완료 기간 및 상담 완료 금액 저장
    x, y = map(int, sys.stdin.readline().split(" "))
    t.append(x)
    p.append(y)

max_value = 0

for i in range(n - 1, -1, -1):
    if i + t[i] <= n:  # 상담이 끝나는 날짜가 n을 초과하지 않는 경우
        dp[i] = max(dp[i + t[i]] + p[i], dp[i + 1])
    else:  # 상담을 할 수 없는 경우
        dp[i] = dp[i + 1] # 다음 날의 이익을 현재 날짜에 반영

print(dp[0])